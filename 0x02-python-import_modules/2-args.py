#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    w = len(argv) - 1
    if w < 1:
        print("{} arguments.".format(w))
    elif w == 1:
        print("{} argument:".format(w))
    else:
        print("{} arguments:".format(w))

    for i in range(w):
        print("{}: {:s}".format(i + 1, argv(i + 1)))
