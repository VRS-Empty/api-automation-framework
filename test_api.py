import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
def test_get_single_user():

    user_id = 1
    response = requests.get(f"{base_url}/users/{user_id}")

    print(f"\n[DEBUG] URL: {response.url}")
    print(f"[DEBUG] Status Code: {response.status_code}")

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    assert response.elapsed.total_seconds() < 1.0, "API response is too slow!"

    data = response.json()

    assert data["id"] == user_id, f"Expected user_id {user_id} but got {data['id']}"

    assert "name" in data, "Name field is missing"
    assert "email" in data, "Email field is missing"

    assert data["name"] == "Leanne Graham", "User name does not match!"

def test_get_user_not_found():

    response = requests.get(f"{base_url}/users/999")
    
    print(f"\n[DEBUG] URL: {response.url}")
    print(f"[DEBUG] Status Code: {response.status_code}")
    
    assert response.status_code == 404, f"Expected 404 but got {response.status_code}"