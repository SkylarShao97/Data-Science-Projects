# **Predictive-Modeling-for-Agriculture**  
Dive into agriculture using supervised machine learning and feature selection to aid farmers in crop cultivation and solve real-world problems.  

---

## **Project Description**  
A farmer reached out to you as a machine learning expert seeking help to select the best crop for his field. Due to budget constraints, the farmer explained that he could only afford to measure one out of the four essential soil measures:  

- **`Nitrogen`**: Content ratio in the soil  
- **`Phosphorous`**: Content ratio in the soil  
- **`Potassium`**: Content ratio in the soil  
- **`pH`**: Value of the soil  

The expert realized that this is a classic **feature selection problem**, where the objective is to pick the most important feature that could help predict the crop accurately.  

---

## **Sowing Success: How Machine Learning Helps Farmers Select the Best Crops**  
Measuring essential soil metrics such as nitrogen, phosphorous, potassium levels, and pH value is crucial for assessing soil condition. However, this process can be expensive and time-consuming, leading farmers to prioritize which metrics to measure based on budget constraints.  

Farmers aim to maximize their crop yields by planting the right crop for their soil conditions. Each crop has an ideal soil composition that ensures optimal growth. This project uses **machine learning** to assist farmers in selecting the best crop by analyzing soil metrics.  

---

## **Dataset Overview**  
The dataset, `soil_measures.csv`, contains the following columns:  
- `"N"`: Nitrogen content ratio in the soil  
- `"P"`: Phosphorous content ratio in the soil  
- `"K"`: Potassium content ratio in the soil  
- `"pH"`: pH value of the soil  
- `"crop"`: Target variable with categorical values representing various crop types  

Each row represents a set of soil metrics and the corresponding optimal crop. The goal is to predict the type of `"crop"` and determine the **single most important feature** for predictive performance.  

---

## **Project Objectives**  
1. **Feature Selection**: Identify the soil metric with the strongest predictive power for crop classification.  
2. **Modeling**: Build and evaluate multi-class classification models to predict crop type based on soil metrics.  
3. **Analysis**: Compare model performances and analyze feature importance.  
4. **Output**: Create a variable `best_predictive_feature`, which is a dictionary containing:  
   - The best feature name as the key.  
   - The evaluation score (e.g., F1-score) as the value.  

---

## **Methodology**  
1. **Data Preprocessing**:  
   - Load and clean the dataset.  
   - Handle missing values and split data into training and testing sets.  

2. **Feature Selection**:  
   - Evaluate each feature independently using logistic regression to find the feature with the best F1-score.  

3. **Modeling**:  
   - Train and compare the following models for multi-class classification:  
     - Logistic Regression  
     - Decision Trees  
     - Random Forest  

4. **Feature Importance Analysis**:  
   - Extract feature importance scores from Random Forest.  
   - Use **permutation importance** for model-agnostic insights.  

5. **Evaluation Metric**:  
   - Use weighted **F1-score** to evaluate model performance.  

---

## **Results**  
- **Potassium (K)** was identified as the most predictive feature for crop classification using logistic regression.  
- Random Forest provided robust predictions and offered insights into feature importance.  
- Permutation importance confirmed **K** as the most critical feature.  

The final `best_predictive_feature` variable:  
```python
best_predictive_feature = {"K": 0.85}  # Example score
```

---

## **Setup and Usage**  

### **Requirements**  
- Python 3.8+  
- Required libraries:  
  ```bash
  pip install pandas scikit-learn matplotlib
  ```  

### **How to Run**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/SkylarShao97/Data-Science-Projects.git
   cd Data-Science-Projects
   ```  
2. Place the dataset (`soil_measures.csv`) in the project directory.  
3. Run the main script:  
   ```bash
   python predictive_modeling_for_agriculture.py
   ```  

---

## **Future Improvements**  
1. Perform hyperparameter tuning for improved performance.  
2. Add more robust visualizations of feature importance.  
3. Create a web-based interface for user-friendly crop prediction.  

---

## **Contributors**  
- **Skylar Shao**  
  - Email: shaoskylar@gmail.com  
  - LinkedIn: [Skylar Shao](https://www.linkedin.com/in/zhenghong-shao-b18aa8220/)  

---

## **License**  
This project is licensed under the MIT License. Feel free to use and modify it for your purposes.  

