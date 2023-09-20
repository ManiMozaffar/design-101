Imagine your next-door neighbor owns a pet dog named Sparky. Interestingly, both dogs and cats share a handful of characteristics: attributes like their names, genders, ages, and fur colors are common to both. Similarly, dogs and cats both breathe, sleep, and are capable of some form of movement. This suggests that we can construct a foundational "Pet" class outlining these shared traits and behaviors.

In object-oriented terminology, such a foundational class is often referred to as a "base class" or "superclass." Classes derived from this base class are called "child classes" or "subclasses." These subclasses inherit the properties and methods of the superclass, adding or modifying only those elements that are unique to them. For example, a "Dog" class might include a bark method, while a "Cat" class might feature a purr method.


A class hierarchy is an arrangement of classes in a tree-like structure.
Where each class is a "kind-of" the class it inherits from.
It models an "is-a" relationship.

In this structure, a parent class (also known as a superclass or base class)
may have one or more child classes (also known as subclasses or derived classes).


# Class Hierarchies
### Definition
A class hierarchy is an arrangement of classes in a tree-like structure, where each class is a "kind-of" the class it inherits from. It models an "is-a" relationship. In this structure, a parent class (also known as a superclass or base class) may have one or more child classes (also known as subclasses or derived classes).


# Inheritance
### Definition
Inheritance is a mechanism in OOP that allows a class to inherit attributes and methods from another class. The derived class can override or extend the functionalities of the base class. This promotes code reusability and can be used to implement elegant software designs.


Animal
|-- Mammal
    |-- Human
    |-- Dog
|-- Bird
    |-- Owl
    |-- Chicken