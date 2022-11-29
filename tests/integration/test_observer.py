
def test_create_user(client):
    response = client.get("/health/")
    assert response.status_code == 200
    
