#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    conteo = len(sys.argv) - 1

if conteo == 0:
    print("0 arguments.")
elif conteo == 1:
    print("{} argument:".format(conteo))
    print("{}: {}".format(conteo, argv[conteo]))
else:
    print("{} arguments:".format(conteo))
    for i in range(1, conteo + 1):
        print("{}: {}".format(i, argv[i]))
