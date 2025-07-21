# WellNet - Mental Health Sentiment Analysis

## Overview

WellNet is a Streamlit-based web application that analyzes text for emotional distress indicators and provides mental health resources. The application uses natural language processing to identify potential mental health concerns in user-provided text and connects users with appropriate support resources. This is an educational and awareness tool, not a replacement for professional mental health care.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web framework for rapid prototyping and deployment
- **Visualization**: Plotly Express and Plotly Graph Objects for interactive charts and data visualization
- **UI Components**: Custom HTML/CSS styling with Streamlit's native components
- **State Management**: Streamlit session state for maintaining analysis history across user interactions

### Backend Architecture
- **Core Logic**: Python-based modular architecture with separate modules for different functionalities
- **NLP Processing**: Multi-library approach combining TextBlob, VADER sentiment analysis, and spaCy for comprehensive text analysis
- **Data Processing**: Pandas and NumPy for data manipulation and statistical analysis

## Key Components

### 1. Sentiment Analysis Engine (`sentiment_analyzer.py`)
- **Primary Function**: Analyzes text for mental health indicators and sentiment
- **NLP Libraries**: 
  - VADER Sentiment for social media text analysis
  - TextBlob for general sentiment analysis
  - spaCy for advanced natural language processing (with fallback handling)
- **Keyword Detection**: Categorized mental health keywords including depression, anxiety, suicidal ideation, self-harm, isolation, and positive indicators
- **Preprocessing**: Text cleaning, contraction handling, and normalization

### 2. Mental Health Resources (`mental_health_resources.py`)
- **Resource Categories**: Professional services, educational resources, and support platforms
- **Content**: Curated list of therapy platforms, government resources, and mental health organizations
- **Structure**: Organized dictionary format for easy categorization and display

### 3. Crisis Resources (`crisis_resources.py`)
- **Emergency Resources**: Immediate crisis intervention contacts and hotlines
- **Coverage**: National and international crisis support services
- **Specialized Support**: LGBTQ+ youth resources, transgender-specific support, and general crisis lines

### 4. Main Application (`app.py`)
- **User Interface**: Streamlit-based web interface with responsive design
- **Session Management**: Maintains analysis history and user state
- **Resource Integration**: Connects sentiment analysis results with appropriate resources
- **Safety Features**: Prominent disclaimers and crisis resource access

## Data Flow

1. **User Input**: Text submission through Streamlit interface
2. **Preprocessing**: Text cleaning and normalization
3. **Analysis**: Multi-layered sentiment analysis using VADER, TextBlob, and keyword matching
4. **Risk Assessment**: Categorization of mental health indicators and severity
5. **Resource Matching**: Dynamic resource recommendations based on analysis results
6. **Visualization**: Interactive charts and graphs displaying sentiment metrics
7. **History Tracking**: Session-based storage of analysis results

## External Dependencies

### Core Libraries
- **Streamlit**: Web application framework
- **Plotly**: Data visualization and interactive charts
- **Pandas/NumPy**: Data manipulation and numerical operations
- **TextBlob**: Natural language processing and sentiment analysis
- **VADER Sentiment**: Social media optimized sentiment analysis
- **spaCy**: Advanced NLP with graceful fallback handling

### Optional Dependencies
- **spaCy English Model** (`en_core_web_sm`): Enhanced NLP capabilities with error handling for missing models

## Deployment Strategy

### Development Environment
- **Platform**: Replit-compatible Python environment
- **Requirements**: All dependencies installable via pip
- **Graceful Degradation**: Application functions even if optional dependencies (spaCy model) are unavailable

### Production Considerations
- **Scalability**: Streamlit caching for sentiment analyzer initialization
- **Performance**: Efficient text processing with minimal computational overhead
- **Privacy**: No persistent data storage, session-based analysis history only
- **Safety**: Clear disclaimers and immediate access to crisis resources

### Key Architectural Decisions

1. **Multi-Library NLP Approach**: Uses multiple sentiment analysis tools for comprehensive coverage, addressing the limitation that no single NLP library is perfect for all text types
2. **Modular Resource Management**: Separates crisis and general mental health resources for better organization and easier maintenance
3. **Graceful Degradation**: Handles missing optional dependencies to ensure application stability across different deployment environments
4. **Session-Based Storage**: Avoids persistent data storage for privacy while maintaining user experience through session state
5. **Safety-First Design**: Prioritizes user safety with prominent crisis resources and clear disclaimers about the tool's limitations