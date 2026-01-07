from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
#---------------------------------------
#PREDICTIONS
#---------------------------------------
predictions = model.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
print(classification_report(y_test, predictions))

#-----------------------------------------
#Paranoid Mode
#-----------------------------------------
# 1. Get the probabilities instead of the final 0/1 choice
# This gives two columns: [Prob of 0, Prob of 1]
probabilities = model.predict_proba(X_test_scaled)[:, 1]

# 2. Lower the threshold from 0.5 to 0.3
# "If you're 30% sure it's an attack, flag it."
paranoid_predictions = (probabilities > 0.3).astype(int)

# 3. Check the new Confusion Matrix
new_cm = confusion_matrix(y_test, paranoid_predictions)
print("New Confusion Matrix (Paranoid Mode):")
print(new_cm)

#-------------------------------------------------
#Feature Importance(Most important features for consideration)
#-------------------------------------------------
num_col_names = X.drop(['proto', 'service', 'state'], axis=1).columns.tolist()

ohe_col_names = ohe.get_feature_names_out(['proto', 'service', 'state']).tolist()
full_feature_names = num_col_names + ohe_col_names

featureImportance = pd.Series(model.feature_importances_, index=full_feature_names)
featureImportance.nlargest(10).plot(kind='barh', color='skyblue')
plt.xlabel("Importance Score")
plt.title("Most Important Features for Detecting Malicious Packets")
plt.tight_layout()
plt.show()


#-----------------------------------------
#Confusion Matrix(False Positives/Negatives)
#-----------------------------------------

cm = confusion_matrix(y_test, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Normal', 'Attack'])
disp.plot(cmap="Blues", values_format='.2f')
plt.show()
