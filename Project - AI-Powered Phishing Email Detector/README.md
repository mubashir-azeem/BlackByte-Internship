# 🔐 AI-Powered Phishing Email Detector (Hybrid ML + Rule-Based System)

## 📌 Project Overview

This project presents a **hybrid phishing email detection system** that combines **Natural Language Processing (NLP)**, **Machine Learning**, and **rule-based cybersecurity techniques**.

The system analyzes email content, extracts both textual and behavioral features, and generates a **phishing probability score (0–1)** along with a **risk classification (SAFE / MEDIUM / HIGH)**.

---

## 🎯 Objective

The main objective is to:

* Detect phishing emails using AI techniques
* Identify suspicious patterns such as malicious URLs and urgency language
* Combine ML predictions with rule-based logic for improved accuracy and explainability

---

## ⚙️ Technologies & Libraries Used

* Python
* Pandas, NumPy
* Scikit-learn (TF-IDF, Random Forest)
* NLTK (text preprocessing)
* Regex (URL extraction)
* SciPy (feature combination using `hstack`)
* Matplotlib & Seaborn (visualization)

---

## 🧠 Model Architecture

### 🔹 Text Processing:

* TF-IDF Vectorizer

  * `max_features=30000`
  * `ngram_range=(1,2)`

### 🔹 Machine Learning Model:

* Random Forest Classifier

  * `n_estimators=300`
  * `class_weight='balanced'`

### 🔹 Hybrid Scoring:

* 70% → ML Model Probability
* 30% → Rule-Based Score

---

## 🔍 Feature Engineering

The system extracts key phishing indicators:

### 🌐 URL Features:

* Number of URLs (`url_count`)
* Detection of IP-based URLs (`has_ip_url`)
* Average URL length (`url_len_avg`)
* Suspicious domains (`.xyz`, `.tk`, `.ml`, `.ga`)

### 🚨 Linguistic Signals:

* Urgency words (e.g., "urgent", "now")
* Threat words (e.g., "suspended", "blocked")
* Reward words (e.g., "free", "won")

---

## ⚖️ Rule-Based System

A rule engine with 6 rules:

* IP-based URL detection
* Multiple URLs
* Suspicious domain extensions
* Urgency language
* Threat language
* Reward/bait language

Each rule contributes to a normalized score between **0 and 1**.

---

## 🎯 Prediction Output

For any input email, the system returns:

* 🔢 Phishing Probability Score (0.0 – 1.0)
* 🚦 Risk Level:

  * HIGH RISK (≥ 0.75)
  * MEDIUM RISK (0.50 – 0.74)
  * SAFE (< 0.50)
* 📊 Number of rules triggered

---

## 📊 Model Evaluation

* Confusion Matrix Visualization
* Precision, Recall, F1 Score
* ROC-AUC Score

📈 The model achieves:

* High accuracy
* Zero false positives (strong reliability)
* Good phishing detection performance

---

## 🧪 Testing

The system is tested on:

* Dataset test split
* Custom real-world email samples:

  * Phishing emails
  * Legitimate emails
  * Borderline cases

---

## 💾 Saved Files

* `phishing_classifier.pkl` → Trained Random Forest model
* `phishing_tfidf.pkl` → TF-IDF vectorizer
* `phishing_confusion_matrix.png` → Evaluation result

---

## 🚀 Key Highlights

* Hybrid AI + Cybersecurity approach
* Combines NLP + feature engineering
* Explainable predictions using rules
* Real-world phishing simulation

---

## 📌 Future Improvements

* Integration with real-time email systems
* Deep learning models (LSTM / BERT)
* URL reputation APIs

---

Developed as part of an NLP + Cybersecurity project, focusing on building an explainable and practical phishing detection system.
