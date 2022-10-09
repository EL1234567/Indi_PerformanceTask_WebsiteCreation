from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/About")
def about():
    return render_template("About.html")


@app.route("/symptoms")
def contact():
    return render_template("symptoms.html")


@app.route("/prevention")
def treatment():
    return render_template("prevention.html")

if __name__ == "__main__":
    app.run(debug=True)