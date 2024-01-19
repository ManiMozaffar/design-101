# **Observer Design Pattern**

## **Type**

Behavioral Design Patterns focus on how objects interact and distribute responsibilities among themselves. They enhance communication and the assignment of responsibilities between objects. Examples include Observer, Strategy, Command, and State patterns.

## **Definitions**

### **Subject (Observable):**

In the Observer pattern, the Subject (also known as Observable) is a core component that maintains a list of its dependents, called Observers. It sends notifications to Observers when its state changes.

- Observable: This is the interface or class that maintains a collection of observers and provides methods to add, remove, and notify observers.

### **Observers:**

Observers are entities that are interested in tracking changes in the state of the Subject. When the state of the Subject changes, it notifies all its Observers.

- Observer Interface: This defines an update method that will be called when the Subject changes. Concrete Observers implement this interface.

### **Concrete Subject:**

A specific implementation of the Subject interface or class. It maintains the state and when a change in state occurs, it notifies the list of Observers.

- NewsPublisher: An example of a concrete subject that could maintain a list of news articles and notify its observers when a new article is published.

### **Concrete Observers:**

These are specific implementations of the Observer interface. They define the action to be taken when the subject's state changes.

- EmailSubscriber and RSSReader: Examples of concrete observers. An EmailSubscriber might send an email to its subscribers when it receives a notification, while an RSSReader could update its display.

## **Descriptions**

When to use:

- When changes to one object (the Subject) require changing other objects (Observers), and the number of objects involved is unknown or dynamic.
- In event handling systems where you want objects to be able to subscribe to certain events and get notified when those events occur in the REAL-TIME.
- To implement a distributed event handling system in a decoupled way.

Pros:

- Promotes the principle of loose coupling between the Subject and its Observers
- Supports the broadcasting of changes to multiple objects, ensuring consistency between the objects
- Allows for dynamic and flexible object interactions, as Observers can be added or removed at runtime
- Very useful as a strategy to push data from third party, to be observer than intruder

Cons:

- Useelss in scenario where real-time updates should be avoided
- Should not mutate the subject again, otherwise it causes implicit bugs
