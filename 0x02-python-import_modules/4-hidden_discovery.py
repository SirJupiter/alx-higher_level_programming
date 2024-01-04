#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for name in sorted(name for name in names if not name.startswith("_")):
        print(name)


if __name__ == "__main__":
    main()
