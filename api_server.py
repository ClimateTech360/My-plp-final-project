from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
import logging

from sentiment_analyzer import SentimentAnalyzer
from mental_health_resources import get_mental_health_resources
from crisis_resources import get_crisis_resources, get_safety_planning_resources
from kenya_mental_health_resources import (
    get_kenya_mental_health_resources,
    get_kenya_crisis_resources,
    get_kenya_safety_planning_resources
)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize sentiment analyzer
analyzer = SentimentAnalyzer()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'WellNet Mental Health API'
    })


@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """Analyze text for mental health sentiment."""
    try:
        data = request.get_json()

        if not data or 'text' not in data:
            return jsonify({
                'error': 'Text field is required',
                'status': 'error'
            }), 400

        text = data['text']

        if not text or not text.strip():
            return jsonify({
                'error': 'Text cannot be empty',
                'status': 'error'
            }), 400

        # Perform sentiment analysis
        analysis_result = analyzer.analyze_text(text)

        if not analysis_result:
            return jsonify({
                'error': 'Analysis failed',
                'status': 'error'
            }), 500

        # Add metadata
        response_data = {
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'analysis': analysis_result,
            'input_length': len(text),
            'recommendations': generate_recommendations(analysis_result['risk_level'])
        }

        logger.info(
            f"Analysis completed for text length: {len(text)}, Risk: {analysis_result['risk_level']}")

        return jsonify(response_data)

    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'status': 'error'
        }), 500


@app.route('/api/resources/crisis', methods=['GET'])
def get_crisis_help():
    """Get crisis intervention resources - Kenya focused."""
    try:
        crisis_resources = get_kenya_crisis_resources()

        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'country': 'Kenya',
            'resources': crisis_resources
        })

    except Exception as e:
        logger.error(f"Crisis resources error: {str(e)}")
        return jsonify({
            'error': 'Failed to retrieve crisis resources',
            'status': 'error'
        }), 500


@app.route('/api/resources/mental-health', methods=['GET'])
def get_mental_health_help():
    """Get mental health resources - Kenya focused."""
    try:
        resources = get_kenya_mental_health_resources()

        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'country': 'Kenya',
            'resources': resources
        })

    except Exception as e:
        logger.error(f"Mental health resources error: {str(e)}")
        return jsonify({
            'error': 'Failed to retrieve mental health resources',
            'status': 'error'
        }), 500


@app.route('/api/resources/safety-planning', methods=['GET'])
def get_safety_help():
    """Get safety planning resources - Kenya focused."""
    try:
        safety_resources = get_kenya_safety_planning_resources()

        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'country': 'Kenya',
            'resources': safety_resources
        })

    except Exception as e:
        logger.error(f"Safety planning resources error: {str(e)}")
        return jsonify({
            'error': 'Failed to retrieve safety planning resources',
            'status': 'error'
        }), 500


@app.route('/api/batch-analyze', methods=['POST'])
def batch_analyze():
    """Analyze multiple texts in batch for research purposes."""
    try:
        data = request.get_json()

        if not data or 'texts' not in data:
            return jsonify({
                'error': 'texts field is required',
                'status': 'error'
            }), 400

        texts = data['texts']

        if not isinstance(texts, list) or len(texts) > 50:  # Limit batch size
            return jsonify({
                'error': 'texts must be a list with maximum 50 items',
                'status': 'error'
            }), 400

        results = []

        for i, text in enumerate(texts):
            if text and text.strip():
                try:
                    analysis_result = analyzer.analyze_text(text)
                    if analysis_result:
                        results.append({
                            'index': i,
                            'text_preview': text[:100] + "..." if len(text) > 100 else text,
                            'analysis': analysis_result
                        })
                    else:
                        results.append({
                            'index': i,
                            'text_preview': text[:100] + "..." if len(text) > 100 else text,
                            'error': 'Analysis failed for this text'
                        })
                except Exception as e:
                    results.append({
                        'index': i,
                        'text_preview': text[:100] + "..." if len(text) > 100 else text,
                        'error': f'Analysis error: {str(e)}'
                    })

        # Generate summary statistics
        successful_analyses = [r for r in results if 'analysis' in r]
        risk_levels = [r['analysis']['risk_level']
                       for r in successful_analyses]

        summary = {
            'total_texts': len(texts),
            'successful_analyses': len(successful_analyses),
            'failed_analyses': len(results) - len(successful_analyses),
            'risk_distribution': {
                'low': risk_levels.count('Low'),
                'moderate': risk_levels.count('Moderate'),
                'high': risk_levels.count('High')
            },
            'average_sentiment': sum(r['analysis']['overall_sentiment'] for r in successful_analyses) / len(successful_analyses) if successful_analyses else 0
        }

        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'results': results,
            'summary': summary
        })

    except Exception as e:
        logger.error(f"Batch analysis error: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'status': 'error'
        }), 500


def generate_recommendations(risk_level):
    """Generate appropriate recommendations based on risk level."""
    recommendations = {
        'High': {
            'immediate_actions': [
                'Contact a crisis helpline immediately (988 in the US)',
                'Reach out to a trusted friend, family member, or mental health professional',
                'Consider going to an emergency room if you have thoughts of self-harm',
                'Use grounding techniques to manage overwhelming emotions'
            ],
            'follow_up': [
                'Schedule an appointment with a mental health professional',
                'Create a safety plan with specific coping strategies',
                'Consider intensive outpatient or inpatient treatment if recommended',
                'Build a strong support network'
            ]
        },
        'Moderate': {
            'immediate_actions': [
                'Talk to someone you trust about how you\'re feeling',
                'Practice stress management techniques like deep breathing',
                'Engage in activities that typically bring you comfort',
                'Monitor your emotional state over the next few days'
            ],
            'follow_up': [
                'Consider scheduling an appointment with a counselor or therapist',
                'Look into local support groups',
                'Develop a regular self-care routine',
                'Learn and practice coping strategies'
            ]
        },
        'Low': {
            'immediate_actions': [
                'Continue with positive coping strategies that work for you',
                'Stay connected with your support network',
                'Maintain healthy lifestyle habits',
                'Be mindful of any changes in your emotional state'
            ],
            'follow_up': [
                'Keep engaging in activities that promote well-being',
                'Consider preventive mental health check-ins',
                'Share positive coping strategies with others',
                'Stay informed about mental health resources'
            ]
        }
    }

    return recommendations.get(risk_level, recommendations['Low'])


@app.route('/api/documentation', methods=['GET'])
def api_documentation():
    """API documentation endpoint."""
    docs = {
        'title': 'WellNet Kenya Mental Health API',
        'version': '1.0.0',
        'description': 'API for mental health sentiment analysis and Kenya-specific resource access',
        'country': 'Kenya',
        'languages': ['English', 'Swahili', 'Local Languages'],
        'endpoints': {
            '/api/health': {
                'method': 'GET',
                'description': 'Health check endpoint',
                'response': 'JSON with service status'
            },
            '/api/analyze': {
                'method': 'POST',
                'description': 'Analyze text for mental health sentiment',
                'body': {
                    'text': 'string (required) - Text to analyze'
                },
                'response': 'JSON with sentiment analysis results'
            },
            '/api/batch-analyze': {
                'method': 'POST',
                'description': 'Analyze multiple texts in batch (max 50)',
                'body': {
                    'texts': 'array of strings (required) - Texts to analyze'
                },
                'response': 'JSON with batch analysis results and summary'
            },
            '/api/resources/crisis': {
                'method': 'GET',
                'description': 'Get crisis intervention resources',
                'response': 'JSON with crisis helplines and resources'
            },
            '/api/resources/mental-health': {
                'method': 'GET',
                'description': 'Get mental health resources',
                'response': 'JSON with professional help, education, and support resources'
            },
            '/api/resources/safety-planning': {
                'method': 'GET',
                'description': 'Get safety planning resources',
                'response': 'JSON with safety planning tools and coping strategies'
            }
        },
        'usage_notes': [
            'All endpoints return JSON responses',
            'Error responses include error message and status',
            'Batch analysis limited to 50 texts per request',
            'No data is stored persistently - privacy focused',
            'Rate limiting may apply in production'
        ]
    }

    return jsonify(docs)


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'status': 'error',
        'available_endpoints': [
            '/api/health',
            '/api/analyze',
            '/api/batch-analyze',
            '/api/resources/crisis',
            '/api/resources/mental-health',
            '/api/resources/safety-planning',
            '/api/documentation'
        ]
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'status': 'error'
    }), 500


if __name__ == '__main__':
    print("🇰🇪 Starting WellNet Kenya Mental Health API Server...")
    print("📋 API Documentation: http://localhost:3000/api/documentation")
    print("🚀 Server running on http://localhost:3000")
    print("🏥 Serving Kenya's 47 counties with mental health support")
    app.run(host='0.0.0.0', port=3000, debug=True)
