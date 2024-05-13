from flask import Flask,redirect,url_for,render_template,request
import numpy as np
import pickle
import sklearn
import os

file_path = 'final2.pkl'

if os.path.isfile(file_path):
    print("File exists")
else:
    print("File does not exist")

model = pickle.load(open('final2.pkl', 'rb'))

# Call the 'predict' method on the model
# prediction = model.predict(input_data)

app = Flask(__name__)   

@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/predict',methods = ["POST"])
def home():
    sy0 = request.form['s0']
    
  
    sy0 = float(sy0)
   

    arr = np.array([[sy0]])
    # pred = file_path.predict(arr)
    pred = model.predict(arr)
    return render_template('after.html',data=pred)






if __name__ == '__main__':
    app.run(debug=True)