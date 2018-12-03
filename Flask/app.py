from flask import Flask, render_template, request
from Crime_Predictor_Predict import predictions
from Crime_Predictor_Model import Crime_Model
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def getInputs():
    return render_template('Flask_Test.html')

@app.route('/result', methods=['GET','POST'])
def result():
    gender = request.form.get("Gender", None)
    age = request.form.get("Age", None)
    crime = request.form.get("Crime", None)
    pop = request.form.get("Pop", None)
    safest = predictions(age, gender, crime, pop)[0]
    worst = predictions(age, gender, crime, pop)[1]

    return render_template('Flask_Test.html', age=age, gender=gender, crime=crime, pop=pop, bestCounties=safest,
                           worstCounty=worst)

if __name__ == '__main__':
    app.run(debug=True)
