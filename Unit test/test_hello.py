from hello import hello

def test_default():
    assert hello() == "hello, world"
    


def test_argument():
    assert hello("David") == "hello, David"

def test_loop():
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) == f"hello, {name}"
        

    #ต้องใช้กับ ฟังขันที่ return ให้เท่านั้น