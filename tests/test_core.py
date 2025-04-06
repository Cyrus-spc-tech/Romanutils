from romanutils import itor,rtoi

def test_roman_to_int():
    assert rtoi('XII') == 12
    assert rtoi('IX') == 9
    assert rtoi('MCMXCIV') == 1994

def test_int_to_roman():
    assert itor(12) == 'XII'
    assert itor(9) == 'IX'
    assert itor(1994) == 'MCMXCIV'