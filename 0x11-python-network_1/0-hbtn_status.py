#!/usr/bin/python3
""" script fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


def main():
    """main fuction"""

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        data = response.read()

    print('Body response:')
    print(f'    - type: {type(data)}')
    print(f'    - content: {data}')
    print(f'    - utf8 content: {data.decode("utf8")}')


if __name__ == "__main__":
    main()
