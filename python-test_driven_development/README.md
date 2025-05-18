# Python - Test-driven Development

This project is about writing tests before writing the actual code. It follows the Test-Driven Development (TDD) approach to ensure code correctness and handle edge cases effectively.

## Learning Objectives

- Understand why tests are important.
- Use `doctest` to write interactive tests.
- Use `unittest` for unit testing in Python.
- Write clear docstrings for functions and modules.
- Think about edge cases before implementing code.

## Project Requirements

- Python 3.8.5
- Files must be executable and end with a new line.
- No external libraries are allowed unless specified.
- Use `pycodestyle` (version 2.7.*) for code style checks.
- All tests must be inside the `tests/` folder.

## File Structure

```
python-test_driven_development/
├── 0-add_integer.py
├── 2-matrix_divided.py
├── 3-say_my_name.py
├── 4-print_square.py
├── 5-text_indentation.py
├── 6-max_integer.py
├── tests/
│   ├── 0-add_integer.txt
│   ├── 2-matrix_divided.txt
│   ├── 3-say_my_name.txt
│   ├── 4-print_square.txt
│   ├── 5-text_indentation.txt
│   └── 6-max_integer_test.py
└── README.md
```

## How to Run Tests

Run all `doctest` tests:

```bash
python3 -m doctest -v ./tests/*
```

Run the `unittest` test file:

```bash
python3 -m unittest tests.6-max_integer_test
```

## Usage

Each `.py` file contains a function or utility with corresponding tests. Functions handle type checking and error handling based on specifications.

## Author

GitHub: [maram-ra](https://github.com/maram-ra)
