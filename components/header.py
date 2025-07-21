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
    
    # Use columns to display statistics instead of complex HTML
    st.markdown("### 🇰🇪 Tailored for Kenya | Iliyoandaliwa kwa Kenya")
    st.info("Supporting mental health across all 47 counties with culturally sensitive resources")
    
    # Display stats in columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Counties Served", "47")
    with col2:
        st.metric("Languages", "3")  
    with col3:
        st.metric("Crisis Support", "24/7")
    with col4:
        st.metric("Local Resources", "50+")

def render_sdg_banner():
    """Render UN SDG banner for Kenya context."""
    
    st.success("🌍 **Supporting UN Sustainable Development Goals in Kenya** - Advancing mental health and social justice through AI-powered technology")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🏥 **SDG 3:** Good Health and Well-being")
    with col2:
        st.markdown("⚖️ **SDG 16:** Peace, Justice and Strong Institutions")