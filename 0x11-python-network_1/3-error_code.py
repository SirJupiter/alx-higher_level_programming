#!/usr/bin/python3
"""script takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8)."""

import urllib.error
import urllib.request
from sys import argv


def main():
    """Main function"""

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.status}')
    else:
        print(data)


if __name__ == "__main__":
    main()
