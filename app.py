from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_heroku import Heroku
import os


app = Flask(__name__)
CORS(app)
heroku= Heroku(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ownjrnnrtuewjp:71d637c09fea04c14a19c71bf0bc926d72e26f2feeaa777fe35d4b1ed9bd03a3@ec2-18-235-97-230.compute-1.amazonaws.com:5432/de4p79630f2pi5"


class BidInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    surfaceArea = db.Column(db.Integer, nullable=False)
    bid = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, surfaceArea, bid):
        self.name = name
        self.surfaceArea = surfaceArea
        self.bid = bid

@app.route("/ark/input/post", methods =["POST"])
def add_post():
    if request.content_type == "application/json":
        post_data = request.get_json()
        name = post_data.get("name")
        surfaceArea = post_data.get("surfaceArea")
        bid = post_data.get("bid")
        record = BidInfo(name, surfaceArea, bid)
        db.session.add(record)
        db.session.comit()
        return jsonify("Data Posted")
    return jsonify("Error:request must be sent as Json Data")

if __name__== "__main__":
    app.debug = True
    app.run()
