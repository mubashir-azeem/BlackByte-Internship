# 🧠 Sentiment Analysis on Amazon Reviews (NLP)

## 📌 Project Overview
This project implements a complete Natural Language Processing (NLP) pipeline to classify Amazon product reviews as **Positive** or **Negative** using TF-IDF and Logistic Regression.

The system processes raw text data, converts it into numerical features, and predicts sentiment while also extracting meaningful insights from customer complaints.

---

## 📊 Dataset
- Source: Amazon Fine Food Reviews (Kaggle)
- Total Reviews: 568,000+
- Features: Text, Score, Summary, User & Product details
- Labels:
  - Positive → 4–5 stars
  - Negative → 1–2 stars
  - Neutral (3 stars) removed

---

## ⚙️ Features & Workflow

### 🔹 Text Preprocessing
- Lowercasing
- Removing HTML & special characters
- Tokenization
- Stopword removal
- Lemmatization

### 🔹 Feature Engineering
- TF-IDF Vectorization
- Unigrams + Bigrams
- Max features = 50,000

### 🔹 Model Training
- Logistic Regression
- Balanced class weights
- Train-test split (80/20)

---

## 📈 Model Evaluation

- Accuracy: ~93%
- ROC-AUC Score: ~0.97
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)

---

## 🔍 Key Insights

- Negative reviews were analyzed to extract complaint keywords
- Common issues identified:
  - Product quality
  - Taste/flavor
  - Packaging problems

---

## ☁️ Visualizations

- Confusion Matrix (Model Performance)
- Word Cloud (Complaint Keywords)

---

## 📁 Project Files

- `sentiment_model.pkl` → Trained model
- `tfidf_vectorizer.pkl` → Text vectorizer
- `confusion_matrix.png` → Model evaluation plot
- `complaint_wordcloud.png` → Complaint visualization
- `notebook.ipynb` → Full implementation

---

## 🚀 How to Use

```python
import joblib

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

text = ["This product is terrible"]
text_vec = vectorizer.transform(text)

prediction = model.predict(text_vec)
print(prediction)
