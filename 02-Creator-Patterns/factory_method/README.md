# Factory Method Design Pattern

## Type
Creator Design Patterns provide interfaces for creating objects, ensuring that concrete classes are separated from the code that uses them. They promote flexibility, encapsulation, and loose coupling. Common examples include Factory Method, Abstract Factory, and Builder patterns.


## Definitions

### Product:

In the context of the Factory Method pattern, the Product is an interface or abstract class that defines the contract (i.e., methods and properties) for objects the factory method will create. It represents the type of objects the factory method is responsible for producing.

- Notification (abstract class): This is the product interface that declares the send method.

### Concrete Products:

These are the specific implementations of the Product interface or abstract class. A Concrete Product is a specific variant or type of the product that the factory method produces. It implements or extends the Product to provide the functionality specific to that particular product variant.

- SMS and Email: These are the concrete implementations of the Notification product interface. They both implement the send method specific to their type.

### Creator:

The Creator, in the Factory Method pattern, is an interface or abstract class that declares the factory method. This method returns an object of type Product. The Creator may also provide a default implementation of the factory method. It might also contain other methods that work with products, but the primary responsibility is to provide the factory method.

- NotificationFactory (abstract class): This is the creator interface that declares the create_notification method and provides a default implementation of the notify method which utilizes the product.

### Concrete Creators:

These are specific implementations of the Creator interface or abstract class. A Concrete Creator overrides the factory method to return a specific Concrete Product. It is responsible for creating and returning an instance of a particular Concrete Product.

- SMSNotificationFactory and EmailNotificationFactory: These are the concrete implementations of the NotificationFactory creator interface. They both override the create_notification method to instantiate and return their respective concrete products (SMS and Email).


## Descriptions

When to use: 
- You don’t know the exact type of object you want to have
- Provide API to your codebase, making sure that other developers can extend internal component
 When you want to reuse objects that you created to save system’s resource

Pros:
- Offers flexibility in creating different objects and can be easily extended to produce different objects based on conditions
- Helps to reduce tight coupling between classes by providing an interface to create instances rather than directly using constructors
- Encourages code reusability and is easier to maintain since the creation logic is centralized

Cons:
- Can increase the overall complexity of the code if used unnecessarily
