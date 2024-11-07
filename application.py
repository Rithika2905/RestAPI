from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

    def __repr__(self):
        return f"{self.username} - {self.email}"

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return("api")

@app.route('/people')
def get_people():
    people_list = User.query.all()
    output=[]
    for people in people_list:
        data = {"name":people.username, "email":people.email}
        output.append(data)

    return jsonify({"registered_people" : output})

@app.route('/people/<int:id>')
def get_peopleid(id):
    people = User.query.get_or_404(id)
    return jsonify({"name":people.username, "email":people.email})

@app.route('/people', methods =["POST"])
def add_people():
    people = User(username = request.json['name'], email = request.json['email'])
    db.session.add(people)
    db.session.commit()
    return jsonify({"id": people.id})

@app.route('/people/<id>', methods=["DELETE"])
def delete(id):
    people = User.query.get(id)
    if people is None:
        return "error found"
    db.session.delete(people)
    db.session.commit()
    return "deleted"