# Step 2, import os from standard Python library
import os
# Step 1, import Flask class from flask
from flask import Flask, render_template

"""
# Create instance of Flask and store in variable "app"
# #rgument is __name__ of applications module
# __name__ is builtin Python module
"""
app = Flask(__name__)


# @ = decorator, wraps functions
@app.route("/")
def index():
    """
    # flask can render HTML, but would make web development
    # very complicated
    # return "<h1>Hello,</h1> <h2>World!<h2>"
    """
    # render_template to render HTML, create templates folder in which 
    # index.html is placed << 
    return render_template("index.html")
    

# __main__ = default module in Python
if __name__ == "__main__":
    # These are the arguments that reference os
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        # port needs to be set as an Integer
        port=int(os.environ.get("PORT", "5000")),
        # debug=False when submitting project
        debug=True)