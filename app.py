from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/get-data")
def get_data():
    return jsonify({
        "data": data
    })

@app.route("/find-star")
def find_star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data
    })

if (__name__ == "__main__"):
    app.run(debug=True)