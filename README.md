<div align="center">

# Workforce & Industry Trend Analyzer

**A full analytics pipeline — from raw data to predictive models to dashboards people actually open.**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-4B8BBE)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?logo=pandas&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-Dashboards-E97627?logo=tableau&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3F4F75?logo=plotly&logoColor=white)
![Power Automate](https://img.shields.io/badge/Power%20Automate-Workflow-0066FF?logo=microsoftpowerautomate&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Actively%20Maintained-success)

</div>

---

<div align="center">

| | | |
|---|---|---|
| **50,000** employee records modeled | **10,000** call transcripts scored | **3** production dashboards |
| **85%+** attrition prediction accuracy | **~92%** sentiment-label agreement | **4** behavioral employee segments |

</div>

---

### Table of contents

1. [Why this exists](#why-this-exists)
2. [What this project actually does](#what-this-project-actually-does)
3. [How it fits together](#how-it-fits-together)
4. [The three dashboards](#the-three-dashboards)
5. [The machine learning layer](#the-machine-learning-layer)
6. [Interactive dashboards, no server required](#interactive-dashboards-no-server-required)
7. [Getting started](#getting-started)
8. [Repository structure](#repository-structure)
9. [Tech stack](#tech-stack)
10. [Design decisions worth knowing about](#design-decisions-worth-knowing-about)
11. [What I'd build next](#what-id-build-next)
12. [FAQ](#faq)
13. [Notes on the data](#notes-on-the-data)
14. [Contributing](#contributing)
15. [License](#license)
16. [Contact](#contact)

---

## Why this exists

Every HR team eventually hits the same wall: attrition data lives in one spreadsheet, sentiment gets tracked (if at all) in another, and by the time someone notices a pattern, the pattern has already cost them a few good employees. This project started as a way to stop assembling that HR report by hand every week, and turned into something closer to a small internal analytics platform — data cleaning, three ML models, SQL, and dashboards that all talk to each other instead of living as disconnected files.

The goal wasn't to build the fanciest model. It was to build something that starts from messy raw data and ends with a stakeholder-ready dashboard, without a human manually stitching the steps together in between.

---

## What this project actually does

Three real business questions, one connected pipeline:

- **Will this employee leave?** A Random Forest model trained on 50,000 employee records flags attrition risk before it becomes a resignation letter.
- **Who are our employees, really?** K-Means clustering groups the workforce into behavioral segments — including one small, high-risk, low-satisfaction cohort that wouldn't show up from just eyeballing a spreadsheet.
- **Are customers actually happy on our calls?** VADER sentiment analysis runs over thousands of call transcripts and turns "we think service is fine" into a number you can actually track over time.

The output isn't CSVs sitting in a folder waiting to be forgotten — it feeds Tableau and Plotly dashboards, plus a Power Automate flow that replaced what used to be someone's Tuesday morning.

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

Each stage writes its output to disk before the next one picks it up, so any layer — the cleaning script, a model, a dashboard — can be re-run or swapped independently without breaking the rest of the pipeline.

---

## The three dashboards

### 1. Analyzing Employee Trends
Built for HR to look at the workforce from every angle that actually matters:
- Employee distribution across business units, roles, age, gender, and education level
- Satisfaction and engagement trends, with attrition broken down by demographic and job factors
- Compensation analysis alongside core HR KPIs

![Employee Dashboard](Analyzing%20Employee%20Trends/Analyzing%20Employee%20Trends%20Dashboard.png)

### 2. Exploring Trends in the Automotive Industry
A used-car market lens applied to sales, pricing, and depreciation:
- Sales trends and pricing broken down by fuel type, transmission, and ownership history
- Mileage-age-price correlation, plus volume by dealer and owner type
- A basic forward-looking price forecast

![Automotive Dashboard](Exploring%20Trends%20in%20the%20Automotive%20Industry/Exploring%20Trends%20in%20the%20Automotive%20Industry.png)

### 3. CallCenter Data Analysis
Where the sentiment model output actually gets used by a human:
- Call volume, sentiment, and complaint-type breakdowns
- Response time vs. SLA, compared across channels — phone, email, chat, web
- Performance broken down by location

![CallCenter Dashboard](CallCenter_Data%20Analysis/Callcenter%20Data%20Analysis.png)

---

## The machine learning layer

### Attrition Prediction + Employee Segmentation
`ml_models/workforce_ml_pipeline.py`

A Random Forest classifier trained on 50,000 synthetic employee records, with satisfaction score, tenure, overtime, and commute distance coming out as the strongest predictors. Each employee gets an attrition probability, a binary prediction, and a cluster segment — so instead of guessing who's a flight risk, HR can point retention efforts at the highest-risk group and skip the rest.

K-Means then groups the same workforce into four behavioral personas based on satisfaction, workload, and engagement signals. One of those clusters — small, low-satisfaction, high-overtime — turns out to be disproportionately responsible for predicted attrition, which is exactly the kind of pattern that's invisible until you cluster for it.

### Call-Center Sentiment Analysis
`ml_models/callcenter_sentiment.py`

VADER sentiment scoring applied to 10,000 synthetic call transcripts, landing around 92% agreement with ground-truth labels. Every call gets a compound sentiment score and a category (Positive / Neutral / Negative), which makes it possible to spot a sentiment dip in near real time instead of waiting three weeks for it to show up in a satisfaction survey.

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

## Design decisions worth knowing about

A few choices that weren't obvious at first but shaped the final structure:

- **Random Forest over a black-box model.** Feature importance was more valuable here than squeezing out an extra percentage point of accuracy — HR needs to know *why* someone is flagged as a risk, not just that they are.
- **Plotly dashboards alongside Tableau, not instead of it.** Tableau is great for stakeholders who already live in it; the HTML dashboards exist so anyone can open a result without a Tableau license or server access.
- **Every stage writes to disk.** Scored CSVs are treated as a contract between pipeline stages. It's less elegant than an in-memory pipeline, but it means any single step can be debugged or re-run in isolation.

---

## What I'd build next

- Swap the static CSV inputs for a scheduled ingestion job, so the models retrain on a rolling window instead of a one-time snapshot.
- Add a lightweight model-monitoring layer to track prediction drift over time.
- Extend the sentiment model beyond VADER's lexicon-based scoring to a fine-tuned transformer for higher accuracy on sarcasm and mixed-sentiment calls.

---

## FAQ

**Is this real company data?**
No — see [Notes on the data](#notes-on-the-data) below. The engineering, models, and dashboards are all real and fully functional; the underlying records are synthetic.

**Can I run this without Tableau?**
Yes. The `ml_dashboards/` folder has self-contained HTML dashboards that only need a browser — no Tableau license or server required.

**Why Random Forest instead of a more advanced model?**
Interpretability. HR stakeholders need to know *why* someone is flagged, not just get a black-box probability. Feature importance from Random Forest gives a defensible answer to "why is this person high-risk?" — see [Design decisions](#design-decisions-worth-knowing-about).

**Can I plug in my own data?**
Yes — replace the input CSVs with your own, keeping the same column structure the scripts expect, then re-run the pipeline as described in [Getting started](#getting-started).

---

## Notes on the data

The employee, call-center, and automotive datasets used here are synthetic, built to mirror realistic distributions rather than pulled from a live production system. The pipeline, models, and dashboards are fully functional — this is meant to demonstrate the end-to-end engineering, not report on a real company's actual attrition numbers.

---

## Contributing

This started as a solo project, but it's structured to be extended. If you spot a bug, have an idea for a new model, or want to swap in a different dataset, issues and pull requests are welcome. For anything sizable, opening an issue first to talk through the approach is the fastest path to a merge.

---

## License

Released under the [MIT License](LICENSE) — use it, fork it, adapt it for your own portfolio or coursework, just keep the attribution.

---

## Contact

**Sangram Keshari Ghose**
Data Engineering | Python · SQL · ETL Pipelines · Power BI · Tableau

[GitHub](https://github.com/sangram18-ghose) · [LinkedIn](https://linkedin.com/in/sangram20) · sangramkesharighose@gmail.com

If this project is useful to you, a star on the repo is always appreciated. Questions or ideas — feel free to open an issue.
