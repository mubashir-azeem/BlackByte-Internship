# 🩺 AI-Powered Doctor Recommendation Chatbot

This project is an AI-based chatbot that recommends doctors based on user symptoms and location using NLP and Machine Learning.

---

## 🚀 Project Overview

The system takes user input (symptoms), processes it using NLP techniques, predicts the required medical specialization, and recommends doctors accordingly.

---

## 🧠 Features

- Symptom-based doctor recommendation  
- NLP using TF-IDF  
- Machine Learning (Logistic Regression)  
- Location-based filtering (Karachi, Lahore, Islamabad)  
- Chat-style web interface using Flask  
- Real-time response generation  

---

## ⚙️ Technologies Used

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- HTML/CSS  

---

## 🧩 How It Works

1. User enters symptoms  
2. Text is converted into numerical form using TF-IDF  
3. ML model predicts specialization  
4. System extracts city from input  
5. Doctors are filtered based on specialization + location  
6. Results are displayed on web interface  

---

## 📊 Dataset

### 1. Symptoms Dataset
Used for training ML model:
- Symptom → Specialization mapping  

### 2. Doctors Dataset
Contains:
- Name  
- Specialization  
- Hospital  
- City  
- Availability  

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/mubashir-azeem/BlackByte-Internship.git

2. Go into the project folder:
```bash
cd "Project - Doctor Recommendation Chatbot System"


3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
python app.py

5. Open in browser:
  http://127.0.0.1:5000/
