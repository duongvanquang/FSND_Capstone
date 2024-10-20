from auth import AuthError, requires_auth
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from models import Actor, Movie, setup_db


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)
    CORS(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers",
                             "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Headers",
                             "GET, POST, PATCH, DELETE, OPTIONS")
        return response

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_all_movies(payload):
        try:
            movies_list = Movie.query.all()

            movies = [movie.format() for movie in movies_list]

            return jsonify({ "success": True, "movies": movies,}), 200
        except:
            abort(500)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        body = request.get_json()

        new_title = body.get('title', None)
        new_genre = body.get('genre', None)
        new_producer = body.get('producer', None)

        if not new_title or not new_genre or not new_producer:
            abort(400)
        try:
            new_movie = Movie(title=new_title, genre=new_genre,producer=new_producer)
            new_movie.insert()

            return jsonify({
                'success': True,
                'movie': new_movie.format()
            })

        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def remove_movie(payload, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                'success': True,
                'movie_removed': movie_id
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def modify_movie(payload, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)

        try:
            body = request.get_json()

            movie.title = body.get('title', movie.title)
            movie.genre = body.get('genre', movie.genre)
            movie.producer = body.get('producer', movie.producer)
            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.format()
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_all_actors(payload):
        try: 
            actors_list = Actor.query.all()

            actors = [actor.format() for actor in actors_list]
            
            return jsonify(
                {"success": True,"actors": actors}), 200
        except:
            abort(500)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        body = request.get_json()

        new_name = body.get('name', None)
        new_gender = body.get('gender', None)
        new_bio = body.get('bio', None)
        if not new_name or not new_gender or not new_bio:
            abort(400)
        
        try:
            actor = Actor(
                name=new_name,
                gender=new_gender,
                bio=new_bio)
            actor.insert()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def remove_actor(payload, actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        try:

            actor.delete()
            return jsonify({
                'success': True,
                'actor_removed': actor_id
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def modify_actor(payload, actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        body = request.get_json()
        new_name = body.get('name', actor.name)
        new_gender = body.get(
                'gender', actor.gender)
        new_bio = body.get('bio', actor.bio)
        try:
            actor.name = new_name
            actor.gender = new_gender
            actor.bio = new_bio
            
            actor.update()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })

        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.errorhandler(AuthError)
    def auth_error(error):
        return (
            jsonify({
                "success": False,
                "error": error.status_code,
                "message": error.error['description']
            }), error.error
        )

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400)

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404,
                    "message": "resource not found"}), 404,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify({"success": False, "error": 500,
                    "message": "internal server error"}), 500,
        )

    return app