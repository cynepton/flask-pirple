from flask import Flask, render_template

app = Flask(__name__)


@app.route("/about", methods=["GET"])
def home():
    """
    Function description goes here
    """
    return render_template("about_us.html", title="About Us")

if __name__ == "__main__":
    app.run(debug=True)