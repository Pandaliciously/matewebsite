from flask import Flask, render_template

app = Flask("TouchGrass", template_folder="templates")

@app.route("/")
def home():
    return  render_template("1.html")

@app.route("/foo")
def foo():
    return render_template("2.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1:5000")