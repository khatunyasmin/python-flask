from flask import Flask ,render_template

app=Flask(__name__)

@app.route('h/')
def index():
    return render_template('finalresm.html')
app.run()