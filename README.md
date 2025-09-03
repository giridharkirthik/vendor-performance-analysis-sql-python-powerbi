# 📦 Vendor Performance Analysis (SQL + Python + Power BI)

## 🧹 Data Cleaning & Preparation
- Removed transactions with:
  - Gross Profit ≤ 0  
  - Profit Margin ≤ 0  
  - Sales Quantity = 0  
- Other steps:
  - Created summary tables with vendor-level metrics  
  - Converted data types  
  - Handled outliers  
  - Merged lookup tables  

---

## 📊 Exploratory Data Analysis (EDA)

### 🔎 Negative or Zero Values Detected
- **Gross Profit**: Min –52,002.78 (loss-making sales)  
- **Profit Margin**: Min –∞ (sales at zero or below cost)  
- **Unsold Inventory** → indicates slow-moving stock  

### 🚩 Outliers Identified
- High Freight Costs (up to 257K)  
- Large Purchase/Actual Prices  

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

### Vendor Profitability
- High Vendors → Mean Margin = **31.17%**  
- Low Vendors → Mean Margin = **41.55%**  

### Hypothesis Testing
- Statistically significant difference in profit margins → distinct vendor strategies  

---

## 📊 Dashboard
The Power BI Dashboard shows:
- Vendor-wise Sales & Margins  
- Inventory Turnover  
- Bulk Purchase Savings  
- Performance Heatmaps  

---

## ⚡ How to Run This Project

### 1️⃣ Clone this repository
```bash
git clone https://github.com/your-username/vendor-performance-analysis.git
cd vendor-performance-analysis
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run ingestion scripts to prepare the database

```bash
python scripts/ingestion_db.py
```

### 4️⃣ Open Jupyter notebooks

Open the notebooks in `/notebooks/` for analysis.

### 5️⃣ Explore insights via Power BI Dashboard

* **Windows**:

  ```bash
  start dashboard/vendor_performance_dashboard.pbix
  ```
* **macOS**:

  ```bash
  open dashboard/vendor_performance_dashboard.pbix
  ```

---

## ✅ Final Recommendations

* Reconsider reliance on top 10 vendors → diversify procurement
* Promote high-margin but low-sales brands
* Optimize freight costs via new logistics contracts
* Address \$2.71M unsold inventory via clearance strategies

---

## 👤 Author & Contact

**Giridhar Kirthik H**
📧 [giridharkirthikh2001@gmail.com]

