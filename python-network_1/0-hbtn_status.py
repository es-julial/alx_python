"""
Make a get request to a webpage
"""
import requests

response = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}\n"
      "\t- content: {}".format(type(response.text), response.text))
