#!/usr/bin/python3
""" Contains a method """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    def valid(byte):
        """ Checks if byte is a continuation byte """
        return byte >> 6 == 0b10

    def check_bytes(count):
        """ Checks next count bytes """
        for _ in range(count):
            if not data or not valid(data.pop(0)):
                return False
        return True

    data = list(data)
    while data:
        first = data.pop(0)
        if first >> 7 == 0:
            continue
        elif first >> 5 == 0b110:
            if not check_bytes(1):
                return False
        elif first >> 4 == 0b1110:
            if not check_bytes(2):
                return False
        elif first >> 3 == 0b11110:
            if not check_bytes(3):
                return False
        else:
            return False
    return True
