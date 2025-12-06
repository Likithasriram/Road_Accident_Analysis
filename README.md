 **🚗Road Accident Analysis (2021–2022)**

**Data Analytics Project**

Python • SQL • Power BI • Excel • EDA • Data Visualization

<p align="left"> <img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/SQL-Queries-red" /> <img src="https://img.shields.io/badge/PowerBI-Dashboard-brightgreen" /> <img src="https://img.shields.io/badge/Excel-Data%20Cleaning-lightgrey" /> <img src="https://img.shields.io/badge/Pandas-EDA-green" /> <img src="https://img.shields.io/badge/Matplotlib-Visualization-yellow" /> </p>

## 📑 Table of Contents
- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Business Problem](#business-problem)
- [Key Objectives](#key-objectives)
- [Top Insights](#top-insights)
- [Tech Stack](#tech-stack)
- [Dashboard Preview](#dashboard-preview)
- [KPI Validation](#kpi-validation)
- [Business Impact](#business-impact)
- [Methodology Summary](#methodology-summary)
- [Recommendations](#recommendations)
- [Future Enhancements](#future-enhancements)
- [Machine Learning Model](#machine-learning-model)
- [Project Structure](#project-structure)
- [How to Run This Project](#how-to-run-this-project)
- [About the Author](#about-the-author)


**Project Structure**

## ⭐ Project Overview


This project analyzes road accident data from 2021–2022 to uncover high-risk conditions, accident patterns, and contributing factors. The goal is to provide actionable insights for improving road safety and supporting data-driven decision-making by government authorities and transport planners.

Using Python, SQL, and Power BI, this end-to-end analysis delivers validated KPIs, visual dashboards, and clear business recommendations.

**📁Dataset Information**

The original dataset contains thousands of accident records with details such as severity, casualties, vehicle type, road type, weather, light conditions, and location.

Due to GitHub file size limitations, this repository includes a 900-row sample of the full dataset for demonstration purposes.

The complete dataset was used during analysis, EDA, SQL validation, and Power BI dashboard creation.

The sample uploaded here preserves the structure and key patterns of the original data.

## 🎯 Business Problem

Road accidents cause significant loss of life and economic damage.
Authorities need insights to:

Reduce accident frequency

Identify high-risk districts and vehicle types

Improve road infrastructure and lighting

Allocate resources efficiently

Implement targeted safety measures

This project provides those insights through an analytical and visual approach.

## 📊 Key Objectives

Analyze total accidents and casualties (2021–2022)

Validate all KPIs using SQL

Identify high-risk roads, vehicle categories, and time periods

Compare month-wise casualty trends

Examine environmental factors (weather, lighting, road type)

Build an interactive Power BI dashboard

## 🧠 Top Insights

Two-wheelers contribute the highest casualty share — major vulnerable group.

Night-time accidents have a significantly higher fatality rate than daytime accidents.

Urban areas report more accidents, but rural areas show higher severity.

Single carriageway roads account for the highest number of casualties.

Noticeable seasonal spikes during monsoon and festive months.

## 🛠️ Tech Stack

### Languages & Tools
- Python (Pandas, NumPy, Matplotlib)
- SQL Server
- Power BI
- Excel
- Google Colab

### Core Skills Demonstrated
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- SQL-Based KPI Validation  
- KPI & Metric Design  
- Dashboard Development  
- Insight Generation & Storytelling  


**Insight generation & storytelling**

## 🔄 Project Workflow

Data Collection → Cleaning → EDA → Visualization → Insights → Dashboard → Recommendations

## 📊 Dashboard Preview

<img src="dashboard/Road analysis screenshot.png" width="1000" alt="Road Accident Dashboard"/>


## 🧪 KPI Validation

All KPIs displayed in Power BI — including total accidents, total casualties, severity splits, monthly trends, and percentages — were independently validated using SQL queries.

This ensures that the dashboard metrics are:

Accurate

Consistent

Reliable for decision-making

## 🚀 Business Impact

This analysis helps authorities and policymakers:

Target road safety interventions more effectively

Prioritize infrastructure upgrades

Improve night-time visibility and lighting

Design campaigns for high-risk vehicle groups

Strengthen emergency response planning

By identifying high-risk factors, this project contributes to reducing accidents and saving lives.

## 🛣️ Methodology Summary

Data Cleaning — handled missing values, fixed date/time formats, standardized categories

EDA (Python) — distributions, correlations, severity analysis, monthly trends

SQL Validation — re-computed KPIs for accuracy

Dashboarding (Power BI) — built interactive visuals for deeper insight

Recommendations — actionable insights for safety improvement

## 📌 Recommendations

Strengthen enforcement and safety programs for two-wheeler riders

Install better lighting and reflective road markings in night-high-risk areas

Improve emergency medical access in rural regions

Upgrade single carriageway roads to safer designs

Implement seasonal awareness campaigns during peak accident months

## 🔮 Future Enhancements

Predict accident hotspots using machine learning

Add geospatial heatmaps (GIS mapping)

Build real-time streaming dashboard

Develop severity prediction models

## 🤖 Machine Learning Model (Accident Severity Prediction)

A machine learning model was developed to predict accident severity (Fatal / Serious / Slight).

### 🔧 Model Details
- **Algorithm:** RandomForestClassifier  
- **Preprocessing:**  
  - OneHotEncoding (categorical features)  
  - StandardScaler (numerical features)  
  - Missing value imputation  
- **Imbalance Handling:** `class_weight="balanced"`  
- **Train/Test Split:** 80/20  

### 📈 Model Performance
- **Accuracy:** 84.08%  
- Full classification report available at → `visuals/classification_report.txt`

### 🔝 Top Predictive Features
| Feature | Importance |
|--------|------------|
| Local_Authority_(District) | 0.4897 |
| Day_of_Week | 0.1064 |
| Vehicle_Type | 0.0643 |
| Number_of_Vehicles | 0.0501 |
| Number_of_Casualties | 0.0435 |
| Speed_limit | 0.0401 |
| Junction_Detail | 0.0380 |
| Road_Surface_Conditions | 0.0322 |
| Weather_Conditions | 0.0308 |
| Light_Conditions | 0.0299 |

### 📦 Model Artifacts (Saved)
- `models/severity_model.pkl`
- `visuals/confusion_matrix.png`
- `visuals/feature_importances.png`
- `visuals/sample_predictions.csv`


## 📁 Project Structure

├── 📄 Road_Accident_Analysis_Report.pdf
├── 📊 PowerBI_Dashboard.pbix
├── 📁 SQL_Validation_Queries.sql
├── 📓 Jupyter_Notebook_EDA.ipynb
├── 📁 models/
├── 📁 visuals/
└── README.md


---

# 🔧 **6️⃣ FIX How to Run Section*


## 🧩 How to Run This Project

 1️⃣ Clone the repository
```bash
git clone https://github.com/Likithasriram/Road_Accident_Analysis.git
cd Road_Accident_Analysis


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Open the notebook

jupyter notebook


4️⃣ Open the Power BI dashboard

/dashboard/Road_Accident_Analysis.pbix

## 👩‍💼 About the Author

P. Likhitha
Data Analyst | SQL | Python | Power BI
Passionate about turning raw data into meaningful insights.ningful insights.

