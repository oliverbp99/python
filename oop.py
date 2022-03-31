class Person:

    type = 'Mammel'

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) > 1:
            self.name = args[0]
            self.age = args[1]



        print(args)
        print(kwargs)
    
    def msg(self, foo = 44):
        if foo == None:
            pass
        else:
            print(foo)
