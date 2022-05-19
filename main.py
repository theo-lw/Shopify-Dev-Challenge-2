import sqlite3
from flask import Flask, request, jsonify, render_template, g
from flask_cors import CORS
from marshmallow.exceptions import ValidationError
from queries import *
from classes import *
app = Flask(__name__)
CORS(app)

####### Database boilerplate
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.cursor().execute("PRAGMA foreign_keys = ON")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    
####### Routes
@app.route('/inventory/all')
def list_inventory():
  cur = get_db().cursor()
  city_creator = CityCreator()
  result = [InventoryItem(row[0], row[1], city_creator.create_city(*row[2:])) for row in cur.execute(FIND_INVENTORY)]

  return jsonify(InventoryItem.Schema(many=True).dump(result))

@app.route('/inventory/create', methods = ['POST'])
def create_inventory():
  try:
    input_json = request.get_json(force=True)
    create_request = InventoryCreateRequest.Schema().load(input_json)
  except ValidationError as e:
    return str(e), 400
    
  cur = get_db().cursor()
  cur.execute(CREATE_INVENTORY, (create_request.name, create_request.city_id))
  get_db().commit()
  return "", 200

@app.route('/inventory/delete', methods = ['DELETE'])
def delete_inventory():
  try:
    input_json = request.get_json(force=True)
    delete_request = InventoryDeleteRequest.Schema().load(input_json)
  except ValidationError as e:
    return str(e), 400
    
  cur = get_db().cursor()
  cur.execute(DELETE_INVENTORY, (delete_request.id,))
  get_db().commit()
  return "", 200

@app.route('/inventory/edit', methods = ['PUT'])
def update_inventory():
  try:
    input_json = request.get_json(force=True)
    edit_request = InventoryUpdateRequest.Schema().load(input_json)
  except ValidationError as e:
    return str(e), 400
  
  cur = get_db().cursor()
  cur.execute(UPDATE_INVENTORY, (edit_request.name, edit_request.city_id, edit_request.id))
  get_db().commit()
  return "", 200

@app.route('/city/create', methods = ['POST'])
def create_warehouse():
  try:
    input_json = request.get_json(force=True)
    create_request = CityCreateRequest.Schema().load(input_json)
  except ValidationError as e:
    return str(e), 400
  
  cur = get_db().cursor()
  cur.execute(CREATE_CITY, (create_request.name, create_request.longitude, create_request.latitude))
  get_db().commit()
  return "", 200

@app.route('/city/all', methods = ['GET'])
def view_warehouses():
  cur = get_db().cursor()
  city_creator = CityCreator()
  result = [city_creator.create_city(*row) for row in cur.execute(FIND_CITY)]

  return jsonify(City.Schema(many=True).dump(result))
  
@app.route('/')
def index():
  return render_template('index.html')

init_db()
app.run(host='0.0.0.0', port=81)