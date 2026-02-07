from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
# replace <your_mongodb_url> with your actual MongoDB Atlas connection string

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("<your_mongodb_url>")
db = client["student_db"]
collection = db["students"]


# Form page
@app.route("/")
def form():
    return render_template("temmplate/todo.html")


# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():

    try:
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        # Insert into MongoDB
        collection.insert_one({
            "name": name,
            "email": email,
            "age": age
        })

        # Redirect on success
        return redirect("/success")

    except Exception as e:
        # Show error on same page
        return render_template("form.html", error=str(e))


# Success page
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
