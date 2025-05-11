# Python - Import & Modules

This project covers the basics of using modules in Python. It includes importing functions, using command line arguments, and understanding how Python scripts behave when imported vs. executed directly.

## Key Concepts

- `import`: How to reuse code from other Python files.
- `from x import y`: Import specific functions or variables.
- `__name__ == "__main__"`: Prevent code from running when imported.
- `sys.argv`: Handle command-line arguments.
- `dir()`: List all names in a module.
- Creating and using `.py` files as modules.

## What I Learned

- Reusing logic by importing functions from other files.
- Writing clean and modular code.
- Controlling script behavior when used as a module.
- Handling inputs from the terminal using `sys.argv`.

## Files & Functions

| File | Description |
|------|-------------|
| `0-add.py` | Imports `add(a, b)` from `add_0.py` and prints `1 + 2 = 3` |
| `1-calculation.py` | Imports all calculator functions and prints results using `a = 10`, `b = 5` |
| `2-args.py` | Prints number of arguments and lists them |
| `3-infinite_add.py` | Adds all command line arguments together |
| `4-hidden_discovery.py` | Lists defined names in a compiled module, skips dunder names |
| `5-variable_load.py` | Imports variable `a` from another file and prints it |

## Usage

Make sure each file is executable:
```bash
chmod +x filename.py
