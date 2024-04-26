#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests


def main():
    """Main function"""

    req = requests.get(url='https://alx-intranet.hbtn.io/status')

    print('Body response:')
    print(f'\t- type: {type(req.text)}')
    print(f'\t- content: {req.reason}')


if __name__ == "__main__":
    main()
