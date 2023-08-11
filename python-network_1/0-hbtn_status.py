#!/usr/bin/python3

"""
This script fetches the status information from a URL using the 'requests' package
and displays the body of the response with tabulation.
"""

import requests

class StatusFetcher:
    """
    A class to fetch and display status information from a URL.
    """

    def __init__(self, url):
        """
        Initialize the StatusFetcher with the given URL.

        Args:
            url (str): The URL to fetch the status from.
        """
        self.url = url

    def fetch_and_display_status(self):
        """
        Fetches the status information from the URL and displays the response body.

        Returns:
            None
        """
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()
            print("Body response:")
            print("\t- type:", type(data))
            print("\t- content:", data)
        else:
            print("Error:", response.status_code)

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    status_fetcher = StatusFetcher(url)
    status_fetcher.fetch_and_display_status()
