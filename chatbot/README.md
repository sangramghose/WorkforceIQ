<div align="center">

# 💬 Chatbot

**A natural-language interface to the Workforce & Industry Trend Analyzer's outputs.**

![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Functional-success)

</div>

---

Instead of opening a dashboard and hunting for the right filter, you just ask. "Which department has the highest attrition risk?" — and the answer comes straight from the scored data, not a menu of chart tabs.

This isn't a separate project bolted on for the sake of having a chatbot. It sits directly on top of the same CSVs the dashboards already use — `workforce_with_ml_results.csv` and `callcenter_sentiment.csv` — so anything the Random Forest, K-Means, and VADER models already computed becomes queryable in plain English.

---

## Why it exists

Dashboards are built for people who want to explore. This is built for people who just want the answer — a manager checking "who's at risk on my team" without learning Tableau, or a quick sanity check mid-meeting when opening a BI tool isn't practical.

---

## How it fits into the pipeline

```
Scored Output (CSVs)
        │
        ├── Tableau Dashboards         → for people who want to explore
        ├── Plotly HTML Dashboards     → for a quick browser-based look
        └── Chatbot (this folder)      → for people who just want an answer
```

Same models, same data, no duplicated logic — it's a fourth way to consume one pipeline. Re-run the ML scripts, and the chatbot's answers update automatically along with everything else.

---

## Run it

```bash
pip install -r requirements.txt
streamlit run chatbot/app.py
```

Opens a local Streamlit app in your browser, ready to take questions against the scored datasets.

---

## What you can ask it

| Category | Example question |
|---|---|
| Attrition risk | "Which department has the highest predicted attrition risk?" |
| Segmentation | "Show me employees in the high-risk, low-satisfaction segment." |
| Sentiment | "What's the average sentiment score for calls this week?" |
| Summary stats | "How many employees are flagged as high risk overall?" |

---

## Under the hood

- **Data layer:** reads directly from the pipeline's scored CSV outputs — no separate database, no duplicated data source.
- **Interface:** Streamlit, chosen for how fast it turns a Python script into something someone can actually click through without a frontend build step.
- **Consistency by design:** because it queries the same files the dashboards read from, the chatbot's answers and the dashboard numbers can never drift out of sync.

---

## Notes on the data

Like the rest of the project, this runs against the synthetic datasets described in the [main README](../README.md#notes-on-the-data). The interface and retrieval logic are fully functional — the underlying records aren't pulled from a live company system.

---

## Part of a larger project

This chatbot is one piece of the [Workforce & Industry Trend Analyzer](../README.md) — see the main README for the full pipeline, the ML models behind these numbers, and the Tableau/Plotly dashboards this chatbot complements.
