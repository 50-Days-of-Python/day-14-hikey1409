import main;

def test():
    assert main.flat_list([[53,267,89]]) == [53,267,89]
def test2():
    assert main.flat_list([[1,2,3],[4,5,6]]) == [1,2,3,4,5,6]
def test3():
    assert main.flat_list([[76,12],[554]]) == [76,12,554]
