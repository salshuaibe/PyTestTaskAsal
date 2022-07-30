import pytest
import requests
import json


def posts_url():
    return "https://jsonplaceholder.typicode.com/posts"


def test_posts_valid():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url)
    assert response.status_code == 201
def test_posts_Postitve():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 200
    assert len(response.json()) ==100
def test_posts_Negative1():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 200
    assert len(response.json()) ==204
def test_posts_Negative2():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 205
    assert len(response.json()) ==100





