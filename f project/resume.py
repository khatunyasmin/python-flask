from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Yasmin Khatun ",
    "title": "Web Developer",
    "bio": "I am a passionate web developer.",
    "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript"],
    "contact": {
        "email": "yasminkhatun8270@gmail.com",
        "phone": "+91 7735919392",
    },
}

@app.route('/')
def index():
    return render_template('resume.html', profile=profile)

app.run()





#if __name__ == '__main__':
#if __name__ == '_main_':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)"""
#app.run(debug=True,port=8000)