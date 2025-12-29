from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/coral_health_predictor.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get temperature data from form
        temperature = float(request.form['temperature'])
        
        # Prepare data for prediction
        data = [[temperature]]
        
        # Make prediction
        prediction = model.predict(data)[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)