# Cardio Disease Prediction

## Overview

This project aims to analyze the influence of various factors on the presence of cardiovascular disease. The study considers demographic features like age and gender, physical attributes such as height and weight, clinical measurements like blood pressure and cholesterol levels, and lifestyle habits like alcohol consumption and physical activity. The goal is to identify key determinants of cardiovascular disease and provide insights for healthcare professionals and individuals.

## Dataset

The dataset used for this analysis is sourced from Kaggle and can be found at [CardioVascular Disease Dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/data). It includes data on a range of factors related to cardiovascular health and is publicly available for research and analysis.

## Tools and Technologies

The analysis and application development were conducted using Python, leveraging the following libraries and frameworks:

- **Pandas** for data manipulation and analysis
- **NumPy** for numerical computations
- **Matplotlib** and **Seaborn** for data visualization and statistical graphics
- **Scikit-learn** for machine learning model development and evaluation
- **Flask** for building the web application and prediction pipeline

## Project Structure

The project consists of the following components:

- **[Exploratory Data Analysis (EDA) Notebook](https://github.com/Vanderval31bs/CardioDiseasePrediction/blob/main/EDA.ipynb)**: This notebook performs data exploration, visualization, and preliminary analysis to understand the dataset and identify potential correlations and trends.
- **[Model Training Notebook](https://github.com/Vanderval31bs/CardioDiseasePrediction/blob/main/Model_Training.ipynb)**: This notebook focuses on training and evaluating different machine learning models to predict the presence of cardiovascular disease. It includes model performance comparisons, hyperparameter tuning, and final results.
- **[Flask Application](https://github.com/Vanderval31bs/CardioDiseasePrediction/blob/main/application.py)**: This directory contains the Flask web application, which serves as a user interface for making predictions. The application includes a prediction pipeline that preprocesses input data, applies the trained machine learning model, and returns the prediction outcome.

## How to Run

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Vanderval31bs/CardioDiseasePrediction.git
   cd CardioDiseasePrediction

   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

   ```

3. Run the Flask application:

   ```bash
    python application.py

   ```

4. Access the application at http://localhost:5000.

## Results

Utilizing a grid search with cross-validation, the chosen model was XGBoost with the following parameters:
- `n_estimators = 300`
- `learning_rate = 0.05`
- `max_depth = 4`

The model achieved an accuracy of 0.73 on the test set, that is, it correctly predicted 73% of the instances.

## Conclusions

Based on the dataset, the following conclusions can be drawn regarding cardiovascular disease:

- There is a significant correlation between blood pressure levels and the presence of the condition, with higher levels indicating greater risk.
- Advanced age and higher weight are predisposing factors for cardiovascular disease.
- Elevated levels of glucose and cholesterol are associated with heart issues.
- Regular physical activity correlates positively with heart health.
- Smoking shows little correlation with heart disease. While there is a higher prevalence of cardiovascular disease among those who consume alcohol, the correlation is not statistically significant based on the tests applied.
- Gender and height show some correlation with the disease, although these correlations are relatively low.

**Disclaimer:** This analysis is conducted for educational purposes and does not possess medical scientific rigor. As such, it should not be considered authoritative medical advice. Additionally, the reliability of the dataset used in this study is uncertain, and caution should be exercised when interpreting these findings.

## Contact

For any questions or feedback, please contact [Vanderval](mailto:vander31bs@gmail.com).
