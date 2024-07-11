import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from models import db, Contact

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')

db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade
CORS(app)

@app.route('/')
def main():
    return jsonify({ "status": "API Running OK"}), 200

@app.route('/api/contacts', methods=['GET'])
def obtener_contactos():

    def info(contact):
        return {
            "id": contact.id,
            "name": contact.name,
            "phone": contact.phone
        }

    contacts = Contact.query.all() # [<Contact 1>, <Contact 2>]
    contacts = list(map(info, contacts))
    """
    contacts = [{
            "id": contact.id,
            "name": contact.name,
            "phone": contact.phone
        } for contact in contacts]
    """
    #contacts = list(map(lambda contact: contact.serialize() , contacts)) # [{"id": 1, ...}, {"id": 2, ...}]

    return jsonify(contacts)

@app.route('/api/contacts', methods=['POST'])
def crear_contacto():

    contact_info = request.get_json()

    contact = Contact()
    contact.name = contact_info["name"]
    contact.phone = contact_info["phone"]

    db.session.add(contact)
    db.session.commit()

    return jsonify(contact.serialize())

@app.route('/api/contacts/<int:id>', methods=['PUT'])
def actualizar_contacto(id):

    contact_info = request.get_json()

    contact = Contact.query.get(id) # SELECT * FROM contacts WHERE id = ?

    if not contact:
        return jsonify({ "msg": "Contact not found"}), 404

    contact.name = contact_info["name"]
    contact.phone = contact_info["phone"]

    db.session.commit()

    return jsonify(contact.serialize())

@app.route('/api/contacts/<int:id>', methods=['DELETE'])
def eliminar_contacto(id):

    contact = Contact.query.get(id) # SELECT * FROM contacts WHERE id = ?

    if not contact:
        return jsonify({ "msg": "Contact not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({ "status": "Contact deleted successfully"}), 200

if __name__ == '__main__':
    app.run()