#test for flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def content():
    return "This liujian's website."
if __name__ == "main":
    app.run(host="0.0.0.0", port=80,debug=True)