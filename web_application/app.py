import joblib
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model and preprocessing objects
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST", "GET"])
def predict():

    if request.method == 'POST':

        # Get user input from the form
        age = int(request.form.get('age'))
        undergrad = int(request.form.get('course'))  # Assuming this is now a single selection
        nationality = int(request.form.get('origin'))  # Assuming this is now a single selection
        gender = int(request.form.get('gender'))
        hours_of_work = float(request.form.get('hour'))
        marital_status = int(request.form.get('status'))
    
        user = [age, undergrad, hours_of_work, gender, nationality, marital_status]
        data = [np.array(user)]
    
        # Make predictions using the model
        prediction = model.predict(data)

    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
