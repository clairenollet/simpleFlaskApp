from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update", methods=['POST'])
def update():
    bpm = request.form["bpm"]
    print(bpm)
    return redirect(url_for("home"))