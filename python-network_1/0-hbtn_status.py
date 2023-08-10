#!/usr/bin/python3
"""script that fetches 'https://alu-intranet.hbtn.io/status' """
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') \
            as response:
        html = response.read()
    print("Body response:")
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('UTF8')))
