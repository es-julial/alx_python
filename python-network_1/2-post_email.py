#!/usr/bin/python3
"""takes url & email, sends a POST request and displays the response"""
import requests
import sys

def send_post_request(url, email):
    data = {'email': email}
    response = requests.post(url, data=data)
    return response.text

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_post_request(url, email)
    print(response_body)
