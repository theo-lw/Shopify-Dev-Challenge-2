# Shopify Fall 2022 Technical Challenge, Production Engineering

### Replit link

https://replit.com/@theo-lw/Shopify-Dev-Challenge-2

The extra feature is that any city in the world can be used as a storage location, so  long as it is created via the `city/create` endpoint.

### Files

`main.py`: server boilerplate, routes and their corresponding functions.

`queries.py`: contains the SQL queries used in this application.

`classes.py`: contains dataclasses representing JSON requests/responses.

`schema.sql`: defines the schema of the database.

`templates/index.html`: the HTML page shown in the browser.

`static/index.js`: some Javascript to make HTTP requests to the backend upon form submissions.

### Libraries used

`flask`: a micro web framework.

`marshmallow`: a library for simple serialization/deserialization and validation.

`sqlite3`: an embedded database, chosen because it is simple to deploy on Replit. I'm not concerned about scalability right now because I don't expect multiple concurrent users :)

`requests`: a library to make HTTP requests in Python.