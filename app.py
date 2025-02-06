import pickle
import warnings
from flask import Flask, render_template, request
from sklearn.exceptions import InconsistentVersionWarning

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        temperature = float(request.form.get('temperature'))
        prediction = model.predict([[temperature]])
        output = round(prediction[0], 2)
        print(output)
        print(prediction)
        return render_template('index.html', prediction_text=f'Total Revenue Generated is ${output}')
    except:
        return render_template('index.html', prediction_text=f'Invalid Input')
        
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
