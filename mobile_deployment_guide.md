# WellNet Mobile Deployment Guide

## Overview
This guide outlines how to integrate the WellNet Flask API with mobile applications using various frameworks.

## API Endpoints Available

### Base URL: `http://your-domain.com/api`

### 1. Health Check
```
GET /api/health
Response: Service status and timestamp
```

### 2. Text Analysis
```
POST /api/analyze
Body: {"text": "Your text here"}
Response: Complete sentiment analysis with risk assessment
```

### 3. Batch Analysis
```
POST /api/batch-analyze
Body: {"texts": ["text1", "text2", ...]}
Response: Analysis results for multiple texts (max 50)
```

### 4. Crisis Resources
```
GET /api/resources/crisis
Response: Emergency helplines and crisis intervention resources
```

### 5. Mental Health Resources
```
GET /api/resources/mental-health
Response: Professional help, educational resources, and support groups
```

### 6. Safety Planning
```
GET /api/resources/safety-planning
Response: Safety planning tools and immediate coping strategies
```

## Mobile Integration Examples

### React Native Integration

```javascript
// services/wellnetApi.js
const API_BASE = 'https://your-wellnet-api.com/api';

class WellNetAPI {
  async analyzeText(text) {
    const response = await fetch(`${API_BASE}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });
    return response.json();
  }

  async getCrisisResources() {
    const response = await fetch(`${API_BASE}/resources/crisis`);
    return response.json();
  }

  async getMentalHealthResources() {
    const response = await fetch(`${API_BASE}/resources/mental-health`);
    return response.json();
  }
}

// components/SentimentAnalyzer.jsx
import React, { useState } from 'react';
import { View, TextInput, Button, Text, Alert } from 'react-native';

const SentimentAnalyzer = () => {
  const [text, setText] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeText = async () => {
    setLoading(true);
    try {
      const api = new WellNetAPI();
      const result = await api.analyzeText(text);
      
      if (result.status === 'success') {
        setAnalysis(result.analysis);
        
        // Show crisis alert for high risk
        if (result.analysis.risk_level === 'High') {
          Alert.alert(
            'Support Available',
            'If you\'re in crisis, please call 988 for immediate help.',
            [{ text: 'Call 988', onPress: () => Linking.openURL('tel:988') }]
          );
        }
      }
    } catch (error) {
      Alert.alert('Error', 'Failed to analyze text');
    }
    setLoading(false);
  };

  return (
    <View>
      <TextInput
        value={text}
        onChangeText={setText}
        placeholder="Share your thoughts..."
        multiline
      />
      <Button title="Analyze" onPress={analyzeText} disabled={loading} />
      {analysis && (
        <View>
          <Text>Risk Level: {analysis.risk_level}</Text>
          <Text>Sentiment: {analysis.overall_sentiment.toFixed(2)}</Text>
        </View>
      )}
    </View>
  );
};
```

### Flutter Integration

```dart
// lib/services/wellnet_api.dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class WellNetAPI {
  static const String baseUrl = 'https://your-wellnet-api.com/api';

  Future<Map<String, dynamic>> analyzeText(String text) async {
    final response = await http.post(
      Uri.parse('$baseUrl/analyze'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'text': text}),
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to analyze text');
    }
  }

  Future<Map<String, dynamic>> getCrisisResources() async {
    final response = await http.get(Uri.parse('$baseUrl/resources/crisis'));
    return json.decode(response.body);
  }
}

// lib/widgets/sentiment_analyzer.dart
import 'package:flutter/material.dart';
import '../services/wellnet_api.dart';

class SentimentAnalyzer extends StatefulWidget {
  @override
  _SentimentAnalyzerState createState() => _SentimentAnalyzerState();
}

class _SentimentAnalyzerState extends State<SentimentAnalyzer> {
  final _textController = TextEditingController();
  Map<String, dynamic>? _analysis;
  bool _loading = false;

  Future<void> _analyzeText() async {
    setState(() => _loading = true);
    
    try {
      final api = WellNetAPI();
      final result = await api.analyzeText(_textController.text);
      
      if (result['status'] == 'success') {
        setState(() => _analysis = result['analysis']);
        
        if (result['analysis']['risk_level'] == 'High') {
          _showCrisisDialog();
        }
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Analysis failed: $e')),
      );
    }
    
    setState(() => _loading = false);
  }

  void _showCrisisDialog() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Support Available'),
        content: Text('If you\'re in crisis, please call 988 for immediate help.'),
        actions: [
          TextButton(
            onPress: () => Navigator.pop(context),
            child: Text('OK'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextField(
          controller: _textController,
          decoration: InputDecoration(hintText: 'Share your thoughts...'),
          maxLines: 4,
        ),
        ElevatedButton(
          onPressed: _loading ? null : _analyzeText,
          child: _loading ? CircularProgressIndicator() : Text('Analyze'),
        ),
        if (_analysis != null) ...[
          Text('Risk Level: ${_analysis!['risk_level']}'),
          Text('Sentiment: ${_analysis!['overall_sentiment'].toStringAsFixed(2)}'),
        ],
      ],
    );
  }
}
```

### iOS Swift Integration

```swift
// WellNetAPI.swift
import Foundation

class WellNetAPI {
    static let baseURL = "https://your-wellnet-api.com/api"
    
    func analyzeText(_ text: String, completion: @escaping (Result<AnalysisResponse, Error>) -> Void) {
        guard let url = URL(string: "\(Self.baseURL)/analyze") else { return }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let body = ["text": text]
        request.httpBody = try? JSONSerialization.data(withJSONObject: body)
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let data = data else { return }
            
            do {
                let analysisResponse = try JSONDecoder().decode(AnalysisResponse.self, from: data)
                completion(.success(analysisResponse))
            } catch {
                completion(.failure(error))
            }
        }.resume()
    }
}

struct AnalysisResponse: Codable {
    let status: String
    let analysis: Analysis
}

struct Analysis: Codable {
    let overallSentiment: Double
    let riskLevel: String
    let riskDescription: String
    let mentalHealthKeywords: [String]
    
    enum CodingKeys: String, CodingKey {
        case overallSentiment = "overall_sentiment"
        case riskLevel = "risk_level"
        case riskDescription = "risk_description"
        case mentalHealthKeywords = "mental_health_keywords"
    }
}
```

### Android Kotlin Integration

```kotlin
// WellNetAPI.kt
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.google.gson.Gson

class WellNetAPI {
    companion object {
        private const val BASE_URL = "https://your-wellnet-api.com/api"
        private val client = OkHttpClient()
        private val gson = Gson()
    }

    suspend fun analyzeText(text: String): AnalysisResponse? = withContext(Dispatchers.IO) {
        val json = gson.toJson(mapOf("text" to text))
        val body = json.toRequestBody("application/json".toMediaType())
        
        val request = Request.Builder()
            .url("$BASE_URL/analyze")
            .post(body)
            .build()

        try {
            val response = client.newCall(request).execute()
            if (response.isSuccessful) {
                response.body?.string()?.let { responseBody ->
                    gson.fromJson(responseBody, AnalysisResponse::class.java)
                }
            } else null
        } catch (e: Exception) {
            null
        }
    }
}

data class AnalysisResponse(
    val status: String,
    val analysis: Analysis
)

data class Analysis(
    val overall_sentiment: Double,
    val risk_level: String,
    val risk_description: String,
    val mental_health_keywords: List<String>
)
```

## Deployment Options

### 1. Replit Deployment
- Use Replit's built-in deployment features
- Automatic HTTPS and domain management
- Easy scaling and monitoring

### 2. Heroku Deployment
```bash
# Install Heroku CLI and login
heroku create wellnet-api
git push heroku main
```

### 3. AWS/Google Cloud
- Use container deployment (Docker)
- Set up load balancing and auto-scaling
- Configure SSL certificates

## Security Considerations

1. **API Rate Limiting**: Implement rate limiting to prevent abuse
2. **CORS Configuration**: Configure CORS appropriately for your mobile apps
3. **Input Validation**: Validate all input data on the server side
4. **Logging**: Implement proper logging without storing sensitive data
5. **SSL/TLS**: Always use HTTPS in production

## Privacy and Ethics

1. **No Data Storage**: The API doesn't store user text or analysis results
2. **Anonymized Analytics**: Only aggregate, anonymized usage statistics
3. **Crisis Detection**: Immediate display of crisis resources for high-risk content
4. **Professional Disclaimer**: Always include disclaimers about professional help

## Testing

Test your API endpoints using tools like:
- Postman
- curl commands
- Mobile app testing frameworks

Example curl test:
```bash
curl -X POST https://your-api.com/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I am feeling great today!"}'
```

## Support and Resources

For implementation support:
1. Check the API documentation endpoint: `/api/documentation`
2. Review example implementations above
3. Test with the provided curl commands
4. Ensure proper error handling in mobile apps