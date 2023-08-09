#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response"""

import requests
import sys

def main():
    """Main function to send POST request and display response"""
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)

if __name__ == "__main__":
    main()