from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#using panadas so can handle my dataset(csv) files, numpy for operations.
#Tfidvectorizer to convert text to number and assign the importance to each word.
#sklearn for training test and imported logistic regression as it is classfication problem to prdict the specilization.
#using flask for my webapp and render to display and connect with my html page and request to send and take input of symtom from the web page form.



app = Flask(__name__)


# added 2 datasets one is for training (symptoms) and other is for doctors info
symptoms_data = pd.read_csv('symptoms.csv')
doctors = pd.read_csv('doctors.csv')


# taking symptom column as input and specialization as output
X = symptoms_data['Symptom']
y = symptoms_data['Specialization']

# converted text into numbers using tfidf so model can understand it and see/assign the weightage of the text.
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# training model so it can predict specialization from symptoms
model = LogisticRegression()
model.fit(X_vectorized, y)




# To check if user mentioned any city in input or not.
def extract_city(text):
    text = text.lower()
    if "karachi" in text:
        return "Karachi"
    elif "lahore" in text:
        return "Lahore"
    elif "islamabad" in text:
        return "Islamabad"
    return None




# to perform the predictions and filter doc to provide output.
def recommend_doctor(user_input):
    
    input_vector = vectorizer.transform([user_input])
    predicted_specialization = model.predict(input_vector)[0]
    
    # getting city from user input
    city = extract_city(user_input)
    
    # filtering doctors based on specialization
    filtered = doctors[doctors['Specialization'] == predicted_specialization]
    
    # if city is provided then filter by city as well
    if city:
        filtered = filtered[filtered['City'] == city]
    
    # if no doctor found
    if filtered.empty:
        return f"No doctors found for {predicted_specialization} in {city}"
    
    # preparing final response to show on screen
    result = f"Specialist: {predicted_specialization}\n\nDoctors:\n"
    
    for _, row in filtered.iterrows():
        result += f"- {row['Name']} ({row['Hospital']}, {row['City']})\n"
    
    return result





# main route where user input is taken and response is shown
@app.route('/', methods=['GET', 'POST'])
def home():
    
    chat = []
    
    if request.method == 'POST':
        user_input = request.form['symptoms']
        
        # checking if user entered something
        if user_input.strip():
            bot_response = recommend_doctor(user_input)
            
            chat.append(("You", user_input))
            chat.append(("Bot", bot_response))
        else:
            chat.append(("Bot", "Please enter symptoms"))
    
    return render_template('index.html', chat=chat)


# running the flask app
if __name__ == '__main__':
    app.run(debug=True)
