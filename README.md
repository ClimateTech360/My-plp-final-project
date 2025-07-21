# 🧠 WellNet - AI-Powered Mental Health Sentiment Analysis

WellNet is a comprehensive mental health sentiment analysis system that detects emotional distress indicators and connects users with appropriate support resources. Built with ethical AI practices and privacy-first principles, WellNet supports SDG 3 (Good Health and Well-being) and SDG 16 (Peace, Justice and Strong Institutions).

## 🌟 Features

### Core Functionality
- **Multi-Model Sentiment Analysis**: Uses TextBlob, VADER, and spaCy for comprehensive text analysis
- **Real-Time Risk Assessment**: Color-coded risk levels (Low, Moderate, High) with detailed explanations
- **Mental Health Keyword Detection**: Identifies indicators of depression, anxiety, suicidal ideation, and more
- **Crisis Resource Integration**: Immediate access to crisis hotlines and emergency resources
- **Interactive Visualizations**: Charts showing sentiment trends and emotional patterns over time

### Privacy & Ethics
- **No Data Storage**: Text analysis is performed locally without persistent storage
- **Anonymous Usage**: No personal information is collected or stored
- **Professional Disclaimers**: Clear guidance about seeking professional help
- **Crisis Detection**: Automatic display of emergency resources for high-risk content

### Technical Architecture
- **Streamlit Frontend**: User-friendly web interface with responsive design
- **Flask API Backend**: RESTful API for mobile integration and third-party access
- **Modular Design**: Separate components for analysis, resources, and crisis intervention
- **Docker Support**: Containerized deployment for easy scaling
- **Mobile-Ready**: Complete mobile integration guide and API documentation

## 🚀 Quick Start

### Using Replit (Recommended)
1. The application is already configured and running
2. Streamlit Frontend: `http://localhost:5000`
3. Flask API: `http://localhost:3000`
4. API Documentation: `http://localhost:3000/api/documentation`

### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd wellnet

# Install dependencies
pip install uv
uv sync

# Download spaCy model
python -m spacy download en_core_web_sm

# Run Streamlit frontend
streamlit run app.py --server.port 5000

# Run Flask API (in separate terminal)
python api_server.py
```

### Docker Deployment
```bash
# Start both services
docker-compose up --build

# Frontend: http://localhost:5000
# API: http://localhost:3000
```

## 📱 API Usage

### Basic Text Analysis
```bash
curl -X POST http://localhost:3000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I am feeling overwhelmed and anxious today."}'
```

### Get Crisis Resources
```bash
curl -X GET http://localhost:3000/api/resources/crisis
```

### Batch Analysis (up to 50 texts)
```bash
curl -X POST http://localhost:3000/api/batch-analyze \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Text 1", "Text 2", "Text 3"]}'
```

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Service health check |
| `/api/analyze` | POST | Analyze single text |
| `/api/batch-analyze` | POST | Analyze multiple texts |
| `/api/resources/crisis` | GET | Get crisis resources |
| `/api/resources/mental-health` | GET | Get mental health resources |
| `/api/resources/safety-planning` | GET | Get safety planning tools |
| `/api/documentation` | GET | Full API documentation |

## 📱 Mobile Integration

WellNet includes comprehensive mobile integration support:

- **React Native**: Complete implementation examples
- **Flutter**: Dart integration with proper error handling  
- **iOS Swift**: Native iOS API integration
- **Android Kotlin**: Native Android implementation
- **API Documentation**: Full endpoint specifications

See `mobile_deployment_guide.md` for detailed implementation examples.

## 🏥 Mental Health Resources

WellNet integrates comprehensive mental health support:

### Crisis Resources
- **988 Suicide & Crisis Lifeline**: 24/7 crisis support
- **Crisis Text Line**: Text-based crisis intervention
- **International Resources**: Global crisis support networks
- **Specialized Support**: LGBTQ+, veterans, eating disorders, and more

### Professional Help
- Psychology Today therapist directory
- Online therapy platforms (BetterHelp, Talkspace)
- Government treatment locators
- Insurance-covered services

### Educational Resources
- NIMH, NAMI, and other authoritative sources
- Self-help tools and coping strategies
- Support groups and communities

## 🔒 Privacy & Security

- **Data Protection**: No text data is stored or logged
- **Session-Based**: Analysis history maintained only during session
- **HTTPS Ready**: SSL/TLS support for production deployment
- **CORS Configuration**: Secure cross-origin resource sharing
- **Input Validation**: Server-side validation of all inputs

## 📊 Analysis Capabilities

### Sentiment Analysis
- Overall sentiment score (-1.0 to 1.0)
- Emotion intensity (0.0 to 1.0)
- Confidence rating for analysis accuracy
- Multi-model consensus scoring

### Risk Assessment
- **Low Risk**: Stable emotional content, continue positive practices
- **Moderate Risk**: Some concerning indicators, consider support
- **High Risk**: Significant distress indicators, immediate action recommended

### Emotional Detection
- Primary emotions: sadness, anxiety, anger, fear, joy, trust
- Mental health keywords: depression, anxiety, suicidal ideation
- Positive indicators: gratitude, hope, support systems

## 🌍 Supporting UN SDGs

### SDG 3: Good Health and Well-being
- Early detection of mental health concerns
- Connection to professional help and resources
- Promotion of mental health awareness and education
- Support for emotional well-being and resilience

### SDG 16: Peace, Justice and Strong Institutions
- Promoting emotional safety in online communities
- Supporting vulnerable populations with crisis resources
- Building trust through transparent, ethical AI practices
- Contributing to social stability through mental health support

## 🛠️ Technical Stack

### Frontend
- **Streamlit**: Interactive web application framework
- **Plotly**: Data visualization and charts
- **Custom CSS**: Responsive design and accessibility

### Backend API
- **Flask**: Lightweight web framework
- **Flask-CORS**: Cross-origin resource sharing
- **Gunicorn**: Production WSGI server

### NLP & Analysis
- **TextBlob**: General sentiment analysis
- **VADER**: Social media optimized sentiment
- **spaCy**: Advanced natural language processing
- **NumPy/Pandas**: Data processing and analysis

### Deployment
- **Docker**: Containerized deployment
- **Docker Compose**: Multi-service orchestration
- **Replit**: Cloud development and hosting

## 📈 Future Enhancements

- Multi-language support (Spanish, French, etc.)
- Advanced transformer models (BERT, RoBERTa)
- Real-time chat integration
- Data visualization dashboard for researchers
- Plugin architecture for extensibility

## ⚠️ Important Disclaimers

**Medical Disclaimer**: WellNet is NOT a substitute for professional mental health care. It provides general sentiment analysis for informational purposes only. Always consult qualified mental health professionals for proper assessment and treatment.

**Crisis Situations**: If you or someone you know is in immediate danger or having thoughts of self-harm, contact emergency services (911) or a crisis hotline (988) immediately.

**Privacy Notice**: While WellNet doesn't store your text data, always be mindful of what personal information you share with any digital tool.

## 📞 Crisis Resources (Always Available)

### United States
- **988 Suicide & Crisis Lifeline**: Call or text 988
- **Crisis Text Line**: Text HOME to 741741
- **Emergency Services**: 911

### International
- **UK**: Samaritans - 116 123
- **Canada**: Crisis Services - 1-833-456-4566
- **Australia**: Lifeline - 13 11 14

## 📄 License

This project is dedicated to supporting mental health and well-being. Please use responsibly and in accordance with ethical AI practices.

## 🤝 Contributing

WellNet is designed to save lives and support mental health. Contributions should prioritize:
- User safety and privacy
- Accuracy of mental health resources
- Accessibility and inclusivity
- Ethical AI practices

---

**Remember: You are not alone. Help is always available. Your mental health matters.**