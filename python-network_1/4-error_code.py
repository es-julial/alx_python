"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":
    response = r.get(s.argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code: ",code)
    else:
        print("Regular request")
