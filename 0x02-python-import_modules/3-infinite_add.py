#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    infinite = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            infinite += int(arg)
    print(infinite)