#!/usr/bin/env python3
"""
Module to fetch and display the status of a website.
"""

import requests

def fetch_hbtn_status():
    """
    Fetches and displays the status of https://alu-intranet.hbtn.io/status.
    """
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    content_type = type(response.text)
    content = response.text

    print("Body response:")
    print(f"\t- type: {content_type}")
    print(f"\t- content: {content}")

if __name__ == "__main__":
    fetch_hbtn_status()



