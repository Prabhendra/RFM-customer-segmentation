# 🧠 Customer Segmentation RFM Automation

![Automated with Python](https://img.shields.io/badge/Automated%20With-Python-blue?style=flat-square&logo=python)

This folder contains the **automated RFM (Recency, Frequency, Monetary) Analysis pipeline** using Python and SQLite, which classifies customers into meaningful business segments like _Champions_, _Loyal Customers_, and _At Risk_.📁 Customer Segmentation RFM Automation
This folder contains the automated RFM (Recency, Frequency, Monetary) Analysis pipeline using Python and SQLite, which classifies customers into meaningful business segments like Champions, Loyal Customers, and At Risk.

🔍 Objective
To automate the full customer segmentation process, from CSV data ingestion to RFM scoring and final export, without manual Excel or SQL queries every time.

⚙️ Tools Used
Python

pandas

SQLite (via sqlite3)

Jupyter Notebook / VS Code

CSV File Input/Output

🔁 Automation Pipeline Steps
Load the CSV
Import customer transaction data from a .csv file.

Connect to SQLite
Automatically creates a SQLite database and uploads data into it.

Create Tables & Clean Data
Removes nulls, invalid entries, ensures types are correct.

Calculate RFM Metrics

Recency: Days since last transaction

Frequency: Number of transactions

Monetary: Total amount spent

RFM Scoring
Scores each customer (1–5) for R, F, and M based on quantiles.

Customer Segmentation
Segments customers into groups like:

🏆 Champion

❤️ Loyal

🆕 New

⚠️ At Risk

❌ Lost

Export Result
Final segmented data is exported as rfm_segmented_export.csv.
