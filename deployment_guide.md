# WellNet Deployment Guide

This guide covers various deployment options for the WellNet Mental Health Sentiment Analysis system, from development to production environments.

## Quick Deployment Options

### 1. Replit (Recommended for Development)
Your WellNet system is already configured and running on Replit with:
- Streamlit Frontend: Port 5000
- Flask API: Port 3000
- Automatic dependency management
- Built-in SSL and domain management

### 2. Local Development
```bash
# Install dependencies
pip install uv
uv sync

# Download spaCy model
python -m spacy download en_core_web_sm

# Start services
streamlit run app.py --server.port 5000 &
python api_server.py &
```

### 3. Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or individual services
docker build -f Dockerfile.streamlit -t wellnet-frontend .
docker build -f Dockerfile.flask -t wellnet-api .

docker run -p 5000:5000 wellnet-frontend
docker run -p 3000:3000 wellnet-api
```

## Production Deployment

### Cloud Platforms

#### Heroku Deployment
```bash
# Create Heroku apps
heroku create wellnet-frontend
heroku create wellnet-api

# Configure buildpacks
heroku buildpacks:set heroku/python -a wellnet-frontend
heroku buildpacks:set heroku/python -a wellnet-api

# Set environment variables
heroku config:set FLASK_ENV=production -a wellnet-api

# Deploy
git push heroku main
```

#### AWS Deployment
```bash
# Using AWS ECS with Fargate
aws ecs create-cluster --cluster-name wellnet-cluster

# Build and push to ECR
aws ecr create-repository --repository-name wellnet-frontend
aws ecr create-repository --repository-name wellnet-api

# Tag and push images
docker tag wellnet-frontend:latest <account>.dkr.ecr.<region>.amazonaws.com/wellnet-frontend:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/wellnet-frontend:latest
```

#### Google Cloud Platform
```bash
# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Build and deploy to Cloud Run
gcloud builds submit --tag gcr.io/PROJECT-ID/wellnet-frontend
gcloud run deploy --image gcr.io/PROJECT-ID/wellnet-frontend --platform managed
```

#### Azure Deployment
```bash
# Create resource group and container instances
az group create --name wellnet-rg --location eastus
az container create --resource-group wellnet-rg --name wellnet-frontend \
  --image wellnet-frontend --ports 5000 --cpu 1 --memory 1.5
```

### Production Configuration

#### Environment Variables
```bash
# Flask API (.env file)
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
CORS_ORIGINS=https://your-frontend-domain.com
LOG_LEVEL=INFO

# Streamlit (.streamlit/secrets.toml)
[server]
headless = true
address = "0.0.0.0"
port = 5000
enableCORS = false
enableXsrfProtection = true
```

#### Production Docker Compose
```yaml
version: '3.8'
services:
  wellnet-frontend:
    build:
      context: .
      dockerfile: Dockerfile.streamlit
    ports:
      - "80:5000"
    environment:
      - PYTHONPATH=/app
    restart: unless-stopped
    depends_on:
      - wellnet-api

  wellnet-api:
    build:
      context: .
      dockerfile: Dockerfile.flask
    ports:
      - "3000:3000"
    environment:
      - FLASK_ENV=production
      - PYTHONPATH=/app
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - wellnet-frontend
      - wellnet-api
```

#### Nginx Configuration
```nginx
events {
    worker_connections 1024;
}

http {
    upstream frontend {
        server wellnet-frontend:5000;
    }
    
    upstream api {
        server wellnet-api:3000;
    }

    server {
        listen 80;
        server_name your-domain.com;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name your-domain.com;

        ssl_certificate /etc/nginx/ssl/fullchain.pem;
        ssl_certificate_key /etc/nginx/ssl/privkey.pem;

        location / {
            proxy_pass http://frontend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /api/ {
            proxy_pass http://api;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

## Kubernetes Deployment

### Kubernetes Manifests

#### Frontend Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wellnet-frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: wellnet-frontend
  template:
    metadata:
      labels:
        app: wellnet-frontend
    spec:
      containers:
      - name: frontend
        image: wellnet-frontend:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
---
apiVersion: v1
kind: Service
metadata:
  name: wellnet-frontend-service
spec:
  selector:
    app: wellnet-frontend
  ports:
  - port: 80
    targetPort: 5000
  type: LoadBalancer
```

#### API Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wellnet-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: wellnet-api
  template:
    metadata:
      labels:
        app: wellnet-api
    spec:
      containers:
      - name: api
        image: wellnet-api:latest
        ports:
        - containerPort: 3000
        env:
        - name: FLASK_ENV
          value: "production"
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
---
apiVersion: v1
kind: Service
metadata:
  name: wellnet-api-service
spec:
  selector:
    app: wellnet-api
  ports:
  - port: 3000
    targetPort: 3000
  type: ClusterIP
```

## Performance Optimization

### Frontend Optimization
```python
# Streamlit caching configuration
@st.cache_resource
def load_analyzer():
    return SentimentAnalyzer()

@st.cache_data(ttl=3600)
def get_resources():
    return get_mental_health_resources()
```

### API Optimization
```python
# Flask API with caching
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route('/api/resources/crisis')
@cache.cached(timeout=3600)
def get_crisis_help():
    return jsonify(get_crisis_resources())
```

### Database Integration (Optional)
```python
# For analytics and monitoring (not user data)
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class AnalyticsEvent(Base):
    __tablename__ = 'analytics_events'
    
    id = Column(Integer, primary_key=True)
    event_type = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    risk_level = Column(String(20))
    sentiment_score = Column(Float)
```

## Monitoring and Logging

### Application Monitoring
```python
# Health check endpoints
@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

@app.route('/metrics')
def metrics():
    return jsonify({
        'requests_total': request_counter,
        'analyses_performed': analysis_counter,
        'high_risk_detections': high_risk_counter
    })
```

### Logging Configuration
```python
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
    handlers=[
        RotatingFileHandler('wellnet.log', maxBytes=10240000, backupCount=10),
        logging.StreamHandler()
    ]
)
```

## Security Configuration

### Production Security
```python
# Flask security headers
@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

# Rate limiting
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1000 per day", "100 per hour"]
)

@app.route('/api/analyze', methods=['POST'])
@limiter.limit("50 per minute")
def analyze_text():
    # Analysis logic here
    pass
```

## Scaling Considerations

### Horizontal Scaling
- Use load balancers (Nginx, HAProxy)
- Implement session affinity if needed
- Scale API independently from frontend
- Consider CDN for static assets

### Vertical Scaling
- Monitor CPU and memory usage
- Optimize spaCy model loading
- Use async processing for batch operations
- Implement caching strategies

### Cost Optimization
- Use spot instances for development
- Implement auto-scaling based on usage
- Monitor resource utilization
- Consider serverless options for API

## Troubleshooting

### Common Issues
1. **Port conflicts**: Ensure ports 3000 and 5000 are available
2. **spaCy model missing**: Run `python -m spacy download en_core_web_sm`
3. **Memory issues**: Increase container memory limits
4. **CORS errors**: Configure proper CORS headers

### Debug Commands
```bash
# Check service status
curl http://localhost:3000/api/health
curl http://localhost:5000

# View logs
docker logs wellnet-api
docker logs wellnet-frontend

# Test API functionality
curl -X POST http://localhost:3000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "test"}'
```

## Backup and Recovery

### Configuration Backup
- Store environment configurations in version control
- Backup SSL certificates and keys
- Document deployment procedures
- Maintain rollback procedures

### Disaster Recovery
- Implement health checks and auto-restart
- Use multiple availability zones
- Maintain service documentation
- Plan for database recovery (if implemented)

---

**Note**: Always prioritize user privacy and data protection in production deployments. Follow GDPR, HIPAA, and other relevant privacy regulations.