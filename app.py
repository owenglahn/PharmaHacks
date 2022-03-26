from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="template")

@app.route('/', methods = ["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)