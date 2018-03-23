from nodes import HuffmanNode, ReadNode
def number_nodes(tree):
    """ Number internal nodes in tree according to postorder traversal;
    start numbering at 0.

    @param HuffmanNode tree:  a Huffman tree rooted at node 'tree'
    @rtype: NoneType

    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(None, HuffmanNode(9), HuffmanNode(10))
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> tree.left.number
    0
    >>> tree.right.number
    1
    >>> tree.number
    2
    """
    parse_num(tree,0)

def parse_num(node,counter):
    if node.symbol != None:
        return counter
    counter = parse_num(node.left,counter)
    counter = parse_num(node.right,counter)
    node.number = counter
    counter = counter + 1
    return counter

left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
right = HuffmanNode(None, HuffmanNode(9), HuffmanNode(10))
tree = HuffmanNode(None, left, right)
number_nodes(tree)
print(tree.left.number)

print(tree.right.number)

print(tree.number)
