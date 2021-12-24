def build_map(**kwargs):
    """
    kwargs - key-word args
    """
    print("Len:", len(kwargs))
    print("Type:", type(kwargs))
    print("Value:", kwargs)

build_map(k = 2, name = 7, bob = "Bob", foo = True, buzz = None, qwerty = [])