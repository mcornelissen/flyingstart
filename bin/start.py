from lib.helloworld import hi
from lib.textfile import printtext
import sys
from lib.xmlextension import processxml
from lib.xmlextension import processxml_get_block

""" Prints to terminal

    Args:
        param1: [hi|txt|xml|name]
                - hi   prints "helloworld"
                - txt  prints contents of etc/text.conf
                - xml  searches all tags that match param2
                - name searches matching name and prints all 
                       info from that block
        param2: String to search wrt param1
"""

def main(params):
    if params[1] == 'hi':
        hi()
    elif params[1] == 'txt':
        printtext()
    elif params[1] == 'xml':
        processxml(params[2])
    elif params[1] == 'name':
        processxml_get_block(params[2])

if __name__ == "__main__":
    main(sys.argv)


