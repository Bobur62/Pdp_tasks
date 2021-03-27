from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
# ***********************************
# task1
# def home():
#     return """
#         <h1>Hello, World</h1>
#     """
# ***********************************
# task2
def home():
    return render_template("hello.html")


# task3
@app.route("/family")
def family():
    members = ["Baxtiyorjon", "Nafisaxon", "Botirbek", "Nodiraxon"]
    return render_template("family.html", members=members)


# task4
@app.route("/search")
def search():
    q = request.args.get("q")
    return f"""
    <h1>Hello, {q}</h1>
    """


# task5
@app.route("/img")
def img():
    return """
        <a href="/">Home</><br>
        <img src="/static/images/music.png" width=250>
    """


app.run(host='127.0.0.1', port=8000)
