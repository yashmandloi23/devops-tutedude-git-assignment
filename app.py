from flask import request, redirect
from pymongo import MongoClient

client = MongoClient("<your_mongodb_url>")
db = client["todo_db"]
collection = db["items"]


@app.route("/submittodoitem", methods=["POST"])
def submit_todo():

    try:
        name = request.form["itemName"]
        description = request.form["itemDescription"]

        collection.insert_one({
            "itemName": name,
            "itemDescription": description
        })

        return "Item stored successfully"

    except Exception as e:
        return str(e)
