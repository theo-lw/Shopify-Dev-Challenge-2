# Shopify Fall 2022 Technical Challenge

### Replit link

https://replit.com/join/jbkaioscru-theo-lw

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