# Python Intermediate Concepts Cheat Sheet

# -----------------------------
# 1. FUNCTIONAL PROGRAMMING
# -----------------------------
print("\n=== Functional Programming Concepts ===")

# Lambda Functions
square = lambda x: x**2
multiply = lambda x, y: x * y
print(f"Lambda square of 5: {square(5)}")
print(f"Lambda multiply 4 * 3: {multiply(4, 3)}")

# Map Function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
squares = list(map(square, numbers))
print(f"Map doubled: {doubled}")
print(f"Map squares: {squares}")

# Filter Function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
positive_numbers = list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2]))
print(f"Filtered even numbers: {even_numbers}")
print(f"Filtered positive numbers: {positive_numbers}")

# Reduce Function
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
product_all = reduce(lambda x, y: x * y, numbers)
print(f"Reduced sum: {sum_all}")
print(f"Reduced product: {product_all}")

# -----------------------------
# 2. DECORATOR PATTERNS
# -----------------------------
print("\n=== Decorator Patterns ===")

# Function Decorator
def timer_decorator(func):
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

# Decorator with Arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Class Decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

# Decorator Method Chaining
@timer_decorator
@repeat(3)
def example_function():
    return "Function executed"

# -----------------------------
# 3. ITERATOR PATTERNS
# -----------------------------
print("\n=== Iterator Patterns ===")

# Custom Iterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Generator Functions
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

# Generator Expressions
squares_gen = (x**2 for x in range(5))
filtered_gen = (x for x in range(10) if x % 2 == 0)

# -----------------------------
# 4. CONTEXT MANAGER PATTERNS
# -----------------------------
print("\n=== Context Manager Patterns ===")

# Context Manager Using Class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Context Manager Using Decorator
from contextlib import contextmanager

@contextmanager
def timer():
    from time import time
    start = time()
    yield
    end = time()
    print(f"Time elapsed: {end - start:.2f} seconds")

@contextmanager
def temporary_attribute(obj, name, value):
    if hasattr(obj, name):
        old_value = getattr(obj, name)
        has_old = True
    else:
        has_old = False
    
    setattr(obj, name, value)
    yield
    
    if has_old:
        setattr(obj, name, old_value)
    else:
        delattr(obj, name)

# -----------------------------
# 5. METACLASS PATTERNS
# -----------------------------
print("\n=== Metaclass Patterns ===")

# Basic Metaclass
class MetaLogger(type):
    def __new__(cls, name, bases, attrs):
        # Add logging to all methods
        for key, value in attrs.items():
            if callable(value):
                attrs[key] = cls.log_call(value)
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def log_call(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

# Abstract Base Class
from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# -----------------------------
# 6. DESCRIPTOR PATTERNS
# -----------------------------
print("\n=== Descriptor Patterns ===")

# Data Descriptor
class ValidString:
    def __init__(self, minsize=0, maxsize=None):
        self.minsize = minsize
        self.maxsize = maxsize
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        if len(value) < self.minsize:
            raise ValueError(f"String must be at least {self.minsize} chars")
        if self.maxsize and len(value) > self.maxsize:
            raise ValueError(f"String must be at most {self.maxsize} chars")
        instance.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name

# Property Decorator
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# -----------------------------
# 7. ADVANCED COLLECTIONS
# -----------------------------
print("\n=== Advanced Collections ===")

from collections import (
    Counter, defaultdict, deque, 
    ChainMap, OrderedDict, namedtuple
)

# Counter Examples
inventory = Counter(['apple', 'banana', 'apple', 'orange'])
print(f"Item count: {inventory}")
print(f"Most common: {inventory.most_common(2)}")

# defaultdict Examples
tree = lambda: defaultdict(tree)
filesystem = tree()
filesystem['user']['documents']['python']['script.py'] = 'content'

# deque Examples
history = deque(maxlen=3)
for i in range(5):
    history.append(i)
print(f"Limited history: {history}")

# ChainMap Examples
defaults = {'theme': 'dark', 'language': 'en'}
user_settings = {'language': 'fr'}
settings = ChainMap(user_settings, defaults)

# OrderedDict Examples
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od.move_to_end('first')

# -----------------------------
# 8. ADVANCED COMPREHENSIONS
# -----------------------------
print("\n=== Advanced Comprehensions ===")

# Nested Dictionary Comprehension
matrix = {{f"pos_{i}_{j}": i * j 
          for j in range(3)} 
          for i in range(3)}

# Conditional Comprehensions
numbers = [-4, -2, 0, 2, 4]
abs_even = [x for x in numbers if x % 2 == 0 if x < 0]

# Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]

# Set Comprehensions with Functions
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
primes = {x for x in range(100) if is_prime(x)}

# -----------------------------
# 9. ADVANCED ARGUMENT PATTERNS
# -----------------------------
print("\n=== Advanced Argument Patterns ===")

# Keyword-Only Arguments
def kw_only_func(*, arg1, arg2):
    return arg1 + arg2

# Positional-Only Arguments
def pos_only_func(arg1, arg2, /):
    return arg1 + arg2

# Combined Arguments
def combined_func(pos_only, /, standard, *, kw_only):
    return pos_only + standard + kw_only

# Variable Arguments with Type Enforcement
def enforce_types(*types, **typed_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check positional args
            for arg, type_ in zip(args, types):
                assert isinstance(arg, type_), f"Argument {arg} must be {type_}"
            # Check keyword args
            for key, value in kwargs.items():
                if key in typed_args:
                    assert isinstance(value, typed_args[key]), \
                        f"Argument {key} must be {typed_args[key]}"
            return func(*args, **kwargs)
        return wrapper
    return decorator

# -----------------------------
# 10. MAGIC METHODS
# -----------------------------
print("\n=== Magic Methods ===")

class SuperString:
    def __init__(self, content):
        self.content = content
    
    def __str__(self):
        return self.content
    
    def __repr__(self):
        return f"SuperString('{self.content}')"
    
    def __len__(self):
        return len(self.content)
    
    def __getitem__(self, key):
        return self.content[key]
    
    def __add__(self, other):
        return SuperString(self.content + str(other))
    
    def __call__(self):
        return self.content.upper()
    
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")