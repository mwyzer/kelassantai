from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/course")
def info_course():
    data = {
        "nama": "Python Fullstack AI Engineer",
        "level": "Pemula",
        "total_pertemuan": 30,
        "modul": ["Flask", "DeepSeek", "Next.js", "Deployment"],
    }
    return jsonify(data)

