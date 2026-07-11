"""
Workforce AI/ML Pipeline
- Generates synthetic employee data (50K rows)
- Trains attrition prediction model (Random Forest)
- Applies K-Means clustering for employee segmentation
- Exports scored data for dashboard integration (Tableau/Power BI)

Author: [Your Name]
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# -------------------------------
# 1. Generate Synthetic Employee Data
# -------------------------------
np.random.seed(42)
n = 50000

data = {
    'employee_id': range(1, n+1),
    'age': np.random.normal(35, 10, n).astype(int).clip(20, 65),
    'gender': np.random.choice(['Male', 'Female'], n, p=[0.6, 0.4]),
    'department': np.random.choice(['Sales', 'R&D', 'HR', 'Finance', 'Marketing'], n),
    'job_level': np.random.choice(['Entry', 'Mid', 'Senior', 'Lead'], n, p=[0.3, 0.4, 0.2, 0.1]),
    'years_at_company': np.random.exponential(5, n).astype(int).clip(0, 30),
    'monthly_salary': np.random.normal(5000, 2000, n).clip(1500, 15000),
    'overtime': np.random.choice(['Yes', 'No'], n, p=[0.25, 0.75]),
    'projects_completed': np.random.poisson(8, n).clip(0, 25),
    'satisfaction_score': np.random.normal(3.5, 0.8, n).clip(1, 5).round(1),
    'last_promotion_years': np.random.exponential(4, n).astype(int).clip(0, 15),
    'commute_distance': np.random.choice(['Near', 'Far', 'Very Far'], n, p=[0.5, 0.35, 0.15]),
}

df = pd.DataFrame(data)

# Create attrition target (based on some patterns)
df['attrition'] = np.where(
    (df['satisfaction_score'] < 2.5) | 
    ((df['overtime'] == 'Yes') & (df['years_at_company'] > 4)) |
    (df['commute_distance'] == 'Very Far'),
    'Yes', 'No')
# Introduce some noise
df.loc[np.random.choice(df.index, size=2000, replace=False), 'attrition'] = np.random.choice(['Yes', 'No'], 2000)

print("Dataset shape:", df.shape)
print("Attrition distribution:\n", df['attrition'].value_counts(normalize=True))

# -------------------------------
# 2. Preprocessing
# -------------------------------
# Encode categorical variables
df_encoded = pd.get_dummies(df, columns=['gender', 'department', 'job_level', 'overtime', 'commute_distance'], drop_first=True)

# Features for prediction (drop non-features)
feature_cols = [c for c in df_encoded.columns if c not in ['employee_id', 'attrition']]
X = df_encoded[feature_cols]
y = df_encoded['attrition'].map({'Yes': 1, 'No': 0})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale for clustering later; for tree-based models scaling is not required, but we'll keep a scaled version for clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------
# 3. Attrition Prediction Model
# -------------------------------
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print("\n--- Attrition Prediction (Random Forest) ---")
print("Accuracy on test set:", round((y_pred == y_test).mean(), 3))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['No', 'Yes']))

# Feature importance
importances = pd.Series(rf.feature_importances_, index=feature_cols).sort_values(ascending=False).head(10)
print("\nTop 10 Feature Importances:")
print(importances)

# Predict attrition probability for all employees
df['attrition_prob'] = rf.predict_proba(X)[:, 1]
df['predicted_attrition'] = np.where(df['attrition_prob'] > 0.5, 'Yes', 'No')

# -------------------------------
# 4. Employee Segmentation (K-Means Clustering)
# -------------------------------
# We'll use a subset of behavioral features for clustering (salary, satisfaction, years, projects, etc.)
cluster_features = ['years_at_company', 'monthly_salary', 'satisfaction_score',
                    'projects_completed', 'last_promotion_years', 'attrition_prob']
X_cluster = df[cluster_features]
scaler_kmeans = StandardScaler()
X_cluster_scaled = scaler_kmeans.fit_transform(X_cluster)

# Find optimal clusters using inertia elbow (in practice you'd plot; we'll use a heuristic)
inertias = []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_cluster_scaled)
    inertias.append(km.inertia_)

# For simplicity, pick k=4 (you can adjust based on elbow)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['segment'] = kmeans.fit_predict(X_cluster_scaled)

# Profile segments
segment_profile = df.groupby('segment')[cluster_features].mean().round(2)
segment_profile['size'] = df['segment'].value_counts()
print("\n--- Employee Segments (K-Means) ---")
print(segment_profile)

# Add segment labels based on profiles (manual mapping example)
# You can customize these based on observed means
# For demonstration, let's map them with a simple if-else using a dictionary (in real project, you'd inspect)
# We'll assign meaningful names if patterns match.
# Here we'll just attach numeric labels, but you can later rename in Tableau.

# -------------------------------
# 5. Export Results for Dashboard
# -------------------------------
# Keep relevant columns for Tableau/Power BI
export_df = df[['employee_id', 'age', 'gender', 'department', 'job_level',
                 'years_at_company', 'monthly_salary', 'overtime',
                 'satisfaction_score', 'commute_distance', 'attrition',
                 'attrition_prob', 'predicted_attrition', 'segment']]

# Save to CSV
export_df.to_csv('workforce_with_ml_results.csv', index=False)
print("\nData exported to 'workforce_with_ml_results.csv'")

# Also save the prediction model and scalers (if needed)
import joblib
joblib.dump(rf, 'attrition_model.pkl')
joblib.dump(scaler_kmeans, 'scaler_kmeans.pkl')
print("Model artifacts saved: 'attrition_model.pkl', 'scaler_kmeans.pkl'")
