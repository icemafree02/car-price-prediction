# car-price-prediction
Car price prediction project using Regression and Tree-based model 
-----------------
# key findings : Car price prediction base on age of car, year, released km-driven etc. Give the predicion result for best decision in purchase car.
-----------------
# Business Problem
This app predicts the car price that based on information and usage of specific car. When the dealer or individual person want to sell the car, they can input the information and predict the price approximate the real price in the market. This app can be used by the individual or dealer who wants to sell car or making decision.
-----------------
# Data Source
https://www.kaggle.com/code/mohaiminul101/car-price-prediction
-----------------
# Method
- Exploratory Data Analysis
- Data Transformation
- Data Preparation
- Model Training
- Model Evaluation
-----------------
# Tech Stack
- Python (requirements.txt is used in this project)
- Streamlit (interface for model)
------------------
# Quick Glance at result
Correlation between features
<img width="832" height="735" alt="image" src="https://github.com/user-attachments/assets/2c70c636-99f3-47df-9ef4-f252a6363ad5" />
Features Importance
<img width="946" height="611" alt="image" src="https://github.com/user-attachments/assets/0fe24b72-a9ab-4a58-8e38-0e0ea9536bf8" />
Actual vs Predicted of XGBoost
<img width="790" height="590" alt="image" src="https://github.com/user-attachments/assets/b7c2a52c-7c9c-4179-9529-7f113f464d59" />
Model evaluation

| Model              | Train R² | Test R² |     MAE     |    RMSE     |
|--------------------|----------|---------|-------------|-------------|
| Linear Regression  | 0.747    | 0.736   | 113,404.94  | 154,842.57  |
| Ridge Regression   | 0.747    | 0.736   | 113,385.53  | 154,848.90  |
| Lasso Regression   | 0.747    | 0.736   | 113,404.94  | 154,842.57  |
| Random Forest      | 0.973    | 0.886   | 66,799.70   | 101,696.78  |
| Gradient Boosting  | 0.966    | 0.895   | 64,583.00   | 97,784.77   |
| XGBoost            | 0.962    | 0.896   | 64,576.10   | 97,150.58   |

- The best model for prediction : XGBoost
- Why choose XGBoost as model prediction
    - Cars are rapidly depreciating assets. Every year, manufacturers introduce new models with advanced technologies, which significantly reduces the value of older car. Additionally, several factors contribute to the decline in a car's resale price — such as kilometers driven, age of the car, and the number of previous owners. These variables make it difficult to set an appropriate selling price. To sell a car effectively, it's crucial to ensure that the listed price is neither too high nor too low, but instead aligned with market expectations. Choosing the best model for price prediction helps estimate a selling price that closely reflects the true market value, ensuring fairness for both buyers and sellers.
 
Conclusion : In our case, choosing the XGBoost for car price prediction is ideal.
----------------------------
# Lessons Learned and Recommendations
- During the analysis phase of this project, we identified outliers that significantly skewed the model’s performance and distorted summary statistics across several variables. One major source of these outliers came from luxury brands such as BMW and Mercedes-Benz, which tend to retain high resale value despite high mileage or age — unlike most standard car brands. However, removing all outliers would result in the loss of valuable data related to the luxury segment, which is crucial for a well-rounded prediction model. Therefore, instead of dropping all high-priced or unusual records, we adopted a balanced approach:

    - Retain moderate outliers that reflect real-world behavior (e.g., older luxury cars still selling at high prices).

    - Remove extreme outliers that heavily skew the model and are statistically inconsistent with typical trends.

- we found out the most important features: year and max_power (bhp) are the most effective the model performance features to prediction the price, also the is_luxury, engine (CC), is_popular are useful, the least useful is transmission.
- Recommendation would be to focus on the reasonable outliers and effective features.
-----------------------------
# Limitaion and Things that can be improved
- Dataset: The improvement for model would be to gain more data (currently have 8128 row and 13 columns) for the most effective and precision predict price.
- Model: The model for prediction was only 6 models, The best way for reaching the precise price is try more model and improve the hyperparameter tuning.

