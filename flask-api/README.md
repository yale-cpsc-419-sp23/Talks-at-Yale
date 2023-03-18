# Flask Application
-------------------
-------------------

## Getting Started

To run the flask application, you need to navigate into flask-api directory
```
cd flask-api
```
then run the command:
```
flask run
```

if you have all requirements installed, the application should start running.

The app has the following files:
* config.py -> has configurations for the application
* api.py -> has the app, making it possible to use the command flask run
* .flaskenv -> setting FLASK_APP=api.py so that we can use flask run, and not set environment variable everytime

## App Folder

### Models
This is where objects such as events and users is defined.
flask sql version, flask-sqlalchemy allow you to create objects and store them in a database which will be easier to handle in the backend.

### Migrations
flask-sqlalchemy is used to store users and events, this is an easy way to keep track of the database, migrations allow you to change your databse schema without having to delete the already existing database or update existing objects. You can downgrade and upgrade the database,
see: [flask-mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for more info.

### BluePrints
Flask BluePrints is also used to modularize the app, allowing routes to handle events be separated from routes handling user logins.

