#!/usr/bin/python3
"""
This is a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import requests
import sys

def fetch_response_body(url):
    """
    Fetches the body of the response from the given URL and prints it.

    Args:
        url (str): The URL to send the request to.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
    """
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        fetch_response_body(url)
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
