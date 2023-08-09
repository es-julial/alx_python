#!/usr/bin/python3
"""
This is a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the provided URL with the email as a parameter and displays the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include as a parameter in the request.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
    """
    payload = {"email": email}

    response = requests.post(url, data=payload)

    response.raise_for_status()

    print("Response body:")
    print(response.text)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please provide a URL and an email address as command-line arguments.")
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        try:
            send_post_request(url, email)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))
