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
  result = [InventoryItem(*row) for row in cur.execute(FIND_INVENTORY)]

  return jsonify(InventoryItem.Schema(many=True).dump(result))

@app.route('/inventory/create', methods = ['POST'])
def create_inventory():
  try:
    input_json = request.get_json(force=True)
    create_request = InventoryCreateRequest.Schema().load(input_json)
  except ValidationError:
    return "Ill-formed request", 400
    
  cur = get_db().cursor()
  cur.execute(CREATE_INVENTORY, (create_request.name,))
  get_db().commit()
  return "", 200

@app.route('/inventory/delete', methods = ['DELETE'])
def delete_inventory():
  try:
    input_json = request.get_json(force=True)
    delete_request = InventoryDeleteRequest.Schema().load(input_json)
  except ValidationError:
    return "Ill-formed request", 400
  
    
  cur = get_db().cursor()
  cur.execute(DELETE_INVENTORY, (delete_request.id,))
  get_db().commit()
  return "", 200

@app.route('/inventory/edit', methods = ['PUT'])
def update_inventory():
  try:
    input_json = request.get_json(force=True)
    edit_request = InventoryUpdateRequest.Schema().load(input_json)
  except ValidationError:
    return "Ill-formed request", 400
  
  cur = get_db().cursor()
  cur.execute(UPDATE_INVENTORY, (edit_request.name, edit_request.id))
  get_db().commit()
  return "", 200

@app.route('/warehouse/create', methods = ['POST'])
def create_warehouse():
  try:
    input_json = request.get_json(force=True)
    create_request = WarehouseCreateRequest.Schema().load(input_json)
  except ValidationError:
    return "Ill-fomred request", 400
  
  cur = get_db().cursor()
  cur.execute(CREATE_WAREHOUSE, (create_request.name,))
  get_db().commit()
  return "", 200

@app.route('/warehouse/all', methods = ['GET'])
def view_warehouses():
  cur = get_db().cursor()
  result = [Warehouse(*row) for row in cur.execute(FIND_WAREHOUSE)]

  return jsonify(Warehouse.Schema(many=True).dump(result))

@app.route('/warehouse/<int:warehouse_id>/inventory', methods=['GET'])
def view_inventory_for_warehouse(warehouse_id):
  cur = get_db().cursor()
  result = [InventoryForWarehouse(*row) for row in cur.execute(GET_INVENTORY_IN_WAREHOUSE, (warehouse_id,))]

  return jsonify(InventoryForWarehouse.Schema(many=True).dump(result))

@app.route('/inventory/<int:inventory_id>/warehouse', methods = ['GET'])
def view_warehouses_for_inventory(inventory_id):  
  cur = get_db().cursor()
  result = [WarehouseInventory(*row) for row in cur.execute(GET_WAREHOUSE_INFO, (inventory_id,))]
    
  return jsonify(WarehouseInventory.Schema(many=True).dump(result))

@app.route('/inventory/assign_to_warehouse', methods = ['POST'])
def assign_inventory_to_warehouse():
  try:
    input_json = request.get_json(force=True)
    assign_request = AssignToWarehouseRequest.Schema().load(input_json)
  except ValidationError:
    return "Ill-formed request", 400
  
  cur = get_db().cursor()
  cur.execute(ASSIGN_TO_WAREHOUSE, 
              (assign_request.inventory_id, 
               assign_request.warehouse_id, 
               assign_request.number))
  get_db().commit()
  return "", 200

@app.route('/')
def index():
  return render_template('index.html')

init_db()
app.run(host='0.0.0.0', port=81)