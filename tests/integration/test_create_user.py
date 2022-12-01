def test_create_user(client):
    response = client.get("/user/")
    assert response.status_code == 200
    
