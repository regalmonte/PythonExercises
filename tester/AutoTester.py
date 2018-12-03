import sys
import os


def main():
    os.chdir(os.path.dirname(__file__))
    sys.path.insert(0, sys.argv[1])
    test_module = __import__(sys.argv[2])
    test_function: function = eval("test_module." + sys.argv[3])
    print(test_function([12, 23, 34, 45]))


if __name__ == "__main__":
    main()

