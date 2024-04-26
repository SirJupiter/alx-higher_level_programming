#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
 displays the value of the X-Request-Id variable found in the header
   of the response."""

import urllib.request
from sys import argv


def main():
    """main function"""

    url = argv[1]

    with urllib.request.urlopen(url) as response:
        _ = response.read()
        head = response.getheader('X-Request-Id')

    print(head)


if __name__ == "__main__":
    main()
