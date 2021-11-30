"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, flash, redirect, session, jsonify
from models import db, connect_db, Cupcake
 
from flask_debugtoolbar import DebugToolbarExtension
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
 
app.config['SECRET_KEY'] = 'trisolarian879'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
 
connect_db(app)

@app.route('/')
def homepage():
    """Homapage"""
    return render_template('homepage.html')

@app.route('/api/cupcakes')
def get_cupcakes():
    """API request for all cupcakes"""

    cc = [cup_cake.serialize() for cup_cake in Cupcake.query.all()]

    return (jsonify(cupcakes=cc), 200)

@app.route('/api/cupcakes/<int:id>')
def get_single_cupcake(id):
    """Get single cupcake"""

    cake = Cupcake.query.get_or_404(id)
    return (jsonify(cupcake=cake.serialize()), 200)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create new cupcake"""

    cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'])

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)



@app.route('/api/cupcakess', methods=['POST'])
def create_user_cupcake():
    """Create new cupcake with submission from user"""

    cupcake = Cupcake(flavor=request.form['flavor'], size=request.form['size'], rating=request.form['rating'], image=request.form['image'])

    db.session.add(cupcake)
    db.session.commit()

    return redirect('/')


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Update cupcake """
    cupcake = Cupcake.query.get_or_404(id)

    #update cupcake
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 200)

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Delete cupcake"""
    cake = Cupcake.query.get_or_404(id)

    db.session.delete(cake)
    db.session.commit()

    return (jsonify(message="Deleted"), 200)