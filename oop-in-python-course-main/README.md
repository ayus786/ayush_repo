# Python OOP: Object Oriented Programming From Beginner to Pro

This is the code repo containing all of the examples covered in the course. I strongly recommend you to code out all of the examples as you follow this course.

## To download and use this repo:

1. Open up a terminal
2. Download the repo to your computer with `git clone https://github.com/DoableDanny/oop-in-python-course.git`
3. Open up the project with your text editor, e.g. VS Code

Example commands for how to run the examples:

- `python -m solid.single_responsibility_principle.naive_solution`
- `python -m design_patterns.abstract_factory_pattern.naive_solution.app.main`

## Below is some extra material that I didn't add to the course that you may find useful as you advance through the course...

## Types

Programming languages use different **type systems** to manage how data is classified and manipulated. The type system determines how strictly types are enforced, when they are checked, and how flexible they are. Below are the **different kinds of typing systems**, with examples.

---

### 1. Static vs. Dynamic Typing

This distinction is about **when type checking** is performed—**at compile-time or runtime**.

- **Static Typing**: Types are checked at **compile-time**. Errors are caught before the program runs.

  - **Examples**: Java, C#, C++, TypeScript, Swift
  - **Pro**: Catch type errors early, improving safety and performance.
  - **Con**: Requires more code to declare types.

  **Example (Java):**

  ```java
  int x = "hello";  // Compile-time error: incompatible types
  ```

- **Dynamic Typing**: Types are checked at **runtime**. Errors occur only when the program runs.

  - **Examples**: Python, JavaScript, Ruby, PHP
  - **Pro**: Code is easier to write and more flexible.
  - **Con**: Type errors may only appear during execution, which can cause bugs.

  **Example (Python):**

  ```python
  x = "hello"
  x = 123  # No error at assignment time, but bugs may appear later.
  ```

---

### 2. Strong vs. Weak Typing

This distinction deals with **how strictly** the language enforces types.

- **Strong Typing**: The language does **not allow implicit type conversions** that might lead to unexpected behavior. Types must be explicitly converted.

  - **Examples**: Python, Java, Ruby
  - **Pro**: Reduces bugs caused by unintended type coercion.
  - **Con**: Requires more careful handling of types.

  **Example (Python):**

  ```python
  print("The number is: " + 123)  # TypeError: cannot concatenate str and int
  ```

- **Weak Typing**: The language **allows implicit type conversions** (coercion), often without the developer’s awareness.

  - **Examples**: JavaScript, PHP, C
  - **Pro**: Code is more concise and flexible.
  - **Con**: Can cause subtle bugs due to unintended type conversions.

  **Example (JavaScript):**

  ```javascript
  console.log("The number is: " + 123); // Implicit conversion to string: "The number is: 123"
  ```

---

### 3. Nominal vs. Structural Typing

This distinction is about **how compatibility** between types is determined.

- **Nominal Typing**: Compatibility is based on **explicit declarations**—types are compatible only if they are declared to be related (e.g., by inheritance or interfaces).

  - **Examples**: Java, C#, Swift
  - **Pro**: Ensures clear relationships between types.
  - **Con**: Can be verbose and rigid.

  **Example (Java):**

  ```java
  class Dog {}
  class Cat {}

  Dog d = new Cat();  // Compile-time error: incompatible types
  ```

- **Structural Typing**: Compatibility is based on **type structure**—two types are compatible if they have the same shape or properties, regardless of their declared relationships.

  - **Examples**: TypeScript, Go, Python (duck typing)
  - **Pro**: More flexible; focuses on what an object can do, rather than what it is.
  - **Con**: Can lead to less predictable code.

  **Example (TypeScript):**

  ```typescript
  type Animal = { sound: () => void };
  const cat = { sound: () => console.log("Meow") };

  let animal: Animal = cat; // Works because it has the same structure
  ```

---

### 4. Manifest vs. Inferred Typing

This distinction focuses on whether **types need to be explicitly declared** by the programmer or are inferred by the compiler.

- **Manifest Typing**: Types must be **explicitly declared** by the programmer.

  - **Examples**: Java, C#, TypeScript (with strict mode)
  - **Pro**: Makes code more readable and predictable.
  - **Con**: Can result in verbose code.

  **Example (Java):**

  ```java
  int x = 10;  // Type explicitly declared
  ```

- **Inferred Typing**: The compiler or interpreter **infers the type** based on the assigned value, so the programmer doesn’t need to declare it explicitly.

  - **Examples**: Python, JavaScript, TypeScript (without strict mode)
  - **Pro**: Less code to write.
  - **Con**: Can make the code harder to understand or debug.

  **Example (Python):**

  ```python
  x = 10  # Type inferred as int
  ```

---

### 5. Duck Typing

This is a type system where **an object’s compatibility** is determined by the presence of certain methods or properties, rather than its actual type.

- **Examples**: Python, JavaScript, Ruby
- **Pro**: Promotes flexibility.
- **Con**: Errors might not surface until runtime.

  **Example (Python):**

  ```python
  class Dog:
      def sound(self):
          print("Woof")

  class Cat:
      def sound(self):
          print("Meow")

  def make_sound(animal):
      animal.sound()  # Works as long as the object has a 'sound' method

  make_sound(Dog())  # Woof
  make_sound(Cat())  # Meow
  ```

---

### 6. Gradual Typing

This is a mix of **static and dynamic typing**. The programmer can choose whether to use types, and the language can optionally enforce type checking.

- **Examples**: TypeScript, Python (with `mypy`), PHP (since v7)
- **Pro**: Provides flexibility to add type checks incrementally.
- **Con**: Can be harder to maintain consistency between typed and untyped parts.

  **Example (Python with `mypy`):**

  ```python
  def greet(name: str) -> str:
      return f"Hello, {name}"

  greet(123)  # mypy will flag this as an error
  ```

---

### Summary Table of Typing Systems

| **Type System**        | **Description**                                     | **Examples**                            |
| ---------------------- | --------------------------------------------------- | --------------------------------------- |
| Static vs. Dynamic     | When types are checked (compile-time vs. runtime)   | Java (static), Python (dynamic)         |
| Strong vs. Weak        | How strictly types are enforced                     | Python (strong), JS (weak)              |
| Nominal vs. Structural | How type compatibility is determined                | Java (nominal), TypeScript (structural) |
| Manifest vs. Inferred  | Whether types must be explicitly declared           | Java (manifest), Python (inferred)      |
| Duck Typing            | Compatibility based on methods/properties, not type | Python, JavaScript                      |
| Gradual Typing         | Supports both static and dynamic typing             | TypeScript, Python (`mypy`)             |

---

### **Conclusion**

Different languages adopt different **type systems** based on their design goals. Some languages prioritize **safety and predictability** (e.g., Java, C#), while others emphasize **flexibility and ease of use** (e.g., Python, JavaScript). Understanding these different type systems helps you pick the right tool for the job and write more effective code.

## **@abstractmethod -- What Happens Under the Hood?**

When you use the **`@abstractmethod` decorator**, Python makes a few internal checks and changes. Here’s a step-by-step breakdown of what it does:

1. **Sets a special flag** on the method to mark it as abstract.

   - This is done by adding a special attribute **`__isabstractmethod__ = True`** to the method. This flag is used by Python to track whether the method is abstract.

2. **Marks the class as abstract** if it contains any `@abstractmethod`s.

   - When the class containing the `@abstractmethod` is defined, Python ensures that the class is marked as **abstract**. This means that you **cannot instantiate** the class directly.

3. **Checks for subclass implementations** at instantiation.
   - When you try to **instantiate a subclass** of an abstract class, Python checks whether **all abstract methods** have been implemented. If not, it raises a **`TypeError`**.

---

### Code Explanation of `@abstractmethod` Internals

Here’s a minimal version of what **`@abstractmethod`** does internally.

#### **How `@abstractmethod` Works Internally (Simplified)**

```python
def abstractmethod(func):
    """Mark a method as abstract by setting a special attribute."""
    func.__isabstractmethod__ = True
    return func
```

This **decorator sets the `__isabstractmethod__` attribute** on the method, marking it as abstract.

---

## How Python Checks Abstract Methods in the Class

When Python defines a class that inherits from `ABC`, it checks **all the methods** to see if **`__isabstractmethod__` is `True`**.

If any abstract methods are not implemented in a subclass, Python raises a **`TypeError`** when trying to instantiate the class. Internally, this is done using the **`ABCMeta` metaclass**, which ensures that **abstract methods must be implemented** before the class can be instantiated.

---

### **Example with Debugging: Inspect Abstract Methods**

Here’s how you can **inspect the abstract methods** behind the scenes:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

print(Shape.calculate_area.__isabstractmethod__)  # Output: True
```

- When the `@abstractmethod` decorator is applied, **`__isabstractmethod__`** is set to `True`.

---

### What Happens if the Abstract Method Is Not Implemented?

If you try to **instantiate a subclass** without implementing the abstract method, Python raises a **`TypeError`**.

```python
class Circle(Shape):
    pass  # No implementation of calculate_area()

circle = Circle()  # TypeError: Can't instantiate abstract class Circle with abstract method calculate_area
```

This behavior is enforced by **`ABCMeta`**, the metaclass that `ABC` uses to define abstract classes.

---

### Summary

- **`@abstractmethod`** marks a method with **`__isabstractmethod__ = True`**.
- Python uses **`ABCMeta`** (a metaclass) to **ensure abstract methods are implemented** in subclasses.
- If an abstract method is not implemented, Python raises a **`TypeError`** at **instantiation time**.

This is how **Python enforces the concept of abstract methods and abstract base classes**, ensuring that certain methods are always implemented in subclasses.

---
