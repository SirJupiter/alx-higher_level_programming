#!/usr/bin/python3
"""script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.error
import urllib.request
import urllib.parse
from sys import argv


def main():
    """main function"""

    url = argv[1]

    data = {}
    if argv[2]:
        data = {'email': argv[2]}

    encoded_data = urllib.parse.urlencode(data).encode('ascii')
    request = urllib.request.Request(url, encoded_data)

    try:
        with urllib.request.urlopen(request) as response:
            result = response.read()
            body = result.decode('utf-8')

        print(body)

    except urllib.error.URLError as e:
        print(f"Error accessing {url}: {e.reason}")


if __name__ == "__main__":
    main()
