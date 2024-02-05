from fastapi.testclient import TestClient
from fastapi import status, HTTPException
from app.main import app

client = TestClient(app)

def test_read_course():
    ## TODO: Check if GET /courses/{course_id} returns status code 200 and that the json response is
    ## correct (as per db) when the course exists
    response = client.get("/courses/CS-E4190") # Fix the route to API as required
    assert response.status_code == 200
    assert response.json() == {
        "id": "CS-E4190",
        "name": "Cloud software and systems",
        "instructor": "Mario Di francesco",
        "keyword": ["cloud", "container"]
    }

def test_read_nonexistent_course():
    ## TODO: Check if GET /courses/{course_id} returns status code 404 and that the json response is
    ## {"detail": "Course does not exist"} when the course does not exist
    response = client.get("/courses/{course_id}") # Fix the route to API as required
    assert response.status_code == 404
    assert response.json() == {"detail": "Course does not exist"}
    # raise HTTPException(
    #     404,
    #     detail="Course does not exist"
    # )

def test_create_course():
    ## TODO: Check if POST /courses/ returns status code 200 and that the json response
    ## contains the correct data if the course does not exist in the db.
    response = client.post('/courses/',json={
        "id": "CS-E1234",
        "name": "Mobile Communications",
        "instructor": "Alexis",
        "keyword": ["4G", "5G"]
    }) # Fix the route to API and data as required
    assert response.status_code == 200
    assert response.json() == {
        "id": "CS-E1234",
        "name": "Mobile Communications",
        "instructor": "Alexis",
        "keyword": ["4G", "5G"]
    }

def test_create_existing_course():
    ## TODO: Check if POST /courses/ returns status code 400 and that the json response
    ## is {"detail": "Course already exists"} if the course already exists in the db.
    response = client.post('/courses/',json={
        "id": "CS-E1234",
        "name": "Mobile Communications",
        "instructor": "Alexis",
        "keyword": ["4G", "5G"]
    })  # Fix the route to API and data as required
    assert response.status_code == 400
    assert response.json() == {"detail": "Course already exists"}
    # raise HTTPException(
    #     400,
    #     detail="Course already exists"
    # )
    




# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)


# def test_read_course():
#     ## TODO: Check if GET /courses/{course_id} returns status code 200 and that the json response is
#     ## correct (as per db) when the course exists
#     response = client.get('/') # Fix the route to API as required
#     assert {"id": "CS-E4190"} == {"id": "CS-1234"}


# def test_read_nonexistent_course():
#     ## TODO: Check if GET /courses/{course_id} returns status code 404 and that the json response is
#     ## {"detail": "Course does not exist"} when the course does not exist
#     response = client.get('/') # Fix the route to API as required
#     assert response.json() == {"id": "CS-1234"}


# def test_create_course():
#     ## TODO: Check if POST /courses/ returns status code 200 and that the json response
#     ## contains the correct data if the course does not exist in the db.
#     response = client.post('/',json={"id":"CS"}) # Fix the route to API and data as required
#     assert response.json() == {"id": "CS-1234"}

# def test_create_existing_course():
#     ## TODO: Check if POST /courses/ returns status code 400 and that the json response
#     ## is {"detail": "Course already exists"} if the course already exists in the db.
#     response = client.post('/',json={"id":"CS"})  # Fix the route to API and data as required
#     assert response.json() == {"id": "CS-1234"}
