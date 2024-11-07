# Python Intermediate Concepts Cheat Sheet

# -----------------------------
# 1. LAMBDA FUNCTIONS
# -----------------------------
print("\n=== Lambda Functions ===")

# Basic lambda
square = lambda x: x**2
print(f"Lambda square of 5: {square(5)}")

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(f"Lambda multiply 4 * 3: {multiply(4, 3)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Map with lambda (doubled numbers): {doubled}")

# -----------------------------
# 2. DECORATORS
# -----------------------------
print("\n=== Decorators ===")

def timer_decorator(func):
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__} took {end-start:.4f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

print("\nTesting decorator:")
slow_function()

# -----------------------------
# 3. GENERATORS
# -----------------------------
print("\n=== Generators ===")

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nFibonacci using generator:")
fib = fibonacci_generator(5)
for num in fib:
    print(num, end=" ")
print()  # New line

# Generator expression
squares_gen = (x**2 for x in range(5))
print(f"Generator expression results: {list(squares_gen)}")

# -----------------------------
# 4. CONTEXT MANAGERS
# -----------------------------
print("\n=== Context Managers ===")

# Custom context manager
from contextlib import contextmanager

@contextmanager
def custom_context():
    print("Entering context")
    try:
        yield "Context value"
    finally:
        print("Exiting context")

print("\nUsing custom context manager:")
with custom_context() as value:
    print(f"Inside context with value: {value}")

# -----------------------------
# 5. CLASS ADVANCED CONCEPTS
# -----------------------------
print("\n=== Advanced Class Concepts ===")

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    # Property decorator
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    # Magic/Dunder methods
    def __str__(self):
        return f"{self.celsius}°C"
    
    def __add__(self, other):
        return Temperature(self.celsius + other.celsius)

# Testing the Temperature class
temp = Temperature(25)
print(f"\nTemperature: {temp}")
print(f"In Fahrenheit: {temp.fahrenheit}°F")

# -----------------------------
# 6. ADVANCED COLLECTIONS
# -----------------------------
print("\n=== Advanced Collections ===")

from collections import Counter, defaultdict, namedtuple

# Counter
text = "mississippi"
char_count = Counter(text)
print(f"\nCounter example: {char_count}")

# defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(f"defaultdict example: {dict(dd)}")

# namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'New York')
print(f"namedtuple example: {person}")
print(f"Accessing namedtuple field: {person.name}")

# -----------------------------
# 7. ADVANCED COMPREHENSIONS
# -----------------------------
print("\n=== Advanced Comprehensions ===")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"\nDictionary comprehension: {squares_dict}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Set comprehension
words = ['hello', 'world', 'hello', 'python']
unique_lengths = {len(word) for word in words}
print(f"Unique word lengths: {unique_lengths}")

# -----------------------------
# 8. ADVANCED ARGUMENT HANDLING
# -----------------------------
print("\n=== Advanced Arguments ===")

def advanced_args(*args, **kwargs):
    print(f"\nPositional args: {args}")
    print(f"Keyword args: {kwargs}")

advanced_args(1, 2, 3, name='Alice', age=30)

# Unpacking operators
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(f"Unpacked lists: {combined}")

dict1 = {'a': 1}
dict2 = {'b': 2}
combined_dict = {**dict1, **dict2}
print(f"Unpacked dictionaries: {combined_dict}")