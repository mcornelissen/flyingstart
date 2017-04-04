from lib.helloworld import hi
from lib.textfile import printtext
import sys
from lib.xmlextension import processxml


""" Prints to terminal

    Args:
        param1: [hi|txt|xml]
                - hi prints "helloworld"
                - txt prints contents of etc/text.conf
                - xml searches all tags that match param2
        param2: xml tag to search
"""

def main(params):
    if params[1] == 'hi':
        hi()
    elif params[1] == 'txt':
        printtext()
    elif params[1] == 'xml':
        processxml(params[2])


if __name__ == "__main__":
    main(sys.argv)


