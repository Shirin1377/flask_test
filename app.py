from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/shirin")
def shirin():
    return "hello shirin"

if __name__ == '__main__':
    app.run(debug=True)
