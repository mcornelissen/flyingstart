""" Print the contect of etc/text.conf to terminal
"""

def printtext():
    filetoread = "etc/text.conf"
    print('-'*20)
    with open(filetoread, 'rt') as infile:
        for line in infile:
            print(line.strip())
    print('-'*20)




