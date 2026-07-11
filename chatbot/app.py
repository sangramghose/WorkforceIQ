"""
Workforce & Call-Center Chatbot
Ask questions about attrition, employee segments, and sentiment – powered by your data.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(base_dir)
    workforce = pd.read_csv(os.path.join(root_dir, 'workforce_with_ml_results.csv'))
    sentiment = pd.read_csv(os.path.join(root_dir, 'callcenter_sentiment.csv'))
    return workforce, sentiment

workforce, sentiment = load_data()

# ---------------- Helper Functions ----------------
def high_risk_count(department=None):
    df = workforce[workforce['attrition_prob'] > 0.7]
    if department:
        df = df[df['department'] == department]
    return len(df)

def avg_satisfaction_by_segment(segment=None):
    if segment is not None:
        return workforce[workforce['segment'] == segment]['satisfaction_score'].mean()
    return workforce['satisfaction_score'].mean()

def sentiment_distribution():
    return sentiment['vader_sentiment'].value_counts().to_dict()

def top_department_attrition():
    return workforce.groupby('department')['attrition_prob'].mean().sort_values(ascending=False).head(5)

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Workforce AI Chatbot", page_icon="🤖")
st.title("🤖 Workforce & Sentiment Chatbot")
st.caption("Ask me about attrition, employee segments, or call‑center sentiment.")

user_input = st.text_input("Your question:")

if user_input:
    user_input_lower = user_input.lower()
    response = ""
    
    # Attrition risk queries
    if "high risk" in user_input_lower or "attrition risk" in user_input_lower:
        if "sales" in user_input_lower:
            count = high_risk_count('Sales')
            response = f"There are {count} employees in **Sales** with high attrition risk (probability > 0.7)."
        elif "r&d" in user_input_lower:
            count = high_risk_count('R&D')
            response = f"There are {count} employees in **R&D** with high attrition risk."
        elif "hr" in user_input_lower:
            count = high_risk_count('HR')
            response = f"There are {count} employees in **HR** with high attrition risk."
        else:
            count = high_risk_count()
            response = f"There are {count} employees across all departments with high attrition risk (probability > 0.7)."
    
    # Satisfaction / segments
    elif "satisfaction" in user_input_lower and "segment" in user_input_lower:
        for seg in [0,1,2,3]:
            if f"segment {seg}" in user_input_lower:
                avg = avg_satisfaction_by_segment(seg)
                response = f"Average satisfaction score for Segment {seg} is **{avg:.2f}**."
                break
        else:
            response = "Please specify a segment number (0-3)."
    
    elif "sentiment" in user_input_lower:
        dist = sentiment_distribution()
        response = f"Sentiment distribution:\n- Positive: {dist.get('Positive',0)}\n- Negative: {dist.get('Negative',0)}\n- Neutral: {dist.get('Neutral',0)}"
        
        # Show pie chart
        fig, ax = plt.subplots()
        ax.pie(dist.values(), labels=dist.keys(), autopct='%1.1f%%')
        ax.set_title("Call-Center Sentiment")
        st.pyplot(fig)
    
    elif "department" in user_input_lower and "attrition" in user_input_lower:
        top_dept = top_department_attrition()
        response = "**Average attrition risk by department:**\n" + top_dept.to_string()
    
    else:
        response = "I didn't understand that. Try asking about 'high risk employees in Sales', 'segment 2 satisfaction', or 'sentiment distribution'."
    
    st.markdown(response)
