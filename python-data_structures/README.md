# Python - Data Structures: Lists, Tuples

##  Curriculum
**Foundations v2.1 - Part 2**  
Average: 100%  
Project Badge: 🟢  
Author: Guillaume  
Weight: 1

---

##  Learning Objectives

At the end of this project, you should be able to explain:

- What are lists and how to use them.
- Differences and similarities between strings and lists.
- Common list methods and how to use them.
- How to use lists as stacks and queues.
- What list comprehensions are and how to use them.
- What tuples are and how to use them.
- When to use tuples vs lists.
- What is a sequence.
- What is tuple packing and unpacking.
- What the `del` statement does and how to use it.

---

##  Requirements

- **Language:** Python 3.8.5
- **OS:** Ubuntu 20.04 LTS
- Files must start with `#!/usr/bin/python3`
- All files must end with a new line
- Follow [pycodestyle](https://pypi.org/project/pycodestyle/) (version 2.7.\*)
- No imports unless specified
- No use of built-in methods unless allowed
- All files must be executable
- `README.md` is mandatory

---

##  Tasks Summary

### 0. Print a list of integers
Function: `print_list_integer(my_list=[])`  
 Prints each integer in a list using `str.format()`.

---

### 1. Secure access to an element in a list
Function: `element_at(my_list, idx)`  
 Returns element at index `idx` or `None` if invalid.

---

### 2. Replace element
Function: `replace_in_list(my_list, idx, element)`  
 Replaces element at index `idx` without errors if index is out of range.

---

### 3. Print a list in reverse
Function: `print_reversed_list_integer(my_list=[])`  
 Prints the list in reverse using `str.format()`.

---

### 4. Replace in a copy
Function: `new_in_list(my_list, idx, element)`  
 Returns a new list with a replaced element, original stays unchanged.

---

### 5. Remove 'c' and 'C'
Function: `no_c(my_string)`  
 Returns a string with all 'c' and 'C' removed.

---

### 6. Print matrix of integers
Function: `print_matrix_integer(matrix=[[]])`  
 Nicely prints a 2D matrix of integers.

---

### 7. Tuples addition
Function: `add_tuple(tuple_a=(), tuple_b=())`  
 Adds two tuples element-wise (first two elements only).

---

### 8. More returns!
Function: `multiple_returns(sentence)`  
 Returns a tuple: (length of string, first character or `None`).

---

### 9. Find the max
Function: `max_integer(my_list=[])`  
 Finds the largest integer in a list or returns `None`.

---

### 10. Only by 2
Function: `divisible_by_2(my_list=[])`  
 Returns a list of booleans indicating if values are divisible by 2.

---

### 11. Delete at
Function: `delete_at(my_list=[], idx=0)`  
 Deletes an element at a given index safely.

---

### 12. Switch
Script: `12-switch.py`  
 Switches the values of `a` and `b` using tuple unpacking.

---

##  Repository Structure

```bash
holbertonschool-higher_level_programming/
└── python-data_structures/
    ├── 0-print_list_integer.py
    ├── 1-element_at.py
    ├── 2-replace_in_list.py
    ├── 3-print_reversed_list_integer.py
    ├── 4-new_in_list.py
    ├── 5-no_c.py
    ├── 6-print_matrix_integer.py
    ├── 7-add_tuple.py
    ├── 8-multiple_returns.py
    ├── 9-max_integer.py
    ├── 10-divisible_by_2.py
    ├── 11-delete_at.py
    ├── 12-switch.py
    └── README.md
