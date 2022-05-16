FIND_INVENTORY = """
SELECT inventory.id, inventory.name FROM inventory 
"""

CREATE_INVENTORY = """
INSERT INTO inventory (name) VALUES (?)
"""

DELETE_INVENTORY = """
DELETE FROM inventory WHERE id = ?
"""

UPDATE_INVENTORY = """
UPDATE inventory SET name = ? WHERE id = ?
"""

FIND_WAREHOUSE = """
SELECT warehouse.id, warehouse.name FROM warehouse
"""

CREATE_WAREHOUSE = """
INSERT INTO warehouse (name) VALUES (?)
"""

ASSIGN_TO_WAREHOUSE = """
INSERT INTO warehouse_inventory (inventory_id, warehouse_id, number) VALUES (?, ?, ?)
"""

GET_WAREHOUSE_INFO = """
SELECT warehouse.id, warehouse.name, warehouse_inventory.number 
FROM warehouse_inventory INNER JOIN warehouse
ON warehouse_inventory.warehouse_id = warehouse.id
WHERE warehouse_inventory.inventory_id = ?
"""
