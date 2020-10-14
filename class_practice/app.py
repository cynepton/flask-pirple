from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    This handles Get and Post requests on the root endpoint
    """
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        if username == "isaac" and password == "isaac":
            return render_template("index.html", message = "Logged in Successfully")
        else:
            error_message = "Hint: isaac"
            return render_template("index.html", message = error_message)

@app.route("/stuff")
def stuff():
    """
    docstring
    """
    return render_template("stuff.html")

if __name__ == "__main__":
    app.run(port=7000, debug=True)
