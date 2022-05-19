FIND_INVENTORY = """
SELECT inventory.id, inventory.name, city.id, city.name, city.longitude, city.latitude 
FROM inventory INNER JOIN city ON inventory.city_id = city.id
"""

CREATE_INVENTORY = """
INSERT INTO inventory (name, city_id) VALUES (?, ?)
"""

DELETE_INVENTORY = """
DELETE FROM inventory WHERE id = ?
"""

UPDATE_INVENTORY = """
UPDATE inventory SET name = ?, city_id = ? WHERE id = ?
"""

FIND_CITY = """
SELECT city.id, city.name, city.longitude, city.latitude FROM city
"""

CREATE_CITY = """
INSERT INTO city (name, longitude, latitude) VALUES (?, ?, ?)
"""