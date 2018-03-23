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
                print("first changed")
                s2 = s1
                s1 = i
            elif s2 == None or freq_dict[i] < freq_dict[s2]:
                print("second changed")
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
        print(freq_dict)
    for i in freq_dict:
        return new[i]
                
freq = {2: 6, 3: 4}
t = huffman_tree(freq)
result1 = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
result2 = HuffmanNode(None, HuffmanNode(2), HuffmanNode(3))
print(t)
print(t == result1 or t == result2)
