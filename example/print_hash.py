
from example.foo import baz, Foo

from codedep import getHash

print 'hash of baz = %s' % getHash(baz)
print 'hash of Foo = %s' % getHash(Foo)

foo = Foo(2)
print 'value1 = %s' % foo.value1()
print 'value2 = %s' % foo.value2()
