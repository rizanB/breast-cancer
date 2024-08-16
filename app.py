from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>hello</h2>"

if __name__ == "__main__":
    app.run(debug=True)