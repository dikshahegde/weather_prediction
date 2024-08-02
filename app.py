from flask import Flask, render_template, request
import pickle
import numpy as np
import logging


# Load the model
model = pickle.load(open('new.pkl', 'rb'))

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict_weather():
    try:
        # Retrieve input data from the form
        precipitation = float(request.form.get('precipitation'))
        temp_max = float(request.form.get('temp_max'))
        temp_min = float(request.form.get('temp_min'))
        wind = float(request.form.get('wind'))
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        
        # Prepare input data for prediction
        input_data = np.array([precipitation, temp_max, temp_min, wind, year, month]).reshape(1, 6)
        
        # Make prediction using loaded model
        result = model.predict(input_data)[0]
        #if result[0]==0:
            #result='Drizzle'
       # if result[0]==1:
           # result='Fog'
        #if result[0]==2:
          #  result='Rainy'
        #if result[0]==3:
           # result='Snow'
        #if result[0]==4:
           # result='Sunny'
        weather_conditions = {0: 'Drizzle', 1: 'Fog', 2: 'Rainy', 3: 'Snow', 4: 'Sunny'}
        result_text = weather_conditions.get(result, "Unknown")
        
        return render_template('index.html',result=result_text)
    
    except Exception as e:
        return str(e)    
        # Return the predicted result as a string
        #return str(result[0])
    
if __name__ == '__main__':
    app.run(debug=True)
