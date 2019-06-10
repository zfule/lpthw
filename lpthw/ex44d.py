class Parent():

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("Child override()")

    def altered(self):
        print("CHILD, before PARENT altered()")
        super(Child, self).altered()
        print("CHILD, after PARENT altered()")

dad = Parent()
son = Child()

# 这是一覆盖
dad.override()
son.override()

# 这是继承
dad.implicit()
son.implicit()

# 它不仅继承了添加了新的玩意儿
dad.altered()
son.altered()
