CREATE TABLE IF NOT EXISTS inventory(
  id INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  city_id INTEGER REFERENCES city ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS city(
  id INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  longitude REAL NOT NULL,
  latitude REAL NOT NULL,
  UNIQUE(longitude, latitude)
);

INSERT OR IGNORE INTO CITY (name, latitude, longitude) VALUES 
  ("Ottawa", 45.424721, -75.695000),
  ("Toronto", 43.653908, -79.384293),
  ("Montreal", 45.508888, -73.561668),
  ("Vancouver", 49.246292, -123.116226),
  ("Waterloo", 43.466667, -80.516670);