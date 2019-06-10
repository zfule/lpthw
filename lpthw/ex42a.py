class A(object):
    def add (self, x):
        y = x + 1
        print(y)

## a = A()
## a.add(2)

class B(A):
    def add(self, x):
        super().add(x)

print(super(B,A))

b = B()
b.add(2)
