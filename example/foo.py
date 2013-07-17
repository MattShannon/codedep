
from codedep import codeDeps, ForwardRef

@codeDeps(ForwardRef(lambda: qux))
def bar(x):
    return qux(x + 1)

@codeDeps()
def qux(x):
    return x * 2

@codeDeps(qux)
def baz(x):
    return qux(x - 2)

@codeDeps(bar, baz)
class Foo(object):
    def __init__(self, x):
        self.x = x

    def value1(self):
        return bar(self.x)

    def value2(self):
        return baz(self.x)
