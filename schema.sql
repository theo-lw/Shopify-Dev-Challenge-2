PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS inventory(
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE IF NOT EXISTS warehouse(
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE IF NOT EXISTS warehouse_inventory(
  warehouse_id INTEGER REFERENCES warehouse ON DELETE CASCADE,
  inventory_id INTEGER REFERENCES inventory ON DELETE CASCADE,
  number INTEGER
);

CREATE INDEX IF NOT EXISTS inventory_index ON warehouse_inventory(inventory_id);