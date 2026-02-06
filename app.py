from flask import Flask
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return "Flask API is running. Visit /api"

@app.route("/api")
def get_data():
    file_path = os.path.join(BASE_DIR, "data.json")

    with open(file_path, "r") as file:
        students = json.load(file)

    html = """
    <h2>Student Grades</h2>
    <table border="1" cellpadding="8">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Grade</th>
        </tr>
    """

    for s in students:
        html += f"""
        <tr>
            <td>{s['id']}</td>
            <td>{s['name']}</td>
            <td>{s['grade']}</td>
        </tr>
        """

    html += "</table>"

    return html


if __name__ == "__main__":
    app.run(debug=True)
