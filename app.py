import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, Casting, db
from auth import AuthError, requires_auth

def create_app(test_config=None):
    ####
    """
    Creating and configuring the application
    """
    ####

    app = Flask(__name__)
    setup_db(app)
    CORS(app, resource={r"/api.*": {"origin": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow_Headers",
                             "Content-Type,Authorization,true")
        response.headers.add("Access-Contorl-Allow_Methods",
                             "GET,POST,PATCH,DELETE")
        return response
    
    ####
    """"
    Movie
    """"
    ####
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        ###
        """
        Retrieve all movies.
        """
        ###
        movies = Movie.query.all()

        if movies is None:
            abort(404, "There is no movie data.")

        movies_format = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies_format
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):
        ###
        """
        Create a new movie.
        """
        ###
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            title = data.get('title')
            release_date = data.get('release_date')

            new_movie = Movie(title=title, release_date=release_date)
            new_movie.insert()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'new_movie': new_movie.format()
            }), 200
            db.session.close()

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, movie_id):
        ###
        """
        Update the movie's info.
        """
        ###
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404, "There is no such a movie.")

        data = request.get_json()
        title = data.get('title')
        release_date = data.get('release_date')

        try:
            movie.title = title
            movie.release_date = release_date
            movie.update()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'updated_movie': movie.format()
            }), 200
            db.session.close()

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        ###
        """
        Deleting a movie.
        """
        ###
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404, "There is no such a movie.")

        try:
            movie.delete()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'deleted_movie': movie_id
            }), 200
            db.session.close()
    ###
    """
    Actors
    """
    ###
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        ###
        """
        Retrieve all actors.
        """
        ###
        actors = Actor.query.all()

        if actors is None:
            abort(404, "There is no actor data.")

        actors_format = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors_format
        }), 200

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(jwt):
        ###
        """
        Create new actor
        """
        ###
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            name = data.get('name')
            age = data.get('age')
            gender = data.get('gender')

            new_actor = Actor(name=name, age=age, gender=gender)
            new_actor.insert()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'new_actor': new_actor.format()
            }), 200
            db.session.close()

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(jwt, actor_id):
        ###
        """
        Update the actors info.
        """
        ###
        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404, "There is no such an actor.")

        data = request.get_json()
        name = data.get('name')
        gender = data.get('gender')
        age = data.get('age')

        try:
            actor.name = name
            actor.gender = gender
            actor.age = age
            actor.update()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'updated_actor': actor.format()
            }), 200
            db.session.close()

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        ###
        """
        Delete an actor.
        """
        ###
        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404, 'There is no such an actor.')

        try:
            actor.delete()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'deleted_actor': actor_id
            }), 200
            db.session.close()

    #######
    """
    Casting
    """
    #######
    @app.route('/casting', methods=['GET'])
    @requires_auth('get:casting')
    def get_casting(jwt):
        
        ###
        """
        Retrieve all casting information.
        """
        ###
        casting = Casting.query.all()

        if casting is None:
            abort(404, 'There is no castin info.')

        casting_format = [cast.format() for cast in casting]

        return jsonify({
            'success': True,
            'casting': casting_format
        }), 200

    @app.route('/casting', methods=['POST'])
    @requires_auth('post:casting')
    def create_casting(jwt):
        ###
        """
        Create a new casting.
        """
        ###
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            actor_id = data.get('actor_id')
            movie_id = data.get('movie_id')

            new_casting = Casting(actor_id=actor_id, movie_id=movie_id)
            new_casting.insert()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'new_casting': new_casting.format()
            }), 200
            db.session.close()

    @app.route('/casting/<int:casting_id>', methods=['PATCH'])
    @requires_auth('patch:casting')
    def update_casting(jwt, casting_id):
        ###
        """
        Update the casting's info.
        """
        ###
        casting = Casting.query.get(casting_id)

        if casting is None:
            abort(404, 'There is no such a casting.')

        data = request.get_json()
        actor_id = data.get('actor_id')
        movie_id = data.get('movie_id')

        try:
            casting.actor_id = actor_id
            casting.movie_id = movie_id
            casting.update()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'updated_casting': casting.format()
            }), 200
            db.session.close()

    @app.route('/casting/<int:casting_id>', methods=['DELETE'])
    @requires_auth('delete:casting')
    def delete_casting(jwt, casting_id):
        ###
        """
        Delete the casting.
        """
        ###
        casting = Casting.query.get(casting_id)

        if casting is None:
            abort(404, "There is no such a casting here.")

        try:
            casting.delete()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'deleted_casting': casting_id
            }), 200
            db.session.close()

    ###
    """
    Errors Handling
    """
    ###

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(500)
    def internal_sever_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    @app.errorhandler(AuthError)
    def auth_error_handler(error):
        response = jsonify(error.error)
        response.status_code = error.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
