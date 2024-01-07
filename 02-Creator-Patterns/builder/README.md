# Builder Design Pattern

## Type

The Builder Pattern is a design pattern used to construct complex objects step by step. It's part of the Gang of Four design patterns, often used when an object needs to be created with many possible configurations and a clear separation between its construction and representation.

## Definitions

### Builder

An abstract interface that specifies methods for creating the different parts of a Product.

### Concrete Builder

Implements the Builder interface, providing specific implementations for the building steps. It keeps the product being created.

### Director

Responsible for managing the construction process. It accepts a Builder instance and executes the necessary operations to build an object.

### Product

The complex object that is being built. The final output of the Builder Pattern.

## Descriptions

When to use:

- Get rid of "telescopic constructor"
- Need state in constructor
- different representations of some product

Pros:

- Separation of Concerns: Decouples the construction of a complex object from its representation.
- Flexibility: Can construct different representations of an object using the same construction process.
- Readability: Increases readability, especially when creating objects with numerous attributes.

Cons:

- Complexity: Adds complexity to the codebase with multiple additional classes and interfaces.
- Mutability: The product is usually mutable, which might lead to issues and bugs in state of mismatch between builders.
- Overhead: Not efficient for simpler objects, as it can lead to unnecessary boilerplate code.
