#!/usr/bin/python3
"""Fetches the value of the X-Request-Id header from a given URL's response"""

import requests
import sys

def main():
    """Main function to fetch and display the X-Request-Id header"""
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)

if __name__ == "__main__":
    main()
