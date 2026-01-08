# Machine-Learning-Network-Detection-
Project Overview: A Machine Learning pipeline designed to identify malicious network traffic in a modern office environment using the UNSW-NB15 dataset.
This project moves beyond legacy datasets (like KDD99) to address contemporary threats like Fuzzers and Backdoors.
Key Features:

Preprocessing: Implemented One-Hot Encoding for protocols and StandardScaler for traffic metrics.

Imbalance Handling: Utilized class_weight='balanced' and custom probability thresholds to reduce False Negatives.

Explainability: Integrated Feature Importance mapping to identify high-risk network behaviors.

Results:

Recall: 87% (Standard) / 91% (Paranoid Mode)

Top Predictors: sttl, ct_state_ttl, sbytes

***View Images for Standard and Paranoid Matrix Charts***
