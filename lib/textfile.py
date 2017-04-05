""" Print the contect of etc/text.conf to terminal
"""

class MyCustomException(Exception):
    def __init__(self, errormessage):
        Exception.__init__(self,errormessage)
        self.errormessage = errormessage



def printtext():
    filetoread = "etc/text.conf"
    print('-'*20)
    try:
        with open(filetoread, 'rt') as infile:
            for line in infile:
                print(line.strip())
        print('-'*20)
    except Exception, e:
        raise MyCustomException("Wrong file")



