"""
    Fetches a URL, sends a request to the URL, and displays the body of the
    response. Prints an error message if the HTTP status code is >= 400.
"""



import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.text)
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
