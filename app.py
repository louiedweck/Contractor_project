from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/')
def hello():
    client = MongoClient()
    db = client['test']
    collection = db.collection
    return"Results:" + str(list(collection.find({})))


if __name__ == '__main__':
    app.run(debug=True)
