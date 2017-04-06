""" Inheritance assigment

+-----+
|     |
| Foo |
|     |
+--+--+
   ^
   |
   |
+--+--+
|     |
| Bar |
|     |
+-----+

"""

class Foo:

    def __init__(self, foo_attribute):
        self.foo_attribute = foo_attribute

    def Print(self):
        for attr in vars(self):
            print "%s = %s" % (attr, getattr(self, attr))


class Bar(Foo):

     def __init__(self, bar_attribute_1, bar_attribute_2):
        self.foo_attribute = bar_attribute_1
        self.bar_attribute = bar_attribute_2


def foobar():
    print('*' * 20)
    a = Foo('123Foo456')
    a.Print();
    print('*' * 20)
    b = Bar(77777, '789Bar')
    b.Print()
    print('*' * 20)
    

