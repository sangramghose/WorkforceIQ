# Workforce & Industry Trend Analyzer

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-4B8BBE)
![Tableau](https://img.shields.io/badge/Tableau-Dashboards-E97627?logo=tableau&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3F4F75?logo=plotly&logoColor=white)
![Power Automate](https://img.shields.io/badge/Power%20Automate-Workflow-0066FF?logo=microsoftpowerautomate&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An end-to-end analytics pipeline that turns raw workforce, automotive, and call-center data into predictive insights and dashboards people actually use. It started as an attempt to stop building HR reports by hand every week — it grew into a small ecosystem of ML models, SQL, and dashboards that talk to each other.

---

## What this project actually does

Three real business problems, one pipeline:

- **Will this employee leave?** A Random Forest model trained on 50,000 employee records flags attrition risk before it becomes a resignation letter.
- **Who are our employees, really?** K-Means clustering groups the workforce into behavioral segments — including one small, high-risk, low-satisfaction cohort that HR wouldn't have found by eyeballing a spreadsheet.
- **Are customers actually happy on our calls?** VADER sentiment analysis runs over thousands of call transcripts and turns "we think service is fine" into a number you can track over time.

The output isn't just CSVs sitting in a folder — it feeds Tableau and Plotly dashboards, and a Power Automate flow that used to be a person's Tuesday morning.

---

## How it fits together

```
Raw Data (Excel / CSV)
        │
        ▼
Data Cleaning & Prep (Pandas, NumPy)
        │
        ▼
SQL Database (Analytics Layer)
        │
        ▼
Machine Learning Layer
   ├── Random Forest   → Attrition Prediction
   ├── K-Means         → Employee Segmentation
   └── VADER           → Call-Center Sentiment
        │
        ▼
Scored Output (CSVs)
        │
        ▼
Visualization & Delivery
   ├── Tableau Dashboards
   ├── Plotly HTML Dashboards (browser, zero install)
   └── Power Automate → Scheduled Stakeholder Emails
```

---

## The three dashboards

| Dashboard | What it's for | The question it answers |
|---|---|---|
| **Analyzing Employee Trends** | HR analytics | Where is turnover concentrated, and which groups are most engaged? |
| **Automotive Industry Trends** | Sales & pricing | How do mileage, fuel type, and ownership history move used-car prices? |
| **CallCenter Data Analysis** | Operations | Are SLAs being met, and which channels are quietly underperforming? |

**Previews:**

![Employee Dashboard](Analyzing%20Employee%20Trends/Analyzing%20Employee%20Trends%20Dashboard.png)
![Automotive Dashboard](Exploring%20Trends%20in%20the%20Automotive%20Industry/Exploring%20Trends%20in%20the%20Automotive%20Industry.png)
![CallCenter Dashboard](CallCenter_Data%20Analysis/Callcenter%20Data%20Analysis.png)

---

## The machine learning layer

### Attrition Prediction + Employee Segmentation
`ml_models/workforce_ml_pipeline.py`

A Random Forest classifier trained on 50,000 synthetic employee records, with satisfaction score, tenure, overtime, and commute distance coming out as the strongest predictors. Each employee gets an attrition probability, a binary prediction, and a cluster segment — so instead of guessing who's a flight risk, HR can point retention efforts at the top 5% and skip the rest.

### Call-Center Sentiment Analysis
`ml_models/callcenter_sentiment.py`

VADER sentiment scoring applied to 10,000 synthetic call transcripts, landing around 92% agreement with ground-truth labels. Every call gets a compound sentiment score and a category (Positive / Neutral / Negative), making it possible to spot a sentiment dip before it shows up in a customer satisfaction survey three weeks later.

---

## Interactive dashboards, no server required

Inside `ml_dashboards/` are self-contained HTML dashboards — no Tableau license, no server, just open the file in a browser:

- `attrition_dashboard.html` — risk distribution, department-level comparisons, feature importance
- `employee_segments_dashboard.html` — cluster profiles, satisfaction vs. attrition trade-offs
- `callcenter_sentiment_dashboard.html` — sentiment distribution, compound score scatter, top complaint terms

Regenerate them anytime with:

```bash
cd ml_dashboards
python generate_dashboards.py
```

---

## Getting started

```bash
# Clone the repo
git clone https://github.com/sangramghose/Workforce-and-Industry-Trend-Analyzer.git
cd Workforce-and-Industry-Trend-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run the ML pipelines (this generates the scored CSVs)
python ml_models/workforce_ml_pipeline.py
python ml_models/callcenter_sentiment.py

# Build the browser dashboards
python ml_dashboards/generate_dashboards.py
```

From there, open any `.html` file in `ml_dashboards/`, or point the CSVs at Tableau, Power BI, or Excel if that's more your workflow.

---

## Repository structure

```
Workforce-and-Industry-Trend-Analyzer/
│
├── Analyzing Employee Trends/                    # Tableau workbook + preview image
├── CallCenter_Data Analysis/                     # Tableau workbook + preview image
├── Exploring Trends in the Automotive Industry/   # Tableau workbook + preview image
│
├── ml_models/
│   ├── workforce_ml_pipeline.py                  # Attrition prediction + clustering
│   └── callcenter_sentiment.py                   # NLP sentiment analysis
│
├── ml_dashboards/
│   ├── generate_dashboards.py                    # Builds the Plotly HTML dashboards
│   ├── attrition_dashboard.html
│   ├── employee_segments_dashboard.html
│   ├── callcenter_sentiment_dashboard.html
│   └── README.md
│
├── workforce_with_ml_results.csv                 # ML-scored employee data
├── callcenter_sentiment.csv                      # Sentiment-scored call data
├── requirements.txt
└── README.md
```

---

## Tech stack

| Layer | Tools |
|---|---|
| Data processing | Python (Pandas, NumPy), SQL |
| Machine learning | Scikit-learn (Random Forest, K-Means), NLTK (VADER) |
| Visualization | Tableau, Plotly |
| Automation | Power Automate, Outlook API |
| Delivery | Plotly HTML, Tableau Server / Public |

---

## Notes on the data

The employee, call-center, and automotive datasets used here are synthetic, built to mirror realistic distributions rather than pulled from a live production system. The pipeline, models, and dashboards are fully functional — this is meant to demonstrate the end-to-end engineering, not report on a real company's actual attrition numbers.

---

## Contact

**Sangram Keshari Ghose**
Data Engineering | Python · SQL · ETL Pipelines · Power BI · Tableau

[GitHub](https://github.com/sangram18-ghose) · [LinkedIn](https://linkedin.com/in/sangram20) · sangramkesharighose@gmail.com

If this project is useful to you, a star on the repo is always appreciated. Questions or ideas — feel free to open an issue.
