# Python Advanced Concepts Cheat Sheet

# -----------------------------
# 1. METACLASSES
# -----------------------------
print("\n=== Metaclasses ===")

class MetaLogger(type):
    def __new__(cls, name, bases, attrs):
        # Log attribute creation
        print(f"\nCreating class: {name}")
        for key, value in attrs.items():
            if not key.startswith('__'):
                print(f"Attribute: {key} = {value}")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MetaLogger):
    x = 1
    y = 2
    def method(self):
        pass

# -----------------------------
# 2. DESCRIPTORS
# -----------------------------
print("\n=== Descriptors ===")

class ValidString:
    def __init__(self, minlen=0, maxlen=None):
        self.minlen = minlen
        self.maxlen = maxlen
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Value must be a string')
        if len(value) < self.minlen:
            raise ValueError(f'String must be at least {self.minlen} characters')
        if self.maxlen and len(value) > self.maxlen:
            raise ValueError(f'String must be at most {self.maxlen} characters')
        instance.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name

class User:
    username = ValidString(minlen=3, maxlen=15)
    password = ValidString(minlen=8, maxlen=20)

# Test descriptors
user = User()
try:
    user.username = "Jo"  # Will raise ValueError
except ValueError as e:
    print(f"\nValidation error: {e}")

# -----------------------------
# 3. ABSTRACT BASE CLASSES
# -----------------------------
print("\n=== Abstract Base Classes ===")

from abc import ABC, abstractmethod
from typing import Protocol

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: list) -> list:
        pass
    
    @abstractmethod
    def validate(self, data: list) -> bool:
        pass

# Protocol for duck typing
class Drawable(Protocol):
    def draw(self) -> None: ...

# -----------------------------
# 4. ASYNCIO AND COROUTINES
# -----------------------------
print("\n=== Asyncio and Coroutines ===")

import asyncio

async def async_operation(sec: int) -> str:
    await asyncio.sleep(sec)
    return f"Operation completed after {sec} seconds"

async def main():
    # Gather multiple coroutines
    results = await asyncio.gather(
        async_operation(1),
        async_operation(2)
    )
    print(f"\nAsync results: {results}")

# Run async code
try:
    asyncio.run(main())
except RuntimeError:
    print("\nAsync code example (skipped in regular Python file)")

# -----------------------------
# 5. ADVANCED ITERATORS
# -----------------------------
print("\n=== Advanced Iterators ===")

class CircularBuffer:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.position = 0
        self.counter = 0
    
    def add(self, item):
        self.buffer[self.position] = item
        self.position = (self.position + 1) % self.size
        self.counter += 1
    
    def __iter__(self):
        idx = self.position - 1 if self.counter > 0 else 0
        items_seen = 0
        
        while items_seen < min(self.counter, self.size):
            if idx < 0:
                idx = self.size - 1
            yield self.buffer[idx]
            idx -= 1
            items_seen += 1

# Test circular buffer
buffer = CircularBuffer(3)
for i in range(5):
    buffer.add(i)
print("\nCircular buffer contents:", list(buffer))

# -----------------------------
# 6. ADVANCED DECORATORS
# -----------------------------
import time

print("\n=== Advanced Decorators ===")

def retry(max_attempts, delay=1):
    def decorator(func):
        async def async_wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    await asyncio.sleep(delay)
        
        def sync_wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        
        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
    return decorator

@retry(max_attempts=3)
def might_fail():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

print("\nTesting retry decorator:")
try:
    result = might_fail()
    print(f"Result: {result}")
except ValueError as e:
    print(f"Final failure: {e}")

# -----------------------------
# 7. ADVANCED CONTEXT MANAGERS
# -----------------------------
print("\n=== Advanced Context Managers ===")

from typing import Optional, Any
from types import TracebackType
import threading

class ResourcePool:
    def __init__(self, size: int):
        print(f"\nInitializing ResourcePool with {size} resources")
        self.resources = [self._create_resource() for _ in range(size)]
        self._lock = threading.Lock()
        print("Available resources:", [r["id"] for r in self.resources])
        
    def _create_resource(self):
        resource = {"id": id(object()), "in_use": False}
        print(f"Created resource with id: {resource['id']}")
        return resource
    
    def __enter__(self):
        print("\nAttempting to acquire resource...")
        with self._lock:
            print("Lock acquired, searching for available resource")
            for resource in self.resources:
                if not resource["in_use"]:
                    resource["in_use"] = True
                    print(f"Resource {resource['id']} allocated")
                    # Store the current resource for __exit__
                    self._current_resource = resource
                    return resource
            print("No available resources found!")
            raise RuntimeError("No available resources")
    
    def __exit__(self, exc_type: Optional[type],
                 exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]) -> bool:
        print("\nReleasing resource...")
        with self._lock:
            if hasattr(self, '_current_resource'):
                self._current_resource["in_use"] = False
                print(f"Resource {self._current_resource['id']} released")
                delattr(self, '_current_resource')
        print("Resource release completed")
        return False  # Don't suppress exceptions

# Demonstrate usage of ResourcePool
print("\nDemonstrating ResourcePool usage:")
pool = ResourcePool(2)  # Create pool with 2 resources

# Example 1: Successfully acquire and release resource
print("\nExample 1: Basic resource acquisition")
with pool as resource1:
    print(f"Using resource: {resource1['id']}")
    print("Doing some work with the resource...")
print("Resource should now be released")

# Example 2: Try to use multiple resources simultaneously
print("\nExample 2: Multiple resource acquisition")
try:
    with pool as resource1:
        print(f"Acquired first resource: {resource1['id']}")
        with pool as resource2:
            print(f"Acquired second resource: {resource2['id']}")
            print("Using both resources...")
        print("Second resource released")
    print("First resource released")
except RuntimeError as e:
    print(f"Caught expected error: {e}")

# Example 3: Error handling
print("\nExample 3: Error handling in context manager")
try:
    with pool as resource:
        print(f"Acquired resource: {resource['id']}")
        raise ValueError("Simulated error")
except ValueError as e:
    print(f"Caught error: {e}")
print("Resource should be released even after error")

# Show final pool state
print("\nFinal pool state:")
print("Available resources:", [r["id"] for r in pool.resources if not r["in_use"]])

# -----------------------------
# 8. ADVANCED TYPE HINTS
# -----------------------------
print("\n=== Advanced Type Hints ===")

from typing import TypeVar, Generic, Callable, Union, Optional
from dataclasses import dataclass

T = TypeVar('T')
S = TypeVar('S')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def map(self, func: Callable[[T], S]) -> 'Stack[S]':
        new_stack = Stack[S]()
        for item in self._items:
            new_stack.push(func(item))
        return new_stack

@dataclass
class Result(Generic[T]):
    value: Optional[T]
    error: Optional[str] = None
    
    @classmethod
    def success(cls, value: T) -> 'Result[T]':
        return cls(value=value)
    
    @classmethod
    def failure(cls, error: str) -> 'Result[T]':
        return cls(value=None, error=error)

# Test advanced types
number_stack: Stack[int] = Stack()
number_stack.push(1)
number_stack.push(2)
string_stack = number_stack.map(str)
print(f"\nConverted stack: {string_stack._items}")

# -----------------------------
# 9. ADVANCED MEMORY MANAGEMENT
# -----------------------------
print("\n=== Advanced Memory Management ===")

import weakref
import gc

class ExpensiveResource:
    def __init__(self, name: str):
        self.name = name
    
    def __del__(self):
        print(f"\nResource {self.name} deallocated")

# Weak references
resource = ExpensiveResource("test")
weak_ref = weakref.ref(resource)
print(f"Weak reference alive: {weak_ref() is not None}")
del resource
print(f"Weak reference after deletion: {weak_ref() is not None}")

# Manual garbage collection
gc.collect()
print(f"Garbage collector statistics: {gc.get_stats()}")