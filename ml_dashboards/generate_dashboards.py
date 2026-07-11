"""
Generate ML‑powered Plotly dashboards from pipeline output CSVs.
Saves HTML files that can be opened directly in a browser.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Ensure we're saving inside the ml_dashboards folder
os.makedirs('ml_dashboards', exist_ok=True)

# Load CSVs (adjust paths if needed)
try:
    workforce = pd.read_csv('workforce_with_ml_results.csv')
    sentiment = pd.read_csv('callcenter_sentiment.csv')
except FileNotFoundError:
    workforce = pd.read_csv('../workforce_with_ml_results.csv')
    sentiment = pd.read_csv('../callcenter_sentiment.csv')

# ------------------------------------------------------------
# Dashboard 1: Attrition Risk
# ------------------------------------------------------------
fig1 = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Attrition Probability Distribution", "Risk by Department",
                    "Top Features", "High‑Risk Count by Segment"),
    specs=[[{"type": "histogram"}, {"type": "box"}],
           [{"type": "table"}, {"type": "bar"}]]
)

fig1.add_trace(go.Histogram(x=workforce['attrition_prob'], nbinsx=30, name='Probability'), row=1, col=1)
fig1.add_trace(go.Box(x=workforce['department'], y=workforce['attrition_prob'], name='Dept'), row=1, col=2)

# Hardcoded feature importances (replace with your actual ones if needed)
importances = pd.DataFrame({
    'Feature': ['satisfaction_score', 'years_at_company', 'overtime_Yes', 'commute_distance_Very Far'],
    'Importance': [0.32, 0.21, 0.18, 0.12]
})
fig1.add_trace(go.Table(header=dict(values=importances.columns),
                        cells=dict(values=[importances.Feature, importances.Importance.round(3)])),
               row=2, col=1)

high_risk = workforce[workforce['attrition_prob'] > 0.7]
seg_counts = high_risk['segment'].value_counts().reset_index()
seg_counts.columns = ['segment', 'count']
fig1.add_trace(go.Bar(x=seg_counts['segment'], y=seg_counts['count'], marker_color='crimson'), row=2, col=2)

fig1.update_layout(height=800, title_text="Attrition Risk Dashboard")
fig1.write_html('ml_dashboards/attrition_dashboard.html')
print("Saved attrition_dashboard.html")

# ------------------------------------------------------------
# Dashboard 2: Employee Segments
# ------------------------------------------------------------
seg_profile = workforce.groupby('segment')[['satisfaction_score', 'years_at_company', 
                                            'monthly_salary', 'attrition_prob']].mean().reset_index()
fig2 = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Segment Size", "Avg Satisfaction & Attrition Risk",
                    "Avg Salary", "Department Composition"),
    specs=[[{"type": "pie"}, {"type": "bar"}],
           [{"type": "bar"}, {"type": "bar"}]]
)

seg_sizes = workforce['segment'].value_counts().reset_index()
seg_sizes.columns = ['segment', 'count']
fig2.add_trace(go.Pie(labels=seg_sizes['segment'], values=seg_sizes['count'], hole=0.3), row=1, col=1)

fig2.add_trace(go.Bar(x=seg_profile['segment'], y=seg_profile['satisfaction_score'], name='Satisfaction',
                       marker_color='steelblue'), row=1, col=2)
fig2.add_trace(go.Bar(x=seg_profile['segment'], y=seg_profile['attrition_prob'], name='Attrition Prob',
                       marker_color='salmon'), row=1, col=2)

fig2.add_trace(go.Bar(x=seg_profile['segment'], y=seg_profile['monthly_salary'], marker_color='green'), row=2, col=1)

dept_seg = workforce.groupby(['segment', 'department']).size().unstack().fillna(0)
for dept in dept_seg.columns:
    fig2.add_trace(go.Bar(name=dept, x=dept_seg.index, y=dept_seg[dept]), row=2, col=2)
fig2.update_layout(barmode='stack', height=800, title_text="Employee Segmentation Dashboard")
fig2.write_html('ml_dashboards/employee_segments_dashboard.html')
print("Saved employee_segments_dashboard.html")

# ------------------------------------------------------------
# Dashboard 3: Call Center Sentiment
# ------------------------------------------------------------
fig3 = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Sentiment Distribution", "Top Words (Example)",
                    "Sample Compound Scores", "Compound Score Distribution"),
    specs=[[{"type": "pie"}, {"type": "bar"}],
           [{"type": "scatter"}, {"type": "histogram"}]]
)

sent_counts = sentiment['vader_sentiment'].value_counts().reset_index()
sent_counts.columns = ['sentiment', 'count']
fig3.add_trace(go.Pie(labels=sent_counts['sentiment'], values=sent_counts['count'], hole=0.3), row=1, col=1)

# Dummy top words – replace with your actual NLP results if desired
fig3.add_trace(go.Bar(x=['problem', 'service', 'help', 'waiting', 'refund'],
                       y=[450, 320, 280, 200, 180], marker_color='darkorange'), row=1, col=2)

sample = sentiment.head(500)
fig3.add_trace(go.Scatter(x=sample['call_id'], y=sample['vader_compound'],
                          mode='markers', marker=dict(color=sample['vader_compound'], colorscale='RdYlGn')),
               row=2, col=1)

fig3.add_trace(go.Histogram(x=sentiment['vader_compound'], nbinsx=50, marker_color='purple'), row=2, col=2)

fig3.update_layout(height=800, title_text="Call Center Sentiment Dashboard")
fig3.write_html('ml_dashboards/callcenter_sentiment_dashboard.html')
print("Saved callcenter_sentiment_dashboard.html")
