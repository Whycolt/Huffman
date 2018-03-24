from nodes import HuffmanNode, ReadNode

def get_codes(tree):
    """ Return a dict mapping symbols from Huffman tree to codes.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: dict(int,str)

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> d = get_codes(tree)
    >>> d == {3: "0", 2: "1"}
    True
    """
    return parse_tree(tree, "")
        
def parse_tree(node, code, codict={}):
    dict1, dict2 = {}, {}
    if node.is_leaf:
        codict[node.symbol] = code
        return codict
    if node.left:
        dict1 = parse_tree(node.left, code+"0", codict)
    if node.right:
        dict2 = parse_tree(node.right, code+"1", codict)
    return {**dict1, **dict2}

tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
d = get_codes(tree)
print(d == {3: "0", 2: "1"})

def avg_length(tree, freq_dict):
    """ Return the number of bits per symbol required to compress text
    made of the symbols and frequencies in freq_dict, using the Huffman tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: float

    >>> freq = {3: 2, 2: 7, 9: 1}
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(9)
    >>> tree = HuffmanNode(None, left, right)
    >>> avg_length(tree, freq)
    1.9
    """
    newdict = get_codes(tree)
    totalbits = 0
    totalchar = 0
    for i in newdict:
        print(i , "lmao")
        totalbits = totalbits + len(str(newdict[i]))*freq_dict[i]
        totalchar = totalchar + freqdict[i]
    return totalbits/totalchar

freq = {3: 2, 2: 7, 9: 1}
left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
right = HuffmanNode(9)
tree = HuffmanNode(None, left, right)
print(avg_length(tree, freq))
1.9
