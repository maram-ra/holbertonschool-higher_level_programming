# Python - Exceptions

## Overview

This project is about one important idea: writing Python code that doesn’t break when something goes wrong.

You'll learn how to handle errors, raise your own exceptions, and make sure your code runs smoothly even when unexpected things happen. This is the kind of skill that makes your code more reliable and your mindset more professional.

## What You’ll Learn

- The difference between errors and exceptions
- How exceptions work in Python
- When and why to use `try / except`
- What `finally` is used for
- How to raise built-in exceptions
- How to clean up after something fails

## Rules

- Python 3.8.5 on Ubuntu 20.04
- All files must start with: `#!/usr/bin/python3`
- Use `pycodestyle` (2.7.\*)
- No external modules
- No using `len()` unless told
- Every file must be executable


## Tasks

### 0. Safe List Print  
Print up to `x` elements from a list using `try / except`.  
Returns the actual number of elements printed.  
No `len()`.

### 1. Safe Integer Print  
Prints the value if it’s an integer using `"{:d}".format()`.  
Returns `True` if successful, `False` if not.  
No `type()`.

### 2. Print & Count Integers  
Only prints integers from the first `x` elements in a list.  
Skips anything else.  
Returns how many integers were printed.

### 3. Division with Debug  
Divides two integers and prints the result in a `finally` block.  
Returns the result, or `None` if something goes wrong.

### 4. Divide Two Lists  
Goes through two lists and divides each element.  
Handles wrong types, division by zero, and short lists.  
Returns a new list with the results.

### 5. Raise Exception  
Simple function that raises a `TypeError`.

### 6. Raise Exception with Message  
Raises a `NameError` with a custom message.
