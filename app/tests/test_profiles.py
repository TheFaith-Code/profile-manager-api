from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
#updated

def test_create_profile():
    response = client.post(
        "/profiles",
        json={"name": "Test User", "email": "test@example.com"}
    )
    # 201 Created is the correct REST response for resource creation
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_read_profile():
    # Create a profile first
    create_response = client.post(
        "/profiles",
        json={"name": "Read User", "email": "read@example.com"}
    )
    profile_id = create_response.json()["id"]

    # Fetch it
    response = client.get(f"/profiles/{profile_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == profile_id
    assert data["name"] == "Read User"


def test_update_profile():
    # Create a profile first
    create_response = client.post(
        "/profiles",
        json={"name": "Old Name", "email": "old@example.com"}
    )
    profile_id = create_response.json()["id"]

    # Update it
    response = client.put(
        f"/profiles/{profile_id}",
        json={"name": "New Name", "email": "new@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "New Name"
    assert data["email"] == "new@example.com"


def test_delete_profile():
    # Create a profile first
    create_response = client.post(
        "/profiles",
        json={"name": "Delete Me", "email": "delete@example.com"}
    )
    profile_id = create_response.json()["id"]

    # Delete it
    response = client.delete(f"/profiles/{profile_id}")
    # 204 No Content is the correct REST response for deletion
    assert response.status_code == 204

    # Confirm it's gone
    get_response = client.get(f"/profiles/{profile_id}")
    assert get_response.status_code == 404
