import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

from sentiment_analyzer import SentimentAnalyzer
from mental_health_resources import get_mental_health_resources
from crisis_resources import get_crisis_resources
from kenya_mental_health_resources import (
    get_kenya_mental_health_resources, 
    get_kenya_crisis_resources, 
    get_kenya_safety_planning_resources
)
from components.header import render_header, render_kenya_banner, render_sdg_banner

# Page configuration
st.set_page_config(
    page_title="WellNet Kenya - Mental Health Sentiment Analysis",
    page_icon="🇰🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize sentiment analyzer
@st.cache_resource
def load_analyzer():
    return SentimentAnalyzer()

analyzer = load_analyzer()

# Initialize session state
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

# Render header components
render_header()
render_kenya_banner()
render_sdg_banner()

# Important disclaimers
with st.expander("⚠️ Important Disclaimers and Privacy Information", expanded=False):
    st.warning("""
    **Important:** This tool is NOT a substitute for professional mental health care. 
    If you are experiencing a mental health crisis, please contact emergency services or a crisis hotline immediately.
    """)
    
    st.info("""
    **Privacy Notice:**
    - No text data is stored or saved by this application
    - All analysis is performed locally and temporarily
    - Your privacy and confidentiality are our top priorities
    - This tool is for informational and educational purposes only
    """)
    
    st.error("""
    **Limitations:**
    - This tool provides general sentiment analysis, not clinical diagnosis
    - Results should not be used for medical decision-making
    - Always consult qualified mental health professionals for proper assessment
    """)

# Sidebar for crisis resources
with st.sidebar:
    st.header("🆘 Crisis Support - Kenya")
    crisis_resources = get_kenya_crisis_resources()
    
    st.markdown("### Immediate Help (Msaada wa Haraka)")
    for resource in crisis_resources['immediate']:
        st.markdown(f"**{resource['name']}**")
        st.markdown(f"📞 {resource['phone']}")
        if resource.get('text'):
            st.markdown(f"📱 {resource['text']}")
        st.markdown(f"🌐 [{resource['website']}]({resource['website']})")
        st.markdown(f"*{resource['description']}*")
        st.markdown("---")
    
    st.markdown("### Regional Centers")
    for resource in crisis_resources['regional']:
        st.markdown(f"**{resource['name']}** ({resource['region']})")
        st.markdown(f"📞 {resource['phone']}")
        if resource.get('address'):
            st.markdown(f"📍 {resource['address']}")
        st.markdown("---")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Text Analysis")
    
    # Input method selection
    input_method = st.radio(
        "Choose input method:",
        ["Manual Text Input", "Sample Social Media Posts"],
        horizontal=True
    )
    
    if input_method == "Manual Text Input":
        text_input = st.text_area(
            "Enter text to analyze:",
            height=150,
            placeholder="Share your thoughts, feelings, or any text you'd like to analyze for emotional indicators..."
        )
    else:
        # Sample posts for demonstration - Kenya context
        sample_posts = [
            "I've been feeling really overwhelmed with life in Nairobi. Everything seems too expensive and stressful.",
            "Had a wonderful day at Uhuru Park with my family! Feeling blessed and grateful.",
            "Can't sleep again thinking about my job situation. I feel so alone in this big city.",
            "Just got a new job opportunity! Hard work and prayer really pay off.",
            "I don't see the point in anything anymore. Life feels hopeless since I moved to town.",
            "Attending prayers at church really helped me today. Feeling more at peace.",
            "Kuna stress sana with this economy. I don't know how to cope anymore.",
            "Family time in shags always makes me feel better. Rural life has its peace."
        ]
        
        selected_sample = st.selectbox(
            "Select a sample post to analyze:",
            [""] + sample_posts
        )
        text_input = selected_sample
    
    # Analysis button
    if st.button("🔍 Analyze Text", type="primary", disabled=not text_input):
        if text_input:
            with st.spinner("Analyzing text for emotional indicators..."):
                # Perform sentiment analysis
                analysis_result = analyzer.analyze_text(text_input)
                
                # Store in session state
                st.session_state.analysis_history.append({
                    'timestamp': datetime.now(),
                    'text': text_input[:100] + "..." if len(text_input) > 100 else text_input,
                    'result': analysis_result
                })
                
                # Display results
                st.success("Analysis complete!")
                
                # Risk level indicator
                risk_level = analysis_result['risk_level']
                risk_colors = {
                    'Low': '#4CAF50',
                    'Moderate': '#FF9800', 
                    'High': '#F44336'
                }
                
                st.markdown(f"""
                <div style="background-color: {risk_colors[risk_level]}; color: white; padding: 15px; border-radius: 10px; text-align: center; margin: 20px 0;">
                    <h3>Risk Level: {risk_level}</h3>
                    <p>{analysis_result['risk_description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Detailed sentiment scores
                st.subheader("📊 Sentiment Analysis Results")
                
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric(
                        "Overall Sentiment",
                        f"{analysis_result['overall_sentiment']:.2f}",
                        help="Range: -1.0 (very negative) to 1.0 (very positive)"
                    )
                
                with col_b:
                    st.metric(
                        "Emotional Intensity",
                        f"{analysis_result['emotion_intensity']:.2f}",
                        help="Range: 0.0 (neutral) to 1.0 (very intense)"
                    )
                
                with col_c:
                    st.metric(
                        "Confidence Score",
                        f"{analysis_result['confidence']:.2f}",
                        help="Model confidence in the analysis"
                    )
                
                # Emotion breakdown
                st.subheader("🎭 Emotional Indicators")
                emotions_df = pd.DataFrame(
                    list(analysis_result['emotions'].items()),
                    columns=['Emotion', 'Score']
                )
                
                fig_emotions = px.bar(
                    emotions_df,
                    x='Emotion',
                    y='Score',
                    title="Detected Emotional Indicators",
                    color='Score',
                    color_continuous_scale='RdYlGn_r'
                )
                fig_emotions.update_layout(showlegend=False)
                st.plotly_chart(fig_emotions, use_container_width=True)
                
                # Mental health keywords
                if analysis_result['mental_health_keywords']:
                    st.subheader("🔍 Mental Health Indicators")
                    keywords_text = ", ".join(analysis_result['mental_health_keywords'])
                    st.info(f"Detected keywords: {keywords_text}")
                
                # Recommendations based on risk level
                st.subheader("💡 Recommendations")
                if risk_level == "High":
                    st.error("""
                    **Immediate Action Recommended:**
                    - Consider reaching out to a mental health professional
                    - Contact a crisis helpline if you're having thoughts of self-harm
                    - Reach out to trusted friends, family, or support networks
                    - Practice grounding techniques and self-care
                    """)
                elif risk_level == "Moderate":
                    st.warning("""
                    **Consider Support:**
                    - Talk to someone you trust about how you're feeling
                    - Consider scheduling an appointment with a counselor
                    - Practice stress management techniques
                    - Monitor your emotional well-being
                    """)
                else:
                    st.success("""
                    **Continue Positive Practices:**
                    - Maintain healthy coping strategies
                    - Stay connected with your support network
                    - Continue activities that promote well-being
                    - Be mindful of any changes in your emotional state
                    """)

with col2:
    st.header("📈 Analysis History")
    
    if st.session_state.analysis_history:
        # Clear history button
        if st.button("🗑️ Clear History"):
            st.session_state.analysis_history = []
            st.rerun()
        
        # Display recent analyses
        for i, analysis in enumerate(reversed(st.session_state.analysis_history[-10:])):
            with st.expander(f"Analysis {len(st.session_state.analysis_history) - i}"):
                st.write(f"**Time:** {analysis['timestamp'].strftime('%Y-%m-%d %H:%M')}")
                st.write(f"**Text:** {analysis['text']}")
                st.write(f"**Risk Level:** {analysis['result']['risk_level']}")
                st.write(f"**Sentiment:** {analysis['result']['overall_sentiment']:.2f}")
        
        # Trend visualization
        if len(st.session_state.analysis_history) > 1:
            st.subheader("📊 Sentiment Trends")
            
            # Prepare trend data
            timestamps = [a['timestamp'] for a in st.session_state.analysis_history]
            sentiments = [a['result']['overall_sentiment'] for a in st.session_state.analysis_history]
            risk_levels = [a['result']['risk_level'] for a in st.session_state.analysis_history]
            
            # Create trend chart
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Scatter(
                x=timestamps,
                y=sentiments,
                mode='lines+markers',
                name='Sentiment Score',
                line=dict(color='#2E86AB', width=2)
            ))
            
            fig_trend.update_layout(
                title="Sentiment Over Time",
                xaxis_title="Time",
                yaxis_title="Sentiment Score",
                yaxis=dict(range=[-1, 1]),
                height=300
            )
            
            st.plotly_chart(fig_trend, use_container_width=True)
            
            # Risk level distribution
            risk_counts = pd.Series(risk_levels).value_counts()
            fig_risk = px.pie(
                values=risk_counts.values,
                names=risk_counts.index,
                title="Risk Level Distribution",
                color_discrete_map={
                    'Low': '#4CAF50',
                    'Moderate': '#FF9800',
                    'High': '#F44336'
                }
            )
            fig_risk.update_layout(height=300)
            st.plotly_chart(fig_risk, use_container_width=True)
    
    else:
        st.info("No analysis history yet. Start by analyzing some text!")

# Mental Health Resources Section - Kenya Focused
st.header("🌟 Mental Health Resources in Kenya")

resources = get_kenya_mental_health_resources()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏥 Professional Help", 
    "📚 Educational", 
    "🧘 Self-Care", 
    "👥 Support Groups",
    "🏘️ Community Resources"
])

with tab1:
    st.subheader("Professional Mental Health Services in Kenya")
    st.info("Find qualified mental health professionals across Kenya's 47 counties")
    for resource in resources['professional']:
        with st.expander(resource['title']):
            st.write(resource['description'])
            if resource.get('website'):
                st.markdown(f"🌐 [Visit Website]({resource['website']})")
            if resource.get('phone'):
                st.markdown(f"📞 {resource['phone']}")

with tab2:
    st.subheader("Educational Resources - Kenya")
    st.info("Learn about mental health from trusted Kenyan and African sources")
    for resource in resources['educational']:
        with st.expander(resource['title']):
            st.write(resource['description'])
            if resource.get('website'):
                st.markdown(f"🌐 [Learn More]({resource['website']})")

with tab3:
    st.subheader("Self-Care and Healing - African Approach")
    st.info("Culturally appropriate self-care practices for Kenyans")
    for resource in resources['self_care']:
        with st.expander(resource['title']):
            st.write(resource['description'])
            if resource.get('website'):
                st.markdown(f"🌐 [Explore]({resource['website']})")

with tab4:
    st.subheader("Support Groups and Communities")
    st.info("Connect with others facing similar challenges across Kenya")
    for resource in resources['support_groups']:
        with st.expander(resource['title']):
            st.write(resource['description'])
            if resource.get('website'):
                st.markdown(f"🌐 [Join Community]({resource['website']})")
            if resource.get('phone'):
                st.markdown(f"📞 {resource['phone']}")

with tab5:
    st.subheader("Community and Cultural Resources")
    st.info("Local community support including faith-based and traditional healing")
    for resource in resources['community_resources']:
        with st.expander(resource['title']):
            st.write(resource['description'])
            if resource.get('website'):
                st.markdown(f"🌐 [Learn More]({resource['website']})")
            if resource.get('phone'):
                st.markdown(f"📞 {resource['phone']}")

# Footer - Kenya Context
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px; background: linear-gradient(90deg, #000 0%, #ce1126 50%, #007a3d 100%); color: white; border-radius: 10px;">
    <p><strong>🇰🇪 WellNet Kenya - Mental Health Sentiment Analysis Tool</strong></p>
    <p><em>Chombo cha Uchambuzi wa Hali ya Afya ya Akili</em></p>
    <p>Supporting SDG 3 (Good Health and Well-being) and SDG 16 (Peace, Justice and Strong Institutions) in Kenya</p>
    <p><strong>Kumbuka: Haupo peke yako. Msaada unapatikana kila wakati.</strong></p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        🏥 Ministry of Health Kenya | 🤝 Kenya Mental Health Association | 
        📞 Crisis Line: +254 722 178 177
    </p>
</div>
""", unsafe_allow_html=True)
