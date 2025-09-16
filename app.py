
from flask import Flask, render_template, request
from joblib import load
import numpy as np

filename = 'diabetes_model.joblib'  # use joblib file extension
classifier = load(filename)  # load model using joblib.load

# Create a Flask app instance
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html',prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = classifier.predict(data)
        print(my_prediction)
        
        return render_template('index.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)