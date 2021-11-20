from flask import Flask, render_template, request
from transform_for_prediction import *
import pickle

app = Flask(__name__)
model = pickle.load(open('support_vector_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])


def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])

def predict():
    
    if request.method == 'POST':
        
        name = request.form['cn']
        year = int(request.form['yr'])
        avg_price = float(request.form['avg_price'])/10000
        kilometers = float(request.form['milage'])*1.60934
        fuel = str(request.form['fuel'])
        seller = str(request.form['seller'])
        transmission = str(request.form['trans'])
        owners = int(request.form['owner'])
        
        name = name.replace("_", " ")
        
        transform = transform_for_prediction(name,year,avg_price,kilometers,fuel,seller,transmission,owners)
        
        prediction = model.predict(transform)
        
        output_num = round(prediction[0]*10000, 2)
        
        output = "{:.2f}".format(output_num)
        
        return render_template('result.html', recommendation = output)
                        
    else:
        
        return render_template('index.html')

if __name__=="__main__":
    
    app.run(debug=True)

