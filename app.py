"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = '123ABC'


# ******************** CUPCAKE ROUTES ********************
@app.route("/")
def homepage():
    """Render homepage template."""
    cupcakes = Cupcake.query.all()
    return render_template("base.html", cupcakes=cupcakes)

@app.route("/api/cupcakes")
def cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcakes)


@app.route("/api/cupcakes/<int:id>")
def cupcake_detail(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    
    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json["image"]
    )

    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(new_cupcake=new_cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def edit_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor=request.json["flavor"],
    cupcake.size=request.json["size"],
    cupcake.rating=request.json["rating"],
    cupcake.image=request.json["image"]

    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='deleted')
