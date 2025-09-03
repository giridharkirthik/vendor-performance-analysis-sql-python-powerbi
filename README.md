# 🧾 Vendor Performance Analysis – Retail Inventory & Sales

Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using **SQL, Python, and Power BI**.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Business Problem](#-business-problem)
- [Dataset](#-dataset)
- [Tools & Technologies](#-tools--technologies)
- [Project Structure](#-project-structure)
- [Data Cleaning & Preparation](#-data-cleaning--preparation)
- [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
- [Research Questions & Key Findings](#-research-questions--key-findings)
- [Dashboard](#-dashboard)
- [How to Run This Project](#-how-to-run-this-project)
- [Final Recommendations](#-final-recommendations)
- [Author & Contact](#-author--contact)

---

## 📖 Overview
This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for **purchasing, pricing, and inventory optimization**.  

A complete data pipeline was built using:
- **SQL** for ETL  
- **Python** for analysis & hypothesis testing  
- **Power BI** for visualization  

---

## 🎯 Business Problem
Effective inventory and sales management are critical in the retail sector.  
This project aims to:

- Identify underperforming brands needing pricing or promotional adjustments  
- Determine vendor contributions to sales and profits  
- Analyze the cost-benefit of bulk purchasing  
- Investigate inventory turnover inefficiencies  
- Statistically validate differences in vendor profitability  

---

## 📂 Dataset
- Multiple CSV files located in `/data/` folder (sales, vendors, inventory)  
- Summary table created from ingested data and used for analysis  

---

## 🛠️ Tools & Technologies
- **SQL** → Common Table Expressions, Joins, Filtering  
- **Python** → Pandas, Matplotlib, Seaborn, SciPy  
- **Power BI** → Interactive Visualizations  
- **GitHub** for version control  

---

## 📁 Project Structure
```bash
vendor-performance-analysis/
│
├── README.md
├── .gitignore
├── requirements.txt
├── Vendor Performance Report.pdf
│
├── notebooks/                  # Jupyter notebooks
│   ├── exploratory_data_analysis.ipynb
│   ├── vendor_performance_analysis.ipynb
│
├── scripts/                    # Python scripts for ingestion and processing
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── dashboard/                  # Power BI dashboard file
│   └── vendor_performance_dashboard.pbix

---

## 🧹 Data Cleaning & Preparation
Removed transactions with:
- Gross Profit ≤ 0  
- Profit Margin ≤ 0  
- Sales Quantity = 0  

---

Other steps:
- Created summary tables with vendor-level metrics  
- Converted data types  
- Handled outliers  
- Merged lookup tables  

---

## 📊 Exploratory Data Analysis (EDA)

### 🔎 Negative or Zero Values Detected
- Gross Profit: Min –52,002.78 (loss-making sales)  
- Profit Margin: Min –∞ (sales at zero or below cost)  
- Unsold Inventory → indicates slow-moving stock  

---

### 🚩 Outliers Identified
- High Freight Costs (up to 257K)  
- Large Purchase/Actual Prices  

---

### 📈 Correlation Analysis
- Weak → Purchase Price & Profit  
- Strong → Purchase Qty & Sales Qty (0.999)  
- Negative → Profit Margin & Sales Price (–0.179)  

---

## ❓ Research Questions & Key Findings
- **Brands for Promotions** → 198 brands with low sales but high profit margins  
- **Top Vendors** → Top 10 vendors = 65.69% of purchases → over-reliance risk  
- **Bulk Purchasing Impact** → 72% cost savings per unit in large orders  
- **Inventory Turnover** → $2.71M worth of unsold inventory  
- **Vendor Profitability**:  
  - High Vendors → Mean Margin = 31.17%  
  - Low Vendors → Mean Margin = 41.55%  
- **Hypothesis Testing** → Statistically significant difference in profit margins → distinct vendor strategies  

---

## 📊 Dashboard
The Power BI Dashboard shows:
- Vendor-wise Sales & Margins  
- Inventory Turnover  
- Bulk Purchase Savings  
- Performance Heatmaps  

---

## ⚡ How to Run This Project
```bash
# 1️⃣ Clone this repository
git clone https://github.com/your-username/vendor-performance-analysis.git
cd vendor-performance-analysis

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run ingestion scripts to prepare the database
python scripts/ingestion_db.py

# 4️⃣ Open Jupyter notebooks in /notebooks/ for analysis

# 5️⃣ Explore insights via Power BI Dashboard
open dashboard/vendor_performance_dashboard.pbix

---

**## ✅ Final Recommendations
- Reconsider reliance on top 10 vendors → diversify procurement  
- Promote high-margin but low-sales brands  
- Optimize freight costs via new logistics contracts  
- Address $2.71M unsold inventory via clearance strategies  

---

## 👤 Author & Contact
**Giridhar Kirthik H**  
📧 [giridharkirthikh2001@gmail.com]
