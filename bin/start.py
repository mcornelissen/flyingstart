from lib.helloworld import hi
from lib.textfile import printtext
import sys

""" Prints to terminal

    Args:
        param1: [hi|txt]
                - hi prints "helloworld"
                - txt prints contents of etc/text.conf
"""

def main(param1):
    if param1 == 'hi':
        hi()
    elif param1 == 'txt':
        printtext()


if __name__ == "__main__":
    main(sys.argv[1])


