# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.inspection import permutation_importance

# Load the dataset
data = pd.read_csv("C:/Users/PC/Projects/DataCamp/Predictive Modeling for Agriculture/workspace/soil_measures.csv")

# Define features (X) and target variable (y)
X = data[["N", "P", "K", "ph"]]
y = data["crop"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Decision Tree Classifier
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)
dt_f1 = f1_score(y_test, dt_preds, average='weighted')
print(f"Decision Tree F1 Score: {dt_f1}")

# 2. Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)
rf_f1 = f1_score(y_test, rf_preds, average='weighted')
print(f"Random Forest F1 Score: {rf_f1}")

# Extract feature importances from Random Forest
rf_feature_importances = pd.DataFrame(
    {"Feature": X.columns, "Importance": rf_model.feature_importances_}
).sort_values(by="Importance", ascending=False)
print("Random Forest Feature Importances:")
print(rf_feature_importances)

# 3. Permutation Feature Importance
perm_importance = permutation_importance(
    rf_model, X_test, y_test, scoring="f1_weighted", n_repeats=5, random_state=42
)
perm_importance_df = pd.DataFrame(
    {"Feature": X.columns, "Importance": perm_importance.importances_mean}
).sort_values(by="Importance", ascending=False)
print("Permutation Feature Importances:")
print(perm_importance_df)

# Update best_predictive_feature with results from new models
best_predictive_feature = {
    "Random Forest Best Feature": rf_feature_importances.iloc[0].to_dict(),
    "Permutation Best Feature": perm_importance_df.iloc[0].to_dict(),
}

print("Best Predictive Features:")
print(best_predictive_feature)
