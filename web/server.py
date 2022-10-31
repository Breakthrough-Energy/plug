from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


@app.get("/create")
def create():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(port=5000)
