import sqlite3
from flask import Flask, request, jsonify, render_template, g
from flask_cors import CORS
from queries import *
app = Flask(__name__)
CORS(app)


####### Database boilerplate
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
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
  result = {}
  cur = get_db().cursor()
  for row in cur.execute(FIND_INVENTORY):
    result[row[0]] = row[1]

  return result

@app.route('/inventory/create', methods = ['POST'])
def create_inventory():
  input_json = request.get_json(force=True)
  if "name" not in input_json:
    return "", 400
    
  cur = get_db().cursor()
  cur.execute(CREATE_INVENTORY, (input_json["name"],))
  get_db().commit()
  return "", 200

@app.route('/inventory/delete', methods = ['DELETE'])
def delete_inventory():
  input_json = request.get_json(force=True)
  if "id" not in input_json:
    return "", 400
    
  cur = get_db().cursor()
  cur.execute(DELETE_INVENTORY, (input_json["id"],))
  get_db().commit()
  return "", 200

@app.route('/inventory/edit', methods = ['PUT'])
def update_inventory():
  input_json = request.get_json(force=True)
  if "name" not in input_json or "id" not in input_json:
    return "", 400
  
  cur = get_db().cursor()
  cur.execute(UPDATE_INVENTORY, (input_json["name"], input_json["id"]))
  get_db().commit()
  return "", 200

@app.route('/warehouse/create', methods = ['POST'])
def create_warehouse():
  input_json = request.get_json(force=True)
  if "name" not in input_json:
    return "", 400
  
  cur = get_db().cursor()
  cur.execute(CREATE_WAREHOUSE, (input_json["name"],))
  get_db().commit()
  return "", 200

@app.route('/warehouse/all', methods = ['GET'])
def view_warehouses():
  result = {}
  cur = get_db().cursor()
  for row in cur.execute(FIND_WAREHOUSE):
    result[row[0]] = row[1]
  return result

@app.route('/inventory/<int:inventory_id>/warehouse', methods = ['GET'])
def view_warehouses_for_inventory(inventory_id):  
  result = {}
  cur = get_db().cursor()
  for row in cur.execute(GET_WAREHOUSE_INFO, (inventory_id,)):
    result[row[0]] = {"warehouse_name": row[1], "count": row[2]}
  return result

@app.route('/inventory/assign_to_warehouse', methods = ['POST'])
def assign_inventory_to_warehouse():
  input_json = request.get_json(force=True)
  if "inventory_id" not in input_json \
    or "warehouse_id" not in input_json \
    or "count" not in input_json:
    return "", 400
  
  cur = get_db().cursor()
  cur.execute(ASSIGN_TO_WAREHOUSE, 
              (input_json["inventory_id"], 
               input_json["warehouse_id"], 
               input_json["count"]))
  get_db().commit()
  return "", 200

@app.route('/')
def index():
  return render_template('index.html')

init_db()
app.run(host='0.0.0.0', port=81)