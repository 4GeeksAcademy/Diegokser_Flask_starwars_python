"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People, Planets, People_favorite, Planets_favorite
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/')
def sitemap():
    return generate_sitemap(app)

@api.route('/user', methods=['GET'])
def usuarios():
    user = User.query.all()
    data = []
    for users in user:
        data.append(users.serialize())

    return jsonify(data), 200

@api.route('/people', methods=['GET'])
def list_people():
    person = People.query.all()
    data = []
    for persona in person:
        data.append(persona.serialize())
    return jsonify(data) , 200 

@api.route('/planets', methods=['GET'])
def list_planets():
    planet= Planets.query.all()
    data = []
    for planetas in planet:
        data.append(planetas.serialize())
    return jsonify(data) , 200 

@api.route('/user/favorites', methods=['GET'])
def get_users():
    people = People_favorite.query.filter_by()
    planet = Planets_favorite.query.filter_by()
    data = []

    for favorito in people:
        data.append(favorito.serialize())
 
    for favorito in planet:
        data.append(favorito.serialize())

    print(data)

    return jsonify(data), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.filter_by(id = people_id).first()
    if not person:
        return jsonify({'message' : 'No se encuentra el personaje'})

    return jsonify(person.serialize()), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    # planet = Planets.query.get(planet_id)
    planet = Planets.query.filter_by(id = planet_id).first()
    if not planet: 
        return jsonify({'message' : 'No se encuentra el planeta'}) 

    return jsonify(planet.serialize()), 200

@api.route('/favorite/planet/<int:planet_id>/<int:id_user>', methods=['POST'])
def add_favorite_planet(planet_id, id_user):
    user = User.query.get(id_user)
    if user:
        favorite = Planets_favorite(id_user=user.id, planet_id=planet_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite planet added successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404
    
@api.route('/favorite/planet/<int:planet_id>/<int:id_user>', methods=['DELETE'])
def delete_planet_favorite(planet_id, id_user):
   user = User.query.get(id_user)
   if user:
        favorite = Planets_favorite.query.filter_by(id_user=user.id, planet_id=planet_id).first()
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite planet was deleted successfully'})
   else:
        return jsonify({'message': 'User not found'}), 404


@api.route('/favorite/people/<int:people_id>/<int:id_user>', methods=['POST'])
def add_favorite_people(people_id, id_user):
    user = User.query.get(id_user)
    if user:
        favorite = People_favorite(id_user=user.id, people_id=people_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite people added successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404
    
@api.route('/favorite/people/<int:people_id>/<int:id_user>', methods=['DELETE'])
def delete_people_favorite(people_id, id_user):
   user = User.query.get(id_user)
   if user:
        favorite = People_favorite.query.filter_by(id_user=user.id, people_id=people_id).first()
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite person was deleted successfully'})
   else:
        return jsonify({'message': 'User not found'}), 404