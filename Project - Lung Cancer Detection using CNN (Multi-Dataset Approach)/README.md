Lung Cancer Detection using CNN

This project implements a deep learning model for lung cancer detection using medical images. It combines multiple datasets and uses transfer learning to achieve high accuracy while also providing visual explanations using Grad-CAM.

🔹 What was done
Combined multiple datasets (Chest X-ray + IQ-OTH)
Converted data into binary classification (normal vs malignant)
Applied preprocessing:
Resizing (224×224)
Normalization
Data augmentation


🔹 Models Used
Custom CNN (baseline)
Transfer Learning with ResNet50
3-phase training:
Frozen base training
Partial fine-tuning
Full fine-tuning (low learning rate)


🔹 Techniques Applied
Early stopping (prevent overfitting)
Learning rate scheduling
Class imbalance handling (class weights)


🔹 Results
Achieved ~96% validation accuracy
Stable and well-generalized model
Balanced performance across classes


🔹 Explainability
Used Grad-CAM to visualize:
Important regions in lung images
Model decision areas


🔹 Project Highlights
Multi-dataset approach
Transfer learning + fine-tuning
Medical image classification
Explainable AI (Grad-CAM)
