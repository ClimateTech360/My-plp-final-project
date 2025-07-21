import streamlit as st

def render_header():
    """Render the main header component for WellNet Kenya."""
    
    # Create columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Main title and subtitle
        st.markdown("# 🧠 WellNet Kenya")
        st.markdown("**AI-Powered Mental Health Support | Afya ya Akili**")
    
    with col2:
        # Kenya flag and crisis line
        st.markdown("### 🇰🇪 Serving Kenya")
        st.markdown("""
        <a href="tel:+254722178177" style="
            background: #dc3545; 
            color: white; 
            padding: 10px 15px; 
            border-radius: 25px; 
            text-decoration: none; 
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        ">
            🆘 Crisis Line: +254 722 178 177
        </a>
        """, unsafe_allow_html=True)

def render_kenya_banner():
    """Render a banner highlighting Kenya-specific features."""
    
    st.markdown("""
    <div style="
        background: linear-gradient(90deg, #000 0%, #ce1126 50%, #007a3d 100%); 
        color: white; 
        padding: 20px; 
        border-radius: 10px; 
        margin: 20px 0; 
        text-align: center;
    ">
        <h3 style="margin: 0 0 10px 0;">🇰🇪 Tailored for Kenya | Iliyoandaliwa kwa Kenya</h3>
        <p style="margin: 0; opacity: 0.9;">Supporting mental health across all 47 counties with culturally sensitive resources</p>
        
        <div style="
            display: flex; 
            justify-content: center; 
            gap: 30px; 
            margin-top: 15px; 
            flex-wrap: wrap;
        ">
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">47</div>
                <div style="font-size: 0.8em; opacity: 0.8;">Counties Served</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">3</div>
                <div style="font-size: 0.8em; opacity: 0.8;">Languages</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">24/7</div>
                <div style="font-size: 0.8em; opacity: 0.8;">Crisis Support</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">50+</div>
                <div style="font-size: 0.8em; opacity: 0.8;">Local Resources</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sdg_banner():
    """Render UN SDG banner for Kenya context."""
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #00689D 0%, #00A99D 100%); 
        color: white; 
        padding: 15px 20px; 
        border-radius: 8px; 
        margin-bottom: 20px;
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        flex-wrap: wrap; 
        gap: 15px;
    ">
        <div>
            <h4 style="margin: 0 0 5px 0;">🌍 Supporting UN Sustainable Development Goals in Kenya</h4>
            <p style="margin: 0; font-size: 0.9em; opacity: 0.9;">Advancing mental health and social justice through AI-powered technology</p>
        </div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <span style="
                background: rgba(255, 255, 255, 0.2); 
                padding: 5px 15px; 
                border-radius: 20px; 
                font-size: 0.8em;
                white-space: nowrap;
            ">🏥 SDG 3: Good Health</span>
            <span style="
                background: rgba(255, 255, 255, 0.2); 
                padding: 5px 15px; 
                border-radius: 20px; 
                font-size: 0.8em;
                white-space: nowrap;
            ">⚖️ SDG 16: Peace & Justice</span>
        </div>
    </div>
    """, unsafe_allow_html=True)