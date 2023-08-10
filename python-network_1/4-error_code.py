#!/usr/bin/python3
"""Sends a request to a URL and displays the response body, handling error codes"""

import requests
import sys

def main():
    """Main function to send request and handle response"""
    if len(sys.argv) != 2:
        print("Usage: ./4-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

if __name__ == "__main__":
    main()
