# Workforce & Industry Trend Analyzer

![Tableau](https://img.shields.io/badge/Tableau-Visualization-blue) ![Python](https://img.shields.io/badge/Python-ML/NLP-yellow) ![Plotly](https://img.shields.io/badge/Plotly-Dashboards-orange)

A complete analytics portfolio combining **interactive Tableau dashboards** with a **machine learning pipeline** and **browser‑based dashboards** – all centered on workforce trends, automotive sales, and call‑center operations.

---

## 📊 Tableau Dashboards

This repository contains three Tableau dashboards built for HR, automotive, and call‑center data.

### 1. Analyzing Employee Trends
[Analyzing Employee Trends.twbx](Analyzing%20Employee%20Trends/Analyzing%20Employee%20Trends%20Dashboard.png)

- Employee distribution across business units, roles, age, gender, education  
- Satisfaction & engagement trends, attrition by demographic and job factors  
- Compensation analysis and HR KPIs  

![Employee Dashboard](https://github.com/swaapnaa/TABLEAU-PROJECTS/assets/149737403/f7622138-227d-488e-8fa0-576dba6c6372)

### 2. Exploring Trends in the Automotive Industry
[Exploring Trends in the Automotive Industry.twbx](Exploring%20Trends%20in%20the%20Automotive%20Industry/Exploring%20Trends%20in%20the%20Automotive%20Industry.png)

- Used‑car sales trends, pricing by fuel type, transmission, ownership  
- Mileage‑age‑price correlation, dealer and owner‑type volume  
- Future price forecasting  

![Automotive Dashboard](https://github.com/swaapnaa/TABLEAU-PROJECTS/assets/149737403/66894295-1d4a-414f-a8d7-0ce85ed178e8)

### 3. CallCenter Data Analysis
[CallCenter Data Analysis.twbx](CallCenter_Data%20Analysis/Callcenter%20Data%20Analysis.png)

- Call volume, sentiment, complaint‑type breakdowns  
- Response time vs. SLA, channel comparison (phone, email, chat, web)  
- Performance by location  

![CallCenter Dashboard](https://github.com/swaapnaa/TABLEAU-PROJECTS/assets/149737403/bb7c3dfc-9b86-4f96-9e41-b6212e546aa7)

---

## 🧠 Machine Learning Pipeline (`ml_models/`)

Two Python scripts that generate synthetic data, train models, and export scored datasets for BI integration.

| Script | Techniques | Outputs |
|--------|------------|---------|
| `workforce_ml_pipeline.py` | Random Forest (attrition prediction), K‑Means clustering | `workforce_with_ml_results.csv` (attrition prob, predicted flag, segment) |
| `callcenter_sentiment.py` | VADER sentiment analysis (NLP) | `callcenter_sentiment.csv` (vader compound score, sentiment label) |

**Requirements:** `pip install pandas numpy scikit-learn joblib nltk`

Run them once to produce the CSV files used by the dashboards.

---

## 📈 ML‑Powered Interactive Dashboards (`ml_dashboards/`)

Browser‑based dashboards built with **Plotly**, driven directly by the ML outputs. No Tableau required – just open the `.html` files.

- **attrition_dashboard.html** – Attrition probability distribution, risk by department, feature importance, high‑risk employees by segment
- **employee_segments_dashboard.html** – Segment profiles, satisfaction vs. risk, salary comparison, departmental composition
- **callcenter_sentiment_dashboard.html** – Sentiment pie, top words (example), compound score scatter and histogram

To regenerate the dashboards:  
```bash
cd ml_dashboards
python generate_dashboards.py
