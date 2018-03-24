<<<<<<< HEAD
from nodes import HuffmanNode, ReadNode
def huffman_tree(freq_dict):
    """ Return the root HuffmanNode of a Huffman tree corresponding
    to frequency dictionary freq_dict.

    @param dict(int,int) freq_dict: a frequency dictionary
    @rtype: HuffmanNode

    >>> freq = {2: 6, 3: 4}
    >>> t = huffman_tree(freq)
    >>> result1 = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> result2 = HuffmanNode(None, HuffmanNode(2), HuffmanNode(3))
    >>> t == result1 or t == result2
    True
    """
    new = {}
    while len(freq_dict) > 1:
        s1 = None
        s2 = None
        for i in freq_dict:
            if s1 == None or freq_dict[i] < freq_dict[s1]:
                s2 = s1
                s1 = i
            elif s2 == None or freq_dict[i] < freq_dict[s2]:
                s2 = i
        h1 = s1
        h2 = s2
        if isinstance(s1, int):
            s1 = HuffmanNode(h1)
        else:
            s1 = new[s1]
        if isinstance(s2, int):
            s2 = HuffmanNode(h2)
        else:
            s2 = new[s2]
        freq_dict[str(h1)+str(h2)]=freq_dict[h1] + freq_dict[h2]
        new[str(h1)+str(h2)] = HuffmanNode(None,s1,s2)
        freq_dict.pop(h1)
        freq_dict.pop(h2)
    for i in freq_dict:
        return new[i]

freq = {2: 6, 3: 4, 4:1,5:7}
t = huffman_tree(freq)
result1 = HuffmanNode(None,HuffmanNode(5),HuffmanNode(None, HuffmanNode(None,HuffmanNode(4),HuffmanNode(3)), HuffmanNode(2)))
print (t == result1)
=======
from nodes import HuffmanNode
def get_codes(tree):
    """ Return a dict mapping symbols from Huffman tree to codes.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: dict(int,str)

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> d = get_codes(tree)
    >>> d == {3: "0", 2: "1"}
    True
    """
    print(tree)
    return parse_tree(tree, "")
        
def parse_tree(node, code, codict={}):
    dict1, dict2 = {}, {}
    if node.is_leaf():
        print("found leaf")
        codict[node.symbol] = code
        return codict
    if node.left:
        print(node.left)
        dict1 = parse_tree(node.left, code+"0", codict)
    if node.right:
        dict2 = parse_tree(node.right, code+"1", codict)
    return {**dict1, **dict2}

tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
d = get_codes(tree)
print(d)
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
print(get_codes(tree) == freq)
>>>>>>> fe36c53e5bbe483ca5662f5674dd1fb3bfd8690d
