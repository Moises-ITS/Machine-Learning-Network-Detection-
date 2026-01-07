import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE

#load the training set
df = pd.read_csv('UNSW_NB15_training-set.csv')

#----------------------------------
#TRAINING SETUP
#----------------------------------
X = df.drop(['label', 'attack_cat', 'id'], axis=1, errors="ignore")
y = df['label']

ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_data = ohe.fit_transform(X[['proto', 'service', 'state']])

X_numerical = X.drop(['proto', 'service', 'state'], axis=1).values
X_final = np.hstack((X_numerical, encoded_data))

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_final)

sm = SMOTE(random_state=42)
X_train_res, y_train_res = sm.fit_resample(X_train_scaled, y)

model = RandomForestClassifier(n_estimators=500, max_depth=40, random_state=42, class_weight='balanced')
# Now train the model on the perfectly balanced data
model.fit(X_train_res, y_train_res)
#X_train, X_test, y_train, y_test = train_test_split(X_final, y_encoded, test_size=0.2)

#----------------------------
# TESTING SETUP
#----------------------------
#Load testing csv
df_test = pd.read_csv('UNSW_NB15_testing-set.csv')

X_test_raw = df_test.drop(['label', 'attack_cat', 'id'], axis=1, errors="ignore")
y_test = df_test['label']

X_test_cat = ohe.transform(X_test_raw[['proto', 'service', 'state']])

X_test_num = X_test_raw.drop(['proto', 'service', 'state'], axis=1).values
X_test_final = np.hstack((X_test_num, X_test_cat))
X_test_scaled = scaler.transform(X_test_final)
