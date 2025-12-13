# notebooks/accident_severity_model.py
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# ---------- CONFIG ----------
DATA_PATH = 'Road_Accident_Analysis/data/Road accident.csv'   # ensure your CSV is at this path
TARGET_COL = 'Accident_Severity'
FEATURE_COLS = [
    'Day_of_Week','Junction_Control','Junction_Detail','Light_Conditions',
    'Local_Authority_(District)','Carriageway_Hazards','Road_Surface_Conditions',
    'Road_Type','Urban_or_Rural_Area','Weather_Conditions','Vehicle_Type',
    'Number_of_Casualties','Number_of_Vehicles','Speed_limit'
]
OUT_DIRS = ['models','visuals']
for d in OUT_DIRS:
    os.makedirs(d, exist_ok=True)

# ---------- LOAD ----------
print("Loading data...")
df = pd.read_csv(DATA_PATH)
df = df.dropna(subset=[TARGET_COL])
df[TARGET_COL] = df[TARGET_COL].astype(str).str.strip()   # normalize

# ---- NEW: fix small label typo ----
# Merge 'Fetal' into 'Fatal' if typo exists
if 'Fetal' in df[TARGET_COL].unique():
    print("Found 'Fetal' label - merging into 'Fatal'")
df[TARGET_COL] = df[TARGET_COL].replace({'Fetal': 'Fatal'})

# Cast numeric columns
for col in ['Number_of_Casualties','Number_of_Vehicles','Speed_limit']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# ---- NEW: group low-frequency Local_Authority values ----
RARE_THRESHOLD = 50
if 'Local_Authority_(District)' in df.columns:
    vc = df['Local_Authority_(District)'].value_counts(dropna=False)
    if len(vc) > 40:  # heuristic: only group when many unique values
        rare = vc[vc <= RARE_THRESHOLD].index
        if len(rare) > 0:
            print(f"Grouping {len(rare)} low-frequency Local_Authority values into 'Other' (threshold={RARE_THRESHOLD})")
            df['Local_Authority_(District)'] = df['Local_Authority_(District)'].where(~df['Local_Authority_(District)'].isin(rare), 'Other')

X = df[FEATURE_COLS].copy()
y = df[TARGET_COL]

# ---------- SPLIT ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("Train / Test sizes:", X_train.shape, X_test.shape)

# ---------- PREPROCESS ----------
cat_cols = X_train.select_dtypes(include=['object','category']).columns.tolist()
num_cols = X_train.select_dtypes(include=['number']).columns.tolist()
print("Categorical cols:", cat_cols)
print("Numeric cols:", num_cols)

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('ohe', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

pre = ColumnTransformer([
    ('cat', cat_pipe, cat_cols),
    ('num', num_pipe, num_cols)
])

# ---------- MODEL ----------
# UPDATED: use class_weight to handle imbalance
rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1, class_weight='balanced')
pipe = Pipeline([('pre', pre), ('rf', rf)])

# ---------- TRAIN ----------
print("Fitting model...")
pipe.fit(X_train, y_train)

# ---------- PREDICT & METRICS ----------
y_pred = pipe.predict(X_test)
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print("Test accuracy:", acc)
print(report)

# ---------- SAVE MODEL ----------
model_path = os.path.join('models','severity_model.pkl')
joblib.dump(pipe, model_path)
print("Saved model to", model_path)

# ---------- SAVE CONFUSION MATRIX ----------
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted'); plt.ylabel('Actual'); plt.title('Confusion Matrix')
plt.tight_layout()
plt.savefig(os.path.join('visuals','confusion_matrix.png'))
plt.close()
print("Saved confusion matrix to visuals/confusion_matrix.png")

# ---------- FEATURE IMPORTANCES (mapped to OHE names) ----------
ohe = pipe.named_steps['pre'].named_transformers_['cat'].named_steps['ohe']
cats = ohe.categories_
feature_names = []
for col, cats_list in zip(cat_cols, cats):
    feature_names.extend([f"{col}__{c}" for c in cats_list])
feature_names.extend(num_cols)

importances = pipe.named_steps['rf'].feature_importances_
# If lengths match map them, else fallback to raw indices
if len(importances) == len(feature_names):
    feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False)
else:
    feat_imp = pd.Series(importances).sort_values(ascending=False)

# Plot top 20 feature importances
top_n = min(20, len(feat_imp))
plt.figure(figsize=(8, top_n*0.4 + 1))
feat_imp.head(top_n).sort_values().plot(kind='barh')
plt.title('Top Feature Importances')
plt.tight_layout()
plt.savefig(os.path.join('visuals','feature_importances.png'))
plt.close()
print("Saved feature importances to visuals/feature_importances.png")

# ---------- SAMPLE PREDICTIONS ----------
sample_out = X_test.copy()
sample_out['y_true'] = y_test.values
sample_out['y_pred'] = y_pred
sample_out.to_csv(os.path.join('visuals','sample_predictions.csv'), index=False)
print("Saved sample predictions to visuals/sample_predictions.csv")

# ---------- SAVE REPORTS ----------
with open(os.path.join('visuals','classification_report.txt'), 'w') as f:
    f.write(f"Accuracy: {acc}\n\n")
    f.write(report)
# Also save aggregated top features (group by original column)
grouped = feat_imp.groupby(lambda x: x.split('__')[0]).sum().sort_values(ascending=False)
grouped.head(10).to_csv(os.path.join('visuals','top_features_by_column.csv'))

print("All outputs saved. Done.")
