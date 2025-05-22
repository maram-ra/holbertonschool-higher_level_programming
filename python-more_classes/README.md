# Python - More Classes and Objects

This project continues the exploration of Object-Oriented Programming (OOP) in Python by building a robust and fully featured `Rectangle` class.

## 📚 Concepts Covered

- Class vs Instance Attributes
- Data encapsulation and property management
- `__str__()` vs `__repr__()`
- Object deletion and destructors
- Class methods and static methods
- Custom behavior for comparison and factory methods
- Pythonic approach to getters/setters using `@property`

## 🧠 Learning Objectives

By the end of this project, I was able to explain:

- What is OOP and how Python supports it
- How attributes and methods work inside a class
- Difference between class attributes and instance attributes
- When to use `@classmethod` vs `@staticmethod`
- The purpose of `__init__`, `__str__`, `__repr__`, and `__del__`
- How `__dict__` reflects the internal namespace of an instance
- How `getattr()` works to retrieve attributes dynamically

## 🛠️ Requirements

- Python 3.8.5
- Code must follow `pycodestyle` (v2.7.*)
- No module imports allowed
- Each file must be executable and end with a new line

## 🚀 File Breakdown

| File             | Description |
|------------------|-------------|
| `0-rectangle.py` | Defines an empty `Rectangle` class |
| `1-rectangle.py` | Adds width and height as private attributes with getters/setters |
| `2-rectangle.py` | Adds methods to compute area and perimeter |
| `3-rectangle.py` | Implements `__str__()` for string display using `#` |
| `4-rectangle.py` | Adds `__repr__()` to allow recreation using `eval()` |
| `5-rectangle.py` | Adds `__del__()` to print a message on deletion |
| `6-rectangle.py` | Adds a class attribute to track instance count |
| `7-rectangle.py` | Adds customizable `print_symbol` for string representation |
| `8-rectangle.py` | Adds `bigger_or_equal()` static method to compare rectangles |
| `9-rectangle.py` | Adds `square()` class method to create square instances |

## 💡 Example Usage

```python
r1 = Rectangle(3, 2)
print(r1)  # ###
           # ###
print(Rectangle.number_of_instances)  # e.g. 1
r2 = Rectangle.square(5)
print(r2.area())  # 25
