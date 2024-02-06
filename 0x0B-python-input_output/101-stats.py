#!/usr/bin/python3
"""Module contains """

import sys


def print_metrics(file_sizes, status_codes):
    """Prints the computed metrics."""
    total_file_size = sum(file_sizes)
    print("Total file size: {}".format(total_file_size))

    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))


def main():
    """Main function to read input and compute metrics."""
    line_count = 0
    file_sizes = []
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }

    try:
        for line in sys.stdin:
            # Split the input line into fields
            fields = line.strip().split()
            if len(fields) >= 9:
                file_size = int(fields[-1])
                status_code = int(fields[-2])

                # Update file size list and status code dictionary
                file_sizes.append(file_size)
                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1

                # Print metrics every 10 lines
                if line_count % 10 == 0:
                    print_metrics(file_sizes, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_metrics(file_sizes, status_codes)


if __name__ == "__main__":
    main()
