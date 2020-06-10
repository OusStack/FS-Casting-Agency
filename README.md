# Casting Agency API

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

This project uses python, flask and postgresql for it's backend and is hosted on Heroku.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

No frontend is developed for this app, you can use it using cURL or [Postman](https://www.postman.com)


## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Virtual Enviornment

Instructions for setting up a virtual environment can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we use to handle cross origin requests from the frontend server.

## Running the server

First ensure that you are working in the created virtual environment.

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Sourcing `setup.sh` sets some environment variables used by the app.

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the this file to find the application.

You can run this API locally at the default `http://127.0.0.1:5000/`

## Testing

To run the tests, run
```
dropdb capstone_test
createdb capstone_test
psql capstone_test < db.psql
python test_app.py
```

## Deployment

The app is deployed on Heroku [link](https://fsndcapstone.herokuapp.com).

## API Reference

### Getting Started

- Base URL: [link](https://fsndcapstone.herokuapp.com)
- Authentication: This app has 3 users. Each has his own token which are provided in `setup.sh` file. Details about each user privilege are provided below.

### Endpoints

- GET '/actors'
- GET '/movies'
- POST '/actors'
- POST '/movies'
- PATCH '/actors/<int:id>'
- PATCH '/movies/<int:id>'
- DELETE '/actors/<int:id>'
- DELETE '/movies/<int:id>'

Following is the demonstration of each endpoint.

- GET '/actors'
	- Fetch all Actor info from DB
	- Request Argument : None
	- Returns : JSON response containing all actors with their info, and request status
	- example
		```
		{
		  "Actors": [
		    {
		      "age": 38,
		      "email": "Noha@gmail.com",
		      "id": 3,
		      "movies": [
		        "GoGo",
		        "alo"
		      ],
		      "name": "Noha",
		      "salary": 1000
		    }
		  ],
		  "success": true
		}
		```

- GET '/movies'
	- Fetch all Movies info from DB
	- Request Argument : None
	- Returns : JSON response containing all movies with their info, and request status
	- example
		```
		{
		  "Movies": [
		    {
		      "actors": [
		        "ALi",
		        "Ahmed"
		      ],
		      "genre": "Romance",
		      "id": 3,
		      "length": 1.9
		    }
		  ],
		  "success": true
		}
		```

- POST '/actors'
	- Insert Actor info into DB
	- Request Argument :  `name` `email` `age` `salary` `movie_ID`
	- Returns : JSON response containing request status
	- example
		```
		{
		  "success": true
		}
		```

- POST '/movies'
	- Insert Movie info into DB
	- Request Argument : `name` `length` `genre` `actor_ID`
	- Returns : JSON response containing request status
	- example
		```
		{
		  "success": true
		}
		```

- PATCH '/actors/<int:id>'
	- Updtae Actor info and insert it DB
	- Request Argument : `Actor id`  `name` `email` `age` `salary`
	- Returns : JSON response containing request status
	- example
		```
		{
		  "success": true
		}
		```

- PATCH '/movies/<int:id>'
	- Updtae Movie info and insert it DB
	- Request Argument : `Movie id` `name` `length` `genre`
	- Returns : JSON response containing request status
	- example
		```
		{
		  "success": true
		}
		```

- DELETE '/actors/<int:id>'
	- Delete Actor from DB
	- Request Argument : Actor id
	- Returns : JSON response containing request status
	- example
		```
		{
		  "success": true
		}
		```

- DELETE '/movies/<int:id>'
	- Delete Movie from DB
	- Request Argument : Movie id
	- Returns : JSON response containing request status
	- example
		```
		{
		  "success": true
		}
		```


### Users

This app has 3 users. each user has his own privileges.

- Casting Assistant
	- Can view actors and movies

- Casting Director
	- All permissions of a Casting Assistant and…
	- Add or delete an actor from the database
	- Modify actors or movies

- Executive Producer
	- All permissions of a Casting Director and…
	- Add or delete a movie from the database
