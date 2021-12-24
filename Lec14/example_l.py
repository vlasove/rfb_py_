def mutant(*args, **kwargs):
    print(args)
    print(kwargs)


mutant(1, 2, 3, 4, a = 2, b = 3)