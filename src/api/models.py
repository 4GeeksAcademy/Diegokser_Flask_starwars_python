from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People (db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    appearances = db.Column(db.String(50), nullable=False)
    locations = db.Column(db.String(20))
    gender = db.Column(db.String(50))
    dimensions = db.Column(db.String(50))
    species = db.Column(db.String(50))
    weapons = db.Column(db.String(50))

    def __repr__(self):
        return f'<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "appearances": self.appearances,
            "locations": self.locations,
            "gender": self.gender,
            "dimensions": self.dimensions,
            "species": self.species,
            "weapons": self.weapons
        }
    

class People_favorite (db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    
    
    def __repr__(self):
        return f'<People_favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "people_id": self.people_id,
        }

class Planets (db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    appearances = db.Column(db.String(150), nullable=False)
    affiliations = db.Column(db.String(150))
    climate = db.Column(db.String(150))
    terrain = db.Column(db.String(150))
    creature = db.Column(db.String(150))
    species = db.Column(db.String(150))
    vehicles = db.Column(db.String(150))
    weapons = db.Column(db.String(50))
    
    def __repr__(self):
        return f'<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "appearances": self.appearances,
            "affilitaions": self.affiliations,
            "climate": self.climate,
            "terrain": self.terrain,
            "creature": self.creature,
            "species": self.species,
            "vehicles": self.vehicles,
            "weapons": self.weapons
        }
    
class Planets_favorite (db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    
    def __repr__(self):
        return f'<Planets_favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "planet_id": self.planet_id,
        }