# Python OOP — Abstract Classes, Interfaces & Inheritance

This repo explores real OOP in Python. Not just syntax — the mindset behind it.

You’ll use:
- **Abstract classes** to enforce structure.
- **Interfaces & duck typing** to build flexible systems.
- **Subclassing built-ins** to control behavior.
- **Method overriding** to customize logic.
- **Multiple inheritance** to combine roles.
- **Mixins** to keep things modular and clean.

## Tasks Breakdown

### 0. Animal (Abstract Base)

Define an abstract `Animal` class with one abstract method: `sound()`.  
Subclasses `Dog` and `Cat` override it with "Bark" and "Meow".

Trying to instantiate `Animal` directly raises a `TypeError`.

### 1. Shape Interface & Duck Typing

Define a `Shape` ABC with `area()` and `perimeter()`.  
Implement `Circle` and `Rectangle`.  
Then write `shape_info(obj)` — it just calls those two methods. No type-checking.  
If it walks like a Shape, it is a Shape.

### 2. VerboseList — Custom list with logs

Inherit from Python's list.  
Override:
- `append()` → log what was added  
- `extend()` → log how many were added  
- `remove()` → log what’s removed  
- `pop()` → log what’s popped  

This shows how to extend built-in classes while keeping their core behavior.

### 3. CountedIterator

Wrap any iterable and track how many items were fetched.  
Override `__next__` and count internally.  
Expose the count via `.get_count()`.

### 4. FlyingFish — Multiple Inheritance

Create:
- `Fish` → has `swim()` and `habitat()`  
- `Bird` → has `fly()` and `habitat()`  

Then:
- `FlyingFish(Fish, Bird)` → override all three methods  
- Print `.mro()` to show how Python resolves method calls

### 5. Dragon — Mixins in Action

Build small, focused mixins:
- `SwimMixin` → adds `swim()`  
- `FlyMixin` → adds `fly()`  

Then:
- `Dragon(SwimMixin, FlyMixin)` → combine behaviors  
- Add `.roar()` to make it yours

## Why This Matters

OOP isn’t about inheritance trees. It’s about clarity, contracts, and composition.  
This project helps you think in systems, not just classes.

## Run Examples

Each task has a `main_0x_*.py` file for quick testing.

---

