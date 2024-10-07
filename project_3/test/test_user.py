from .utils import *
from ..routers.user import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'manguito_test'
    assert response.json()['email'] == 'manguito_test@gmail.com'
    assert response.json()['first_name'] == 'Manguito'
    assert response.json()['last_name'] == 'Lovebird'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '(111) 111-1111'


def test_change_password_success(test_user):
    response = client.put(
        '/user/password', json={'password': 'testpassword', 'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid(test_user):
    response = client.put(
        '/user/password', json={'password': 'wrongpassword', 'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}


def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/22222222222')
    assert response.status_code == status.HTTP_204_NO_CONTENT
