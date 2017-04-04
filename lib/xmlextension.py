from lxml import etree
import pprint

""" Prints content of a specific tag
"""

def read_document():
    myfile = "etc/text.xml"
    return etree.parse(myfile)


def search_tag_in_node(node, tag):
    """ Recurse node children to find printable end-nodes
    """
    if (len(node.getchildren())) == 0:
        if node.tag == tag:
            print(node.tag, node.text)
    else:
        for item in node.getchildren():
            search_tag_in_node(item, tag)


def processxml(search_tag):
    xmldoc = read_document()
    search_tag_in_node(xmldoc.getroot(), search_tag)
