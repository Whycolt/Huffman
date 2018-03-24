from nodes import HuffmanNode, ReadNode
def get_bit(byte, bit_num):
    """ Return bit number bit_num from right in byte.

    @param int byte: a given byte
    @param int bit_num: a specific bit number within the byte
    @rtype: int

    >>> get_bit(0b00000101, 2)
    1
    >>> get_bit(0b00000101, 1)
    0
    """
    return (byte & (1 << bit_num)) >> bit_num


def byte_to_bits(byte):
    """ Return the representation of a byte as a string of bits.

    @param int byte: a given byte
    @rtype: str

    >>> byte_to_bits(14)
    '00001110'
    """
    return "".join([str(get_bit(byte, bit_num))
                    for bit_num in range(7, -1, -1)])


def bits_to_byte(bits):
    """ Return int represented by bits, padded on right.

    @param str bits: a string representation of some bits
    @rtype: int

    >>> bits_to_byte("00000101")
    5
    >>> bits_to_byte("101") == 0b10100000
    True
    """
    return sum([int(bits[pos]) << (7 - pos)
                for pos in range(len(bits))])

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

def tree_to_bytes(tree):
    """ Return a bytes representation of the Huffman tree rooted at tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes

    The representation should be based on the postorder traversal of tree
    internal nodes, starting from 0.
    Precondition: tree has its nodes numbered.

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2]
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(5)
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2, 1, 0, 0, 5]
    """
    items = []
    left = False
    lleaf = False
    right = False
    rleaf = False
    if tree.left != None:
        left = True
        if not tree.left.is_leaf():
            a = tree_to_bytes(tree.left)
            for i in a:
                items.append(i)
        else:
            lleaf = True
    if tree.right != None:
        right = True
        if not tree.right.is_leaf():
            a = tree_to_bytes(tree.right)
            for i in a:
                items.append(i)
        else:
            rleaf = True
    if left:
        if lleaf:
            items.append(0)
            items.append(tree.left.symbol)
        else:
            items.append(1)
            items.append(tree.left.number)
    if left:
        if rleaf:
            items.append(0)
            items.append(tree.right.symbol)
        else:
            items.append(1)
            items.append(tree.right.number)
    return bytes(items)

tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
number_nodes(tree)
print(list(tree_to_bytes(tree)))
[0, 3, 0, 2]
left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
right = HuffmanNode(5)
tree = HuffmanNode(None, left, right)
number_nodes(tree)
print(list(tree_to_bytes(tree)))
[0, 3, 0, 2, 1, 0, 0, 5]
    
