"""documentation module"""

import requests
def fetch_hbtn_status():
    """documentation fonction"""
    req = requests.get("https://alu-intranet.hbtn.io/status")
    content = req.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
if __name__ == "__main__":
    fetch_hbtn_status()
