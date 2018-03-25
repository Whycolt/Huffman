def make_freq_dict(text):
    """ Return a dictionary that maps each byte in text to its frequency.

    @param bytes text: a bytes object
    @rtype: dict(int,int)

    >>> d = make_freq_dict(bytes([65, 66, 67, 66]))
    >>> d == {65: 1, 66: 2, 67: 1}
    True
    """
    d = {}
    for i in text:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d

d = make_freq_dict(bytes([65, 66, 67, 66]))
print(d == {65: 1, 66: 2, 67: 1})
