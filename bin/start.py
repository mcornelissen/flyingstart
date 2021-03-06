""" Print to terminal

    Usage: python -m bin.script param1 [Param 2]

    Args:
        param1: [hi|txt|xml|name|foobar]
                - hi   prints "helloworld"
                - txt  prints contents of etc/text.conf
                - xml  searches all tags that match param2
                - name searches matching name and prints all 
                       info from that block
                - foobar Inheritance example
        param2: String to search wrt param1
"""

from lib.helloworld import hi
from lib.textfile import printtext
import sys
from lib.xmlextension import processxml
from lib.xmlextension import processxml_get_block
from lib.inheritance import foobar

def main(params):
    if params[1] == 'hi':
        hi()
    elif params[1] == 'txt':
        printtext()
    elif params[1] == 'xml':
        processxml(params[2])
    elif params[1] == 'name':
        processxml_get_block(params[2])
    elif params[1] == 'foobar':
        foobar()

if __name__ == "__main__":
    main(sys.argv)


