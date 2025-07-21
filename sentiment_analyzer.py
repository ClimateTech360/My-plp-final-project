import re
import numpy as np
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
from collections import Counter

class SentimentAnalyzer:
    def __init__(self):
        """Initialize the sentiment analyzer with multiple NLP tools."""
        self.vader_analyzer = SentimentIntensityAnalyzer()
        
        # Try to load spaCy model, fall back to basic processing if not available
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            self.nlp = None
        
        # Mental health keywords and indicators
        self.mental_health_keywords = {
            'depression': ['depressed', 'depression', 'sad', 'hopeless', 'worthless', 'empty', 'numb', 'despair'],
            'anxiety': ['anxious', 'anxiety', 'worried', 'panic', 'fear', 'nervous', 'stress', 'overwhelmed'],
            'suicidal': ['suicide', 'kill myself', 'end it all', 'don\'t want to live', 'want to die', 'life not worth'],
            'self_harm': ['cut myself', 'hurt myself', 'self harm', 'cutting', 'burning myself'],
            'isolation': ['alone', 'lonely', 'isolated', 'no friends', 'nobody cares', 'disconnected'],
            'sleep_issues': ['insomnia', 'can\'t sleep', 'nightmares', 'tired', 'exhausted'],
            'eating_issues': ['not eating', 'can\'t eat', 'binge', 'purge', 'weight loss', 'weight gain'],
            'substance_use': ['drinking', 'drugs', 'high', 'drunk', 'escape', 'numb the pain']
        }
        
        # Positive mental health indicators
        self.positive_keywords = {
            'gratitude': ['grateful', 'thankful', 'blessed', 'appreciate'],
            'joy': ['happy', 'joy', 'excited', 'cheerful', 'delighted'],
            'hope': ['hope', 'optimistic', 'looking forward', 'positive'],
            'support': ['friends', 'family', 'loved ones', 'support', 'help'],
            'coping': ['meditation', 'exercise', 'therapy', 'counseling', 'self-care']
        }
    
    def preprocess_text(self, text):
        """Clean and preprocess text for analysis."""
        # Convert to lowercase
        text = text.lower()
        
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Handle contractions and common abbreviations
        contractions = {
            "don't": "do not",
            "won't": "will not", 
            "can't": "cannot",
            "n't": " not",
            "'re": " are",
            "'ve": " have",
            "'ll": " will",
            "'d": " would",
            "'m": " am"
        }
        
        for contraction, expansion in contractions.items():
            text = text.replace(contraction, expansion)
        
        return text
    
    def analyze_with_textblob(self, text):
        """Analyze sentiment using TextBlob."""
        blob = TextBlob(text)
        return {
            'polarity': blob.sentiment.polarity,  # -1 to 1
            'subjectivity': blob.sentiment.subjectivity  # 0 to 1
        }
    
    def analyze_with_vader(self, text):
        """Analyze sentiment using VADER."""
        scores = self.vader_analyzer.polarity_scores(text)
        return {
            'compound': scores['compound'],  # -1 to 1
            'positive': scores['pos'],
            'negative': scores['neg'],
            'neutral': scores['neu']
        }
    
    def extract_mental_health_keywords(self, text):
        """Extract mental health related keywords from text."""
        found_keywords = []
        text_lower = text.lower()
        
        for category, keywords in self.mental_health_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    found_keywords.append(keyword)
        
        return found_keywords
    
    def extract_positive_keywords(self, text):
        """Extract positive mental health indicators from text."""
        found_keywords = []
        text_lower = text.lower()
        
        for category, keywords in self.positive_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    found_keywords.append(keyword)
        
        return found_keywords
    
    def analyze_emotions(self, text):
        """Analyze emotional content using keyword matching and sentiment."""
        emotions = {
            'sadness': 0,
            'anxiety': 0,
            'anger': 0,
            'fear': 0,
            'joy': 0,
            'trust': 0,
            'anticipation': 0,
            'disgust': 0
        }
        
        text_lower = text.lower()
        
        # Sadness indicators
        sad_words = ['sad', 'depressed', 'down', 'blue', 'melancholy', 'grief', 'sorrow']
        emotions['sadness'] = sum(1 for word in sad_words if word in text_lower) / 10
        
        # Anxiety indicators
        anxiety_words = ['anxious', 'worried', 'nervous', 'stressed', 'panic', 'fear']
        emotions['anxiety'] = sum(1 for word in anxiety_words if word in text_lower) / 10
        
        # Anger indicators
        anger_words = ['angry', 'mad', 'furious', 'rage', 'irritated', 'frustrated']
        emotions['anger'] = sum(1 for word in anger_words if word in text_lower) / 10
        
        # Fear indicators
        fear_words = ['scared', 'afraid', 'terrified', 'frightened', 'fearful']
        emotions['fear'] = sum(1 for word in fear_words if word in text_lower) / 10
        
        # Joy indicators
        joy_words = ['happy', 'joyful', 'excited', 'cheerful', 'delighted', 'pleased']
        emotions['joy'] = sum(1 for word in joy_words if word in text_lower) / 10
        
        # Trust indicators
        trust_words = ['trust', 'confident', 'secure', 'safe', 'comfortable']
        emotions['trust'] = sum(1 for word in trust_words if word in text_lower) / 10
        
        # Anticipation indicators
        anticipation_words = ['excited', 'eager', 'hopeful', 'optimistic', 'expecting']
        emotions['anticipation'] = sum(1 for word in anticipation_words if word in text_lower) / 10
        
        # Disgust indicators
        disgust_words = ['disgusted', 'revolted', 'sick', 'nauseated']
        emotions['disgust'] = sum(1 for word in disgust_words if word in text_lower) / 10
        
        # Normalize scores
        max_score = max(emotions.values()) if max(emotions.values()) > 0 else 1
        emotions = {k: min(v / max_score, 1.0) for k, v in emotions.items()}
        
        return emotions
    
    def calculate_risk_level(self, sentiment_scores, mental_health_keywords, emotions):
        """Calculate mental health risk level based on analysis."""
        risk_score = 0
        
        # Sentiment contribution
        if sentiment_scores['textblob']['polarity'] < -0.5:
            risk_score += 2
        elif sentiment_scores['textblob']['polarity'] < -0.2:
            risk_score += 1
        
        if sentiment_scores['vader']['compound'] < -0.5:
            risk_score += 2
        elif sentiment_scores['vader']['compound'] < -0.2:
            risk_score += 1
        
        # Mental health keywords contribution
        high_risk_keywords = ['suicide', 'kill myself', 'end it all', 'want to die', 'self harm']
        moderate_risk_keywords = ['depressed', 'hopeless', 'worthless', 'anxious', 'panic']
        
        for keyword in mental_health_keywords:
            if any(hrk in keyword for hrk in high_risk_keywords):
                risk_score += 3
            elif any(mrk in keyword for mrk in moderate_risk_keywords):
                risk_score += 1
        
        # Emotion intensity contribution
        negative_emotions = ['sadness', 'anxiety', 'anger', 'fear']
        negative_intensity = sum(emotions[emotion] for emotion in negative_emotions)
        
        if negative_intensity > 2.0:
            risk_score += 2
        elif negative_intensity > 1.0:
            risk_score += 1
        
        # Determine risk level
        if risk_score >= 5:
            return 'High', 'Indicators suggest significant emotional distress. Professional support is strongly recommended.'
        elif risk_score >= 2:
            return 'Moderate', 'Some concerning indicators detected. Consider seeking support or monitoring your well-being.'
        else:
            return 'Low', 'Text shows generally stable emotional content. Continue maintaining positive mental health practices.'
    
    def analyze_text(self, text):
        """Perform comprehensive sentiment and mental health analysis."""
        if not text or not text.strip():
            return None
        
        # Preprocess text
        processed_text = self.preprocess_text(text)
        
        # Perform sentiment analysis
        textblob_results = self.analyze_with_textblob(processed_text)
        vader_results = self.analyze_with_vader(processed_text)
        
        # Extract keywords
        mental_health_keywords = self.extract_mental_health_keywords(processed_text)
        positive_keywords = self.extract_positive_keywords(processed_text)
        
        # Analyze emotions
        emotions = self.analyze_emotions(processed_text)
        
        # Calculate overall sentiment (weighted average)
        overall_sentiment = (textblob_results['polarity'] * 0.6 + vader_results['compound'] * 0.4)
        
        # Calculate emotion intensity
        emotion_intensity = max(emotions.values()) if emotions.values() else 0
        
        # Calculate risk level
        risk_level, risk_description = self.calculate_risk_level(
            {'textblob': textblob_results, 'vader': vader_results},
            mental_health_keywords,
            emotions
        )
        
        # Calculate confidence score
        sentiment_agreement = 1 - abs(textblob_results['polarity'] - vader_results['compound'])
        confidence = min(sentiment_agreement + (len(mental_health_keywords) * 0.1), 1.0)
        
        return {
            'overall_sentiment': overall_sentiment,
            'emotion_intensity': emotion_intensity,
            'confidence': confidence,
            'risk_level': risk_level,
            'risk_description': risk_description,
            'mental_health_keywords': mental_health_keywords,
            'positive_keywords': positive_keywords,
            'emotions': emotions,
            'detailed_scores': {
                'textblob': textblob_results,
                'vader': vader_results
            }
        }
