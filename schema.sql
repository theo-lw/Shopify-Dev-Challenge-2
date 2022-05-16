CREATE TABLE IF NOT EXISTS inventory(
  id INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS warehouse(
  id INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS warehouse_inventory(
  warehouse_id INTEGER REFERENCES warehouse ON DELETE CASCADE,
  inventory_id INTEGER REFERENCES inventory ON DELETE CASCADE,
  number INTEGER NOT NULL CHECK(number >= 0)
);

CREATE INDEX IF NOT EXISTS inventory_index ON warehouse_inventory(inventory_id);
CREATE INDEX IF NOT EXISTS warehouse_index ON warehouse_inventory(warehouse_id);