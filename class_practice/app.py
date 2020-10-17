from flask import Flask, render_template, request
import dataModel

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    This handles Get and Post requests on the root endpoint
    """
    if request.method == "GET":
        return render_template("index.html", message="Welcome!")
    else:
        username = request.form["username"]
        password = request.form["password"]
        db_password = dataModel.check_password(username)
        if password == db_password:
            message = dataModel.show_color(username)
            return render_template("stuff.html", message = message)
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
