from lxml import etree
import pprint

""" Prints content of a specific tag of block
"""

def read_document():
    myfile = "etc/text.xml"
    return etree.parse(myfile)


def search_tag_in_node(node, tag):
    """ Recurse node children to find printable end-nodes
        matching the required tag
    """
    if (len(node.getchildren())) == 0:
        if node.tag == tag:
            print(node.tag, node.text)
    else:
        for item in node.getchildren():
            search_tag_in_node(item, tag)


def search_block_in_node(node, search_text):
    """ Recurse node children to find specific name
        Assumes that the name is part of the block to print

        Returns node to print all items from
    """
    if (len(node.getchildren())) == 0 and \
        node.text == search_text      and \
        node.tag  == 'name':
            return node.getparent()
    else:
        for item in node.getchildren():
            result = search_block_in_node(item, search_text)
            if result != None:
                return result


def print_and_expand(node):
    if (len(node.getchildren())) == 0:
        print(node.tag, node.text)
    else:
        for item in node.getchildren():
            print_and_expand(item)


def processxml(search_tag):
    xmldoc = read_document()
    search_tag_in_node(xmldoc.getroot(), search_tag)


def processxml_get_block(search_text):
    xmldoc = read_document()
    found_block = search_block_in_node(xmldoc.getroot(), search_text)
    if found_block != None:
        print_and_expand(found_block)
    else:
        print("Not found")


