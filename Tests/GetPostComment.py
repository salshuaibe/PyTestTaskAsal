import pytest
import requests
import json
def test_posts_positive():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    response = requests.get(url)
    response_data = response.json()
    postId=response_data[0]['postId']
    assert response.status_code == 200
    assert postId==1

def test_posts_Negative():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    response = requests.get(url)
    response_data = response.json()
    postId=response_data[0]['postId']
    assert response.status_code == 201
    assert postId==1

def test_posts_Negative2():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    response = requests.get(url)
    response_data = response.json()
    postId=response_data[0]['postId']
    assert response.status_code == 200
    assert postId==2
