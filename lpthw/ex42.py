## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ??Dog has-a attribute named name
        self.name = name

##?? Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ##??Cat has-a attribute named name
        self.name = name

##?? Person is-a object
class Person(object):

    def __init__(self, name):
        ##?? Person has-a attribute named name
        self.name = name

        ##P?? erson has-a pet of some kind
        self.pet = None

##?? Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##??hmm what is this strang magic?
        super(Employee, self).__init__(name)
        ##??
        self.salary = salary

##?? Fish is-a object
class Fish(object):
    pass

##?? Salmon is-a Fish
class Salmon(Fish):
    pass

##?? Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

##?? satan is-a Cat
satan = Cat("satan")

##?? mary is-a Person
mary = Person("mary")

##?? mary has-a pet attribute named satan
mary.pet = satan

##??
frank = Employee("Frank", 120000)

##?? frank has-a pet attribute named rover
frank.pet = rover

##?? flipper is-a Fish
flipper = Fish()

##?? crouse is-a Salmon
crouse = Salmon()

##?? hatty is-a Halibut
harry  = Halibut()
