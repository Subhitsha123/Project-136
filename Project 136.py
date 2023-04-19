from flask import Flask, jsonify, request
import csv

df = []

with open('bright_stars.csv','r') as f:
  csvreader = csv.reader(f)
  for i in csvreader:
    if i != []:
      df.append(i)

headers = df[0]
headers[0] = "Index"
data = df[1:]

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
    }), 200

@app.route("/star")
def stars_data():
    name = request.args.get("name")
    modi_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": modi_data,
    }), 200

if __name__ == "__main__":
    app.run()