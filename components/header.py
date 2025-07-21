import streamlit as st

def render_header():
    """Render the main header component for WellNet Kenya."""
    
    # Custom CSS for the header
    st.markdown("""
    <style>
    .wellnet-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 1.5rem 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .header-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .logo {
        font-size: 2.5rem;
        color: white;
    }
    
    .brand-text {
        color: white;
    }
    
    .brand-title {
        font-size: 2rem;
        font-weight: bold;
        margin: 0;
        line-height: 1.2;
    }
    
    .brand-subtitle {
        font-size: 0.9rem;
        opacity: 0.9;
        margin: 0;
        line-height: 1.2;
    }
    
    .header-nav {
        display: flex;
        align-items: center;
        gap: 2rem;
        flex-wrap: wrap;
    }
    
    .nav-item {
        color: white;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: background-color 0.3s;
        font-weight: 500;
    }
    
    .nav-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
        text-decoration: none;
        color: white;
    }
    
    .emergency-button {
        background: #dc3545;
        color: white;
        padding: 0.7rem 1.2rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s;
        border: 2px solid transparent;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .emergency-button:hover {
        background: white;
        color: #dc3545;
        border-color: #dc3545;
        text-decoration: none;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
    }
    
    .kenya-flag {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: white;
        font-size: 0.9rem;
    }
    
    .flag-colors {
        display: flex;
        height: 20px;
        width: 30px;
        border-radius: 3px;
        overflow: hidden;
        margin-right: 0.5rem;
    }
    
    .flag-black { background: #000; flex: 1; }
    .flag-red { background: #ce1126; flex: 1; }
    .flag-green { background: #007a3d; flex: 1; }
    
    @media (max-width: 768px) {
        .header-content {
            flex-direction: column;
            text-align: center;
        }
        
        .brand-title {
            font-size: 1.5rem;
        }
        
        .header-nav {
            justify-content: center;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header HTML
    st.markdown("""
    <div class="wellnet-header">
        <div class="header-content">
            <div class="logo-section">
                <div class="logo">🧠</div>
                <div class="brand-text">
                    <h1 class="brand-title">WellNet Kenya</h1>
                    <p class="brand-subtitle">AI-Powered Mental Health Support | Afya ya Akili</p>
                </div>
            </div>
            
            <div class="header-nav">
                <div class="kenya-flag">
                    <div class="flag-colors">
                        <div class="flag-black"></div>
                        <div class="flag-red"></div>
                        <div class="flag-green"></div>
                    </div>
                    Serving Kenya
                </div>
                <a href="#analysis" class="nav-item">Text Analysis</a>
                <a href="#resources" class="nav-item">Resources</a>
                <a href="#about" class="nav-item">About</a>
                <a href="tel:+254722178177" class="emergency-button">
                    🆘 Crisis Line: +254 722 178 177
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_kenya_banner():
    """Render a banner highlighting Kenya-specific features."""
    
    st.markdown("""
    <style>
    .kenya-banner {
        background: linear-gradient(90deg, #000 0%, #ce1126 50%, #007a3d 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .kenya-banner::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .banner-content {
        position: relative;
        z-index: 1;
    }
    
    .banner-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .banner-subtitle {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .kenya-stats {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: bold;
        display: block;
    }
    
    .stat-label {
        font-size: 0.8rem;
        opacity: 0.8;
    }
    
    @media (max-width: 768px) {
        .kenya-stats {
            gap: 1rem;
        }
        
        .stat-number {
            font-size: 1.2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="kenya-banner">
        <div class="banner-content">
            <div class="banner-title">🇰🇪 Tailored for Kenya | Iliyoandaliwa kwa Kenya</div>
            <div class="banner-subtitle">Supporting mental health across all 47 counties with culturally sensitive resources</div>
            
            <div class="kenya-stats">
                <div class="stat-item">
                    <span class="stat-number">47</span>
                    <span class="stat-label">Counties Served</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">3</span>
                    <span class="stat-label">Languages</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">24/7</span>
                    <span class="stat-label">Crisis Support</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">50+</span>
                    <span class="stat-label">Local Resources</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sdg_banner():
    """Render UN SDG banner for Kenya context."""
    
    st.markdown("""
    <style>
    .sdg-banner {
        background: linear-gradient(135deg, #00689D 0%, #00A99D 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .sdg-content {
        flex: 1;
    }
    
    .sdg-title {
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .sdg-subtitle {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .sdg-goals {
        display: flex;
        gap: 1rem;
        align-items: center;
        flex-wrap: wrap;
    }
    
    .sdg-goal {
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        white-space: nowrap;
    }
    
    @media (max-width: 768px) {
        .sdg-banner {
            flex-direction: column;
            text-align: center;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sdg-banner">
        <div class="sdg-content">
            <div class="sdg-title">🌍 Supporting UN Sustainable Development Goals in Kenya</div>
            <div class="sdg-subtitle">Advancing mental health and social justice through AI-powered technology</div>
        </div>
        <div class="sdg-goals">
            <div class="sdg-goal">🏥 SDG 3: Good Health</div>
            <div class="sdg-goal">⚖️ SDG 16: Peace & Justice</div>
        </div>
    </div>
    """, unsafe_allow_html=True)