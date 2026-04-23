# 📊 Retail Sales Forecasting using Time-Series (Walmart Dataset)

## 📌 Project Overview
This project focuses on forecasting Walmart retail sales using time-series analysis. The goal is to analyze historical sales data, identify trends and seasonality, and predict future sales to support better inventory and demand planning.

---

## 🎯 Objective
- Understand sales patterns over time
- Identify seasonal trends and peak demand periods
- Forecast future sales using ARIMA model
- Provide business insights for inventory optimization

---

## 📂 Dataset
The dataset contains weekly sales data for Walmart stores, including:
- Date
- Weekly Sales (Target Variable)
- Store
- Holiday Flag
- Temperature, Fuel Price, CPI, Unemployment

---

## ⚙️ Data Preprocessing
- Converted Date column to datetime format
- Extracted Year, Month, Week, and Day features
- Sorted data by time and set Date as index
- Checked for missing values, duplicates, and anomalies
- Selected Store 1 for clean time-series modeling

---

## 📊 Exploratory Data Analysis
- Visualized weekly sales trends
- Identified seasonal patterns
- Analyzed holiday vs non-holiday sales
- Observed peak demand during late-year months

---

## 🤖 Model Used
### ARIMA (1,1,1)
- Checked stationarity using ADF test
- Applied differencing for stability
- Forecasted next 8 weeks of sales

---

## 📈 Results
- MAE: ~82,653
- RMSE: ~89,645
- Model shows stable and reliable predictions
- Forecast captures overall sales level with smooth trends

---

## 💼 Business Insights
- Peak demand occurs during November–December
- Inventory should be increased during high-demand periods
- Off-season demand drops in early months (Feb–March)
- Forecast helps reduce stockouts and optimize storage

---

## 📌 Conclusion
The ARIMA model successfully forecasts short-term sales trends and provides valuable insights for retail decision-making. The results can help businesses improve inventory planning and demand forecasting.

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Scikit-learn

---

## 🚀 Future Improvements
- Compare ARIMA with Linear Regression or SARIMA
- Use multiple stores for advanced modeling
- Implement time-series cross-validation
