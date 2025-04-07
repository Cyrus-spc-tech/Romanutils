roman_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def rtoi(s):
    total = 0
    prev_value = 0
    for char in reversed(s.upper()):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total

def itor(num):
    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ''
    for v, sym in val:
        while num >= v:
            res += sym
            num -= v
    return res
def 