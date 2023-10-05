def test_product():
    assert product(2,2,2)==8


def test_longest():
    assert longest([1,1,1],[1,1])==[1,1,1]

def test_distance():
    assert distance((1,1),(1,2))==1
    assert distance((1,1),(1,1))==0