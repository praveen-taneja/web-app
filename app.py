from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ffjksjdwejfekfwekfejfekekwefj"

@app.route('/')
def index():
    return render_template("index.html")
# def hello_world():
#     return "hello world!"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    #flash("hi " + str(request.form["fName"]))
    output = "hi " + str(request.form["fName"]) + "!!"
    return render_template("index.html", output=output)