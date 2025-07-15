# 🚗 Car Price Prediction

A machine learning project for predicting used car prices using **regression** and **tree-based models**.

---

## 🔍 Key Findings

Car price prediction is based on features such as **manufacturing year**, **car age**, **kilometers driven**, and more. This helps users — whether buyers, sellers, or dealers — make informed decisions by estimating a fair market value for any car.

---

## 🧩 Business Problem

Determining the right price for a used car can be challenging due to the influence of multiple variables. This application allows **dealers** and **individual sellers** to input a car’s details and receive an estimated selling price that's closely aligned with **actual market trends**. It helps prevent underpricing or overpricing, making it useful for both pricing and negotiation purposes.

---

## 📁 Data Source

Dataset from Kaggle:  
🔗 [Car Price Prediction Dataset](https://www.kaggle.com/code/mohaiminul101/car-price-prediction)

---

## ⚙️ Methodology

- 📊 Exploratory Data Analysis (EDA)  
- 🔧 Data Transformation  
- 🧹 Data Preparation  
- 🧠 Model Training  
- 📈 Model Evaluation  

---

## 🛠️ Tech Stack

- **Python** (dependencies managed via `requirements.txt`)  
- **Streamlit** (used for interactive web interface)  

---

## 📈 Model Performance

| Model              | Train R² | Test R² |     MAE     |    RMSE     |
|--------------------|----------|---------|-------------|-------------|
| Linear Regression  | 0.747    | 0.736   | 113,404.94  | 154,842.57  |
| Ridge Regression   | 0.747    | 0.736   | 113,385.53  | 154,848.90  |
| Lasso Regression   | 0.747    | 0.736   | 113,404.94  | 154,842.57  |
| Random Forest      | 0.973    | 0.886   | 66,799.70   | 101,696.78  |
| Gradient Boosting  | 0.966    | 0.895   | 64,583.00   | 97,784.77   |
| **XGBoost**        | 0.962    | **0.896** | **64,576.10** | **97,150.58** |

---

## 🏆 Best Model: **XGBoost**

### Why XGBoost?

Cars are rapidly depreciating assets. Each year, new models with advanced technologies reduce the value of older vehicles. Additionally, factors like **kilometers driven**, **ownership history**, and **engine power** greatly affect the resale price.

XGBoost handles complex patterns and interactions effectively and provides the **best performance** across all evaluation metrics — making it the most suitable model for predicting car prices accurately.

---

## 📌 Visual Insights

### 🔗 Correlation Between Features  
![Correlation Matrix](https://github.com/user-attachments/assets/2c70c636-99f3-47df-9ef4-f252a6363ad5)

### 🔍 Feature Importance  
![Feature Importance](https://github.com/user-attachments/assets/0fe24b72-a9ab-4a58-8e38-0e0ea9536bf8)

### 🎯 Actual vs Predicted (XGBoost)  
![Actual vs Predicted](https://github.com/user-attachments/assets/b7c2a52c-7c9c-4179-9529-7f113f464d59)

---

## 🎓 Lessons Learned & Recommendations

- **Outlier Handling**:  
  Outliers — particularly from **luxury brands** like BMW and Mercedes-Benz — were found to **skew model performance**. These brands retain high resale value even when the cars are older or have high mileage.

  ✅ Strategy:  
  - **Kept moderate outliers** that reflect realistic luxury vehicle behavior  
  - **Removed extreme outliers** that significantly distorted the model

- **Key Features**:
  - Most important: `year`, `max_power (bhp)`, `is_luxury`, `engine (CC)`, `is_popular`
  - Least impactful: `transmission`

📌 **Recommendation**: Focus on meaningful features and carefully manage outliers for better predictions.

---

## ⚠️ Limitations & Future Improvements

- **Dataset Size**:  
  The dataset contains **8,128 rows** and **13 columns**. Expanding the dataset could improve model robustness and performance.

- **Model Variety**:  
  Only 6 models were tested. Future work can include:
  - More algorithms (e.g., CatBoost, LightGBM, deep learning models)
  - Advanced hyperparameter tuning
  - Model ensembling or stacking techniques

---
