# 🚀 Enterprise Customer Segmentation & Analytics — v1.0.0 (Initial Public Release)

**From raw data to actionable customer intelligence — powered by SQL & Python**

## 📦 What's Inside
- **Interactive Jupyter Notebook**
  - Data cleaning & preparation
  - Advanced SQL (CTEs, window functions, LAG/LEAD, multi-dimensional segmentation)
  - Performance tuning with EXPLAIN
  - Business-driven narratives and executive summaries
  - Interactive dashboards via ipywidgets
  - Predictive "Potential VIP" identification

- **Reusable Python Toolkit (`analytics_toolkit.py`)**
  - Database connection helpers
  - Query runner for Pandas DataFrames
  - Parameterized `find_potential_vips()` predictive query

- **Supporting Files**
  - `requirements.txt` for reproducibility
  - `LICENSE` (MIT) for open usage
  - `README.md` with quick start and productionization guidance

## 💼 Business Value
Empowers analysts, data scientists, and BI teams to:
- Identify top-value customers and emerging VIPs
- Track purchase frequency and product diversity
- Automate and schedule customer insights reports
- Transition smoothly from exploration to production

## 📈 Key Business Questions Answered
1. **Who are our customers?** — Data cleaning and foundational segmentation
2. **How do they behave?** — Frequency, variety, and VIP identification
3. **Who should we focus on next?** — Predictive segment for high-potential customers

---

## 🏷️ Version
**v1.0.0** — Initial Public Release

## 🔖 Tagging Instructions
```bash
git tag -a v1.0.0 -m "Initial public release: Enterprise Customer Segmentation & Analytics"
git push origin v1.0.0
```

## 🧭 Roadmap
- **v1.1.0** — Add optional seed data, more annotated visualizations
- **v1.2.0** — Parameterized dashboard, at-risk VIP helper
- **v2.0.0** — DB adapters (Postgres/BigQuery), breaking changes
