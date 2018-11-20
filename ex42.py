## Animal is-a object (yes , sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-a
class Dog(Animal):

    def __init__(self,name):
        ## ??
        self.name = name

## has-a
class Cat(Animal):

    def __init__(self,name):
        ## ??
        self.name = name

## is-a
class Person(object):

    def __init__(self,name):
        ## ??
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## has-a
class Employee(Person):

    def __init__(self,name,salary):
        ## ?? hmm what is this sstrange magic?
        super(Employee,self).__init__(name)
        ## ??
        self.salary = salary

## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## has-a
satan = Cat("Satan")

## has-a
mary = Person("Mary")

## has-a
mary.pet = satan

## has-a
frank = Employee("Frank",120000)

## has-a
frank.pet = rover

## has-a
flipper = Fish()

## has-a
crouse = Salmon()

## has-a
harry = Halibut()
