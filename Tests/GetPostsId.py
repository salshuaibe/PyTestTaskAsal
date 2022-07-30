import pytest
import requests
import json
def test_posts_positive():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    response_data = response.json()
    id=response_data['id']
    assert response.status_code == 200
    assert id==1
    assert len(response_data)==4
def test_posts_Negative1():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    response_data = response.json()
    id=response_data['id']
    assert response.status_code == 201
    assert id==1
    assert len(response_data)==4
def test_posts_Negative2():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    response_data = response.json()
    id=response_data['id']
    assert response.status_code == 200
    assert id==2
    assert len(response_data)==4
def test_posts_Negative3():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    response_data = response.json()
    id=response_data['id']
    assert response.status_code == 200
    assert id==1
    assert len(response_data)==7


