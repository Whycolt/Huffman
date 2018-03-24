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

def generate_compressed(text, codes):
    """ Return compressed form of text, using mapping in codes for each symbol.

    @param bytes text: a bytes object
    @param dict(int,str) codes: mapping from symbols to codes
    @rtype: bytes

    >>> d = {0: "0", 1: "10", 2: "11"}
    >>> text = bytes([1, 2, 1, 0])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111000']
    >>> text = bytes([1, 2, 1, 0, 2])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111001', '10000000']
    """
    convert = ""
    for i in text:
        convert = convert + codes[i]
        print(convert)
    while len(convert)%8 != 0:
        convert = convert + "0"
    print (convert)
    bytelist = []
    while len(convert)>7:
        bytelist.append(convert[:8])
        print (convert[:8])
        convert = convert[8:]
    symbollist = []
    for i in bytelist:
        symbollist.append(bits_to_byte(i))
    return bytes(symbollist)

d = {0: "0", 1: "10", 2: "11"}
text = bytes([1, 2, 1, 0])
result = generate_compressed(text, d)
print([byte_to_bits(byte) for byte in result])

text = bytes([1, 2, 1, 0, 2])
result = generate_compressed(text, d)
print([byte_to_bits(byte) for byte in result])
