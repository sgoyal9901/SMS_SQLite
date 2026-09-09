from fastapi.testclient import TestClient
from api.main import app
from test.conftest import test_database

client = TestClient(app)

def test_get_all_students(test_database):
    response = client.get("/api/v1/students")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1
    assert data["limit"] == 20
    assert isinstance(data["data"], list)
    
def test_get_all_students_with_query_params(test_database):
    response = client.get("/api/v1/students?class_id=1&section_id=1")
    assert response.status_code == 200

def test_get_all_students_with_non_existent_class(test_database):
    response = client.get("/api/v1/students?class_id=90&section_id=1")
    assert response.status_code == 404 

def test_get_all_students_with_invalid_page(test_database):
    response = client.get("/api/v1/students?page=0")
    assert response.status_code == 400

def test_get_all_students_with_invalid_limit(test_database):
    response = client.get("/api/v1/students?limit=101")
    assert response.status_code == 400

def test_get_all_students_response_structure(test_database):
    response = client.get("/api/v1/students")
    data = response.json()
    assert "page" in data
    assert "limit" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data

def test_get_all_students_with_limit(test_database):
    response = client.get("/api/v1/students?limit=10")
    data = response.json()
    assert data["limit"] == 10

def test_get_all_students_with_search(test_database):
    response = client.get("/api/v1/students?search=aR")
    data = response.json()
    assert any("arjun" in student["name"].lower() for student in data["data"])

def test_post_student(test_database):
    response = client.post("/api/v1/students", json={"name": "anil", "father_name": "kumar", "section_id": 2, "contact_number": "1234567890"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "anil"
    assert data["father_name"] == "kumar"
    assert data["class_name"] == "1"
    assert data["section_name"] == "B"
    assert data["contact_number"] == "1234567890"

def test_post_student_with_incomplete_data(test_database):
    response = client.post("/api/v1/students", json={"name": "anil", "father_name": "kumar", "contact_number": "1234567890"})
    assert response.status_code == 422

def test_post_student_with_incomplete_data_2(test_database):
    response = client.post("/api/v1/students", json={"name": "anil", "father_name": "kumar", "section_id": 2})
    assert response.status_code == 422

def test_get_student_by_id(test_database):
    response = client.get("/api/v1/students/id/1")
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == 1
    assert data["name"] == "Arun"
    assert data["father_name"] == "Abhi"
    assert data["class_name"] == "1"
    assert data["section_name"] == "A"
    assert data["contact_number"] == "9090890890"

def test_get_non_existent_student(test_database):
    response = client.get("/api/v1/students/id/90")
    assert response.status_code == 404

def test_put_student(test_database):
    response = client.put("/api/v1/students/8", json={"name": "akhil"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "akhil"
    assert data["father_name"] == "kumar"
    assert data["class_name"] == "1"
    assert data["section_name"] == "B"
    assert data["contact_number"] == "1234567890"

def test_put_non_existent_student(test_database):
    response = client.put("/api/v1/students/90", json={"name": "akhil"})
    assert response.status_code == 404

def test_put_student_with_invalid_data(test_database):
    response = client.put("/api/v1/students/8", json={"name": "0akhil"})
    assert response.status_code == 400

def test_delete_student(test_database):
    response = client.delete("/api/v1/students/8")
    assert response.status_code == 204

def test_delete_non_existent_student(test_database):
    response = client.delete("/api/v1/students/90")
    assert response.status_code == 400

