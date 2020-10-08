from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """
    Function description goes here
    """
    return render_template("index.html")

@app.route("/stuff")
def stuff():
    """
    docstring
    """
    return render_template("stuff.html")

if __name__ == "__main__":
    app.run(port=7000, debug=True)