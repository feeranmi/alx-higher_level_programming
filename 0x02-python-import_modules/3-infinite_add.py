#!/usr/bin/python3
import sys


def main():
    add = 0
    for i in range(1, len(sys.argv)):
        add += int(sys.argv[i])
    print("{}".format(add))


if __name__ == "__main__":
    main()
