# python-inheritance

This project explores Python inheritance and how classes relate to each other through parent-child relationships.

## ✅ Learning Objectives

By the end of this project, I can clearly explain:

- What is a superclass / base class / parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- The default class every class inherits from
- How to override a method or attribute from the base class
- Which attributes or methods are available to subclasses
- The purpose of inheritance
- How and when to use `isinstance`, `issubclass`, `type`, and `super`

---

## 🧪 Project Files and Tasks

### `0-lookup.py`
Returns a list of all attributes and methods of an object.

### `1-my_list.py`
A class `MyList` that inherits from `list` and adds a `print_sorted()` method.

### `2-is_same_class.py`
Checks if an object is exactly an instance of a specific class.

### `3-is_kind_of_class.py`
Checks if an object is an instance of a class or inherits from it.

### `4-inherits_from.py`
Checks if an object is a **subclass** (not the exact class) of a given class.

### `5-base_geometry.py`
Defines an empty class `BaseGeometry`.

### `6-base_geometry.py`
Adds a public method `area()` that raises an exception: `area() is not implemented`.

### `7-base_geometry.py`
Adds `integer_validator(name, value)` to check that value is a positive integer.

### `8-rectangle.py`
Defines a class `Rectangle` that inherits from `BaseGeometry`. Validates `width` and `height`.

### `9-rectangle.py`
Same as task 8, but adds `area()` method and custom `__str__`.

### `10-square.py`
Defines class `Square` inheriting from `Rectangle`, with equal width and height.

### `11-square.py`
Extends task 10 with a custom `__str__` to show: `[Square] <width>/<height>`

---

## 🧷 Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- No external libraries
- Follows `pycodestyle` (PEP8) 2.7.*
- Files are executable and end with a new line
- All tests written using `doctest` and placed in the `tests/` directory

---

## 🧪 Testing

Run test files using:

```bash
python3 -m doctest ./tests/*
