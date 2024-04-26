#!/usr/bin/python3
"""script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

from sys import argv
import requests


def main():
    """Main function"""

    url = argv[1]

    data = {}
    if argv[2]:
        data = {'email': argv[2]}

    req = requests.post(url=url, data=data)

    print(req.text)


if __name__ == "__main__":
    main()
