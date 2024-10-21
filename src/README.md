## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `capstone_project_db` database:
```bash
createdb capstone_project_db
```
Populate the database using the `capstone_project.psql` file provided. From the `backend` folder in terminal run:

```bash
psql capstone_project_db < capstone_project.psql
```

### Run the Server

From within the `./backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.
### RBAC
- Casting assistant permissions:
    "get:actors",
    "get:movies"
- Casting director permissions:
    "delete:actors",
    "get:actors",
    "get:movies",
    "patch:actors",
    "patch:movies",
    "post:actors"
- Executive producer permissions:
    "delete:actors",
    "delete:movies",
    "get:actors",
    "get:movies",
    "patch:actors",
    "patch:movies",
    "post:actors",
    "post:movies"
### TOKEN
- ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRGN2hkdVRtSWVxWkx3SDZyYURrLSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mZnR3a3diN2JhdG0wNWMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzEzNjY0M2UxNjhkYjRiNjNhMmRmODAiLCJhdWQiOiJGU05EIC0gQ2Fwc3RvbmVfQVBJIiwiaWF0IjoxNzI5NTAyMzU5LCJleHAiOjE3Mjk1ODg3NTksInNjb3BlIjoiIiwiYXpwIjoiYUNnTjVCMVNUY243eml1a0dXT3NSYkZoWG1WenhwTUsiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ktSvODxL0NeCyXbhwOXm_j2VEda7DYJYsGdTf1ORnpLNPHepVuMI-dAUwx1ceMtzwRlBFzenXbtbgWGYnd8zmkUj2ibuA4lhetl0gx8kHDeVc7iKET-Lb2Nq7ktL_ZsEsiDpTmZnS7yzWXQXyatpNbk8vFotEWwaz-gyWYKRJLMJEUhhWYut2FbqVDzEtiUXzevrkE2-YsoYDyxZTuLcwbWKZymnXnHYWuZDiRedJPfSxtCboyXoa7P-cAVgG8s1vSw8vQhWQu7oQb5Lu_ufpxCwAlt7-22Mx5Q5hv_sypgSHOy6j7xU5aPSSwCn2CMuMmU3mVXo6ZO5UqdA8wZ-aA'
- DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRGN2hkdVRtSWVxWkx3SDZyYURrLSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mZnR3a3diN2JhdG0wNWMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzEzNjY0M2UxNjhkYjRiNjNhMmRmODAiLCJhdWQiOiJGU05EIC0gQ2Fwc3RvbmVfQVBJIiwiaWF0IjoxNzI5NTAyNDQ4LCJleHAiOjE3Mjk1ODg4NDgsInNjb3BlIjoiIiwiYXpwIjoiYUNnTjVCMVNUY243eml1a0dXT3NSYkZoWG1WenhwTUsiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.p7LToDtNkZiTD-gUlwhsWQ_VXKqpB9q-sFm2LcHCNoqhngW1gfFXFpAm4wAE9xQZyKN2xiF8FxVF3dUS7sl19z4sCjt_uQXFG4qQQde_T4HWJR0GOwgh_laMc4WMFHEKMy2g2bcVJwunXVGKX7kORUtOoC8po5BCYKyDTm0ha2o6C03sZCGarV0YKi_bbxQUAE66EhX3vqqFUyzRBsi7F_F6KeqpNyG4pLWBz8g_Npim4QvEXcomfUHjpPpp1U-rqxXaG4sY9kSOiLoOJ5O77RMcRX1AUOPl7swlmgJP5YDozDIYTdUzot6SU1vc00UmsTNQv9No8qQHBDZye1e7FA'

- PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRGN2hkdVRtSWVxWkx3SDZyYURrLSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mZnR3a3diN2JhdG0wNWMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzEzNjY0M2UxNjhkYjRiNjNhMmRmODAiLCJhdWQiOiJGU05EIC0gQ2Fwc3RvbmVfQVBJIiwiaWF0IjoxNzI5NTAyMjQ0LCJleHAiOjE3Mjk1ODg2NDQsInNjb3BlIjoiIiwiYXpwIjoiYUNnTjVCMVNUY243eml1a0dXT3NSYkZoWG1WenhwTUsiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.btEYW4ud09jp89wnVdlO6GXiDvlLhnBaZvadWiGzsqEu3Gfi_SSizEehVbCjYIY_WJpYW8r5eODIk1NclB8Xnjz2KPnYvDWCZzdgiSpEPzdUFutyi_vd_vWNl_BLkYrvGHbrf4NDIj_3NzcglTn393Y-z0XNvaWK2EFnntrJBDS8FnE7C-eJPLnCcj6eFdL3rr93lOSt7ZMcaSWkVjl14-RiCZsjlo51qkYc5Pjgim6RFk-70HjWnrg71Mh2tLWJFSp1sIrbNaw63v39WD4Fk4Dp_dnPIf5d6oS8f5Ptv6CFJpQqyNIznBcoluo9Zx6mEteFklc26z-tNjgYTKqDPA'

### Expected endpoints and behaviors

### `GET '/actors'`
- Fetch the list of all actors from the server. 
- Request Arguments: None
- Returns: A list of actor objects containing the attributes id, bio, gender and name.

```json
{
    "actors": [
        {
            "bio": "Bio 1",
            "gender": "Male",
            "id": 1,
            "name": "Actor 1"
        },
        {
            "bio": "Bio 2",
            "gender": "Female",
            "id": 2,
            "name": "Actor 2"
        },
        {
            "bio": "Bio 3",
            "gender": "Male",
            "id": 3,
            "name": "Actor 3"
        }
    ],
    "success": true
}
```

### `POST '/actors'`
- post a new actor to the server.
- Request Arguments: An object containing string attributes including bio, gender, and name.
```json
        {
            "name": "Test Actor",  
            "gender": "Female",
            "bio": "This is test data for the actor"
        }
```
- Returns: An object containing the information of the newly added movie, including id, bio, gender, and name.
```json
{
    "actor": {
        "bio": "This is test data for the actor",
        "gender": "Female",
        "id": 4,
        "name": "Test Actor"
    },
    "success": true
}
```

### `PATCH '/actors/<int:actor_id>'`
- Find the actor with the matching ID from the URL and modify that actor's data.
- Request Arguments: An object has at least one of these properties: bio, gender, or name.
```json
        {
            "name": "Edited name",  
            "gender": "Male",
            "bio": "Edited bio"
        }
```
- Returns: An object containing the information of the newly updated movie, including id, bio, gender, and name.

```json
{
    "actor": {
        "bio": "Edited bio",
        "gender": "Male",
        "id": 1,
        "name": "Edited name"
    },
    "success": true
}
```

### `DELETE '/actors/<int:actor_id>'`
- Find and delete the actor whose ID matches the ID in the URL.
- Request Arguments: None
- Returns: An object with an actor_removed property that holds the ID of the recently deleted actor.

```json
{
    "actor_removed": 1,
    "success": true
}
```

### `GET '/movies'`
- Fetch the list of all movies from the server. 
- Request Arguments: None
- Returns: A list of movie objects containing the attributes id, genre, producer and title.

```json
{
    "movies": [
        {
            "genre": "anime",
            "id": 1,
            "producer": "Producer 3",
            "title": "Test Movies"
        },
        {
            "genre": "anime",
            "id": 2,
            "producer": "Producer 3",
            "title": "Test Movies"
        }
    ],
    "success": true
}
```

### `POST '/movies'`
- post a new actor to the server.
- Request Arguments: An object containing string attributes including bio, gender, and name.
```json
        {
            "title": "Test Movies",
            "producer": "Producer 3",
            "genre": "anime"
        }
```
- Returns: An object containing the information of the newly added movie, including id, bio, gender, and name.
```json
{
    "movie": {
        "genre": "anime",
        "id": 3,
        "producer": "Producer 3",
        "title": "Test Movies"
    },
    "success": true
}
```

### `PATCH '/movies/<int:movie_id>'`
- Find the actor with the matching ID from the URL and modify that actor's data.
- Request Arguments: An object has at least one of these properties: bio, gender, or name.
```json
        {
            "title": "Edit Movies",
            "producer": "Producer 3",
            "genre": "anime"
        }
```
- Returns: An object containing the information of the newly updated movie, including id, bio, gender, and name.

```json
{
    "movie": {
        "genre": "anime",
        "id": 1,
        "producer": "Producer 3",
        "title": "Edit Movies"
    },
    "success": true
}
```

### `DELETE '/movies/<int:movie_id>'`
- Find and delete the actor whose ID matches the ID in the URL.
- Request Arguments: None
- Returns: An object with an actor_removed property that holds the ID of the recently deleted actor.

```json
{
    "movie_removed": 1,
    "success": true
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb capstone_project_db_test
createdb capstone_project_db_test
psql capstone_project_db_test < capstone_project.psql
python test_app.py