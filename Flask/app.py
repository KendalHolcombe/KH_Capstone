from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def dropdown():
    gender = request.form.get("Gender", None)
    age = request.form.get("Age", None)
    return render_template('Flask_Test.html', age=age, gender=gender)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)
