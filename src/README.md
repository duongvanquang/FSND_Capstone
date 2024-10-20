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
- ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRGN2hkdVRtSWVxWkx3SDZyYURrLSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mZnR3a3diN2JhdG0wNWMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzEzNjY0M2UxNjhkYjRiNjNhMmRmODAiLCJhdWQiOiJGU05EIC0gQ2Fwc3RvbmVfQVBJIiwiaWF0IjoxNzI5NDEyMTYxLCJleHAiOjE3Mjk0ODQxNjAsInNjb3BlIjoiIiwiYXpwIjoiYUNnTjVCMVNUY243eml1a0dXT3NSYkZoWG1WenhwTUsiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ZBX9yp4zUXkiplC3Ygn1Qv4EJYAY1or5uLzyis466Q24oj_7xSgcdywrJZ3ywILltrnijPmIziM971SBkXGWICssrLUWszk6L8JwPjMSWigKqBFdLNANSXzFNjNA4U68sy_hu0MTkTnvGG7qO0FulPhqxZUd85bF4eCwhH7zkywApE0kfMYVHMhJmwhzcpwKtHApY5-w4J9YeuxiLpuLyCJ6GKQaESTR0S_zA4KzXuau6f4Uh4Ad4GXR2igRo-XkUp3MOAgiOS3smKSopPndD4XQ8jwwJYWwEUoFlDAr8SwJld-s2ufk0GSM9WJGYkgkyMCtFJ-ZTyL_DZHZetItkw'
- DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRGN2hkdVRtSWVxWkx3SDZyYURrLSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mZnR3a3diN2JhdG0wNWMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzEzNjY0M2UxNjhkYjRiNjNhMmRmODAiLCJhdWQiOiJGU05EIC0gQ2Fwc3RvbmVfQVBJIiwiaWF0IjoxNzI5NDEyMjg3LCJleHAiOjE3Mjk0ODQyODYsInNjb3BlIjoiIiwiYXpwIjoiYUNnTjVCMVNUY243eml1a0dXT3NSYkZoWG1WenhwTUsiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.laMRrrO8C_L9F19oLUw8k7nN8Kh8mLCb5QJwH59V3SBifYVTUkL24PRtk_-7sG2M881MTnf3E6y6RWNV55KbG-zTuvR_qcAm4vSju99RITtZ4tfhg_91ABGJ7Arb4EZ-5SRjzcUHsNdCR5EMuLcTcNYzoUo0tExIxRQADIZ3esQs92kkZXnpQi5mWeuygz05mQnZ7h7NfNhcc523nlSPFxn-lryQnjovNgNdsAmLWe6ti2ZUDpKp17s0xaHi9jFai0DFPW7eg4CNFht4qqF9HWtjjr1nz8-Iqe_GpGQsV81SKITgOPMpzs6tKhu9vW6uWM7nx1i1r_eUjLBClNoKlw'
- PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRGN2hkdVRtSWVxWkx3SDZyYURrLSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mZnR3a3diN2JhdG0wNWMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzEzNjY0M2UxNjhkYjRiNjNhMmRmODAiLCJhdWQiOiJGU05EIC0gQ2Fwc3RvbmVfQVBJIiwiaWF0IjoxNzI5NDEyNDg1LCJleHAiOjE3Mjk0ODQ0ODQsInNjb3BlIjoiIiwiYXpwIjoiYUNnTjVCMVNUY243eml1a0dXT3NSYkZoWG1WenhwTUsiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.IHwv60I6GCAne7AYet_RV21l9gSPCrIc6xku-ZFWZBKRi_PzgnvZvIJaM1f0HCC2tmjnbNZ9dgOXod6xfk6PK6B5hD2YY2mGnOKgdUia_VSgEDm2NxS799QD-jv3juCmJsU86gxVphlm9USG6WD5ELpiipv_7Skl9Mg6f2bAeGWdsqUA90M40174hVZUxK4xSSalsWRuKmKN4fvZKwMQ7uDe-6mhU_gtfDCyw6CbalQUld2U0-odk1wfb1uXrhAfuXqxV4ZhUKRPZj8ydNQgLN_9Zm0Kw2B3MsF1zaLTcs0-_0xCKIp6xNvA2Xq2oorrVN37_dfQpZELUhb-j2itdQ'

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
            "genre": "Genre 1",
            "id": 1,
            "producer": "Producer 1",
            "title": "Movie 1"
        },
        {
            "genre": "Genre 2",
            "id": 2,
            "producer": "Producer 2",
            "title": "Movie 2"
        },
        {
            "genre": "Genre 3",
            "id": 3,
            "producer": "Producer 3",
            "title": "Movie 3"
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
            "name": "Test Actor",  
            "gender": "Female",
            "bio": "This is test data for the actor"
        }
```
- Returns: An object containing the information of the newly added movie, including id, bio, gender, and name.
```json
{
    "actor": 
        {
            "name": "Test Actor",  
            "gender": "Female",
            "id": 4,
            "bio": "This is test data for the actor"
        },
    "success": true
}
```

### `PATCH '/movies/<int:movie_id>'`
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
    "actor": 
        {
            "name": "Edited name",  
            "gender": "Male",
            "id": 1,
            "bio": "Edited bio"
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
    "actor_removed": 1,
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