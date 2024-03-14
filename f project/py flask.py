from flask import Flask ,render_template

app=Flask(__name__)

@app.route("/")
def hello():
    name="Yasmin"
    return render_template("index.html",x1=name)

@app.route("/about")
def hi():
    name2="Subhu"
    return render_template("about.html",x2=name2)
@app.route("/form")
def h():
    return render_template("form.html")




app.run()