from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """
    This returns an HTML with content:
    Hello World!
    """
    return("<body><h1>Hello World!<h1><body>")

if __name__ == "__main__":
    app.run(debug=True)
