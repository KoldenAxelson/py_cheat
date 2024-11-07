# Python Advanced Concepts Cheat Sheet

# -----------------------------
# 1. METAPROGRAMMING
# -----------------------------
print("\n=== Metaprogramming ===")

# Basic Metaclass
class MetaLogger(type):
    def __new__(cls, name, bases, attrs):
        print(f"\nCreating class: {name}")
        for key, value in attrs.items():
            if not key.startswith('__'):
                print(f"Attribute: {key} = {value}")
        return super().__new__(cls, name, bases, attrs)

# Metaclass with Method Interception
class MetaValidator(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value) and not key.startswith('__'):
                attrs[key] = cls.validate_types(value)
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def validate_types(func):
        def wrapper(*args, **kwargs):
            # Validate types using annotations
            for arg, value in zip(func.__annotations__, args[1:]):
                if not isinstance(value, func.__annotations__[arg]):
                    raise TypeError(f"Argument {arg} must be {func.__annotations__[arg]}")
            return func(*args, **kwargs)
        return wrapper

# Class Factory
def create_dataclass(class_name, **fields):
    return type(class_name, (), {
        '__init__': lambda self, **kwargs: setattr(self, '__dict__', kwargs),
        '__repr__': lambda self: f"{class_name}({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})",
        **fields
    })

# -----------------------------
# 2. DESCRIPTOR PATTERNS
# -----------------------------
print("\n=== Descriptor Patterns ===")

# Data Descriptor
class ValidatedField:
    def __init__(self, *validators):
        self.validators = validators
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        for validator in self.validators:
            validator(value)
        instance.__dict__[self.name] = value

# Validators
def min_length(min_len):
    def validate(value):
        if len(value) < min_len:
            raise ValueError(f"Length must be at least {min_len}")
    return validate

def max_length(max_len):
    def validate(value):
        if len(value) > max_len:
            raise ValueError(f"Length must be at most {max_len}")
    return validate

def pattern(regex):
    import re
    def validate(value):
        if not re.match(regex, value):
            raise ValueError(f"Value must match pattern {regex}")
    return validate

# -----------------------------
# 3. ADVANCED TYPE SYSTEM
# -----------------------------
print("\n=== Advanced Type System ===")

from typing import (
    TypeVar, Generic, Callable, Union, Optional,
    Literal, TypedDict, NewType, Protocol,
    runtime_checkable
)

# Generic Types
T = TypeVar('T')
S = TypeVar('S', bound='Stringable')

class Stringable(Protocol):
    def __str__(self) -> str: ...

class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    
    def get(self) -> T:
        return self.item
    
    def transform(self, func: Callable[[T], S]) -> 'Container[S]':
        return Container(func(self.item))

# Custom Types
UserId = NewType('UserId', int)

class UserData(TypedDict):
    name: str
    age: int
    active: bool

# Runtime Protocol
@runtime_checkable
class Renderable(Protocol):
    def render(self) -> str: ...

# -----------------------------
# 4. ASYNCHRONOUS PROGRAMMING
# -----------------------------
print("\n=== Asynchronous Programming ===")

import asyncio
from typing import AsyncIterator

# Async Context Manager
class AsyncResource:
    async def __aenter__(self):
        await self.open()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.close()
    
    async def open(self):
        await asyncio.sleep(0.1)
        print("Resource opened")
    
    async def close(self):
        await asyncio.sleep(0.1)
        print("Resource closed")

# Async Iterator
class AsyncRange:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.start >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.start += 1
        return self.start - 1

# Async Generator
async def async_generator(n: int) -> AsyncIterator[int]:
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

# -----------------------------
# 5. MEMORY MANAGEMENT
# -----------------------------
print("\n=== Memory Management ===")

import weakref
import gc
from contextlib import suppress

# Custom Reference Counting
class RefCounted:
    _instances = {}
    
    def __init__(self, name):
        self.name = name
        self.__class__._instances[name] = self.__class__._instances.get(name, 0) + 1
    
    def __del__(self):
        with suppress(KeyError):
            self.__class__._instances[self.name] -= 1
            if self.__class__._instances[self.name] == 0:
                del self.__class__._instances[self.name]

# Weak References
class Cache:
    def __init__(self):
        self._cache = weakref.WeakKeyDictionary()
    
    def get(self, key, default=None):
        return self._cache.get(key, default)
    
    def set(self, key, value):
        self._cache[key] = value

# Memory Profiling
class MemoryTracker:
    def __init__(self):
        self.start_stats = None
    
    def __enter__(self):
        gc.collect()
        self.start_stats = gc.get_stats()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        gc.collect()
        end_stats = gc.get_stats()
        for i, (start, end) in enumerate(zip(self.start_stats, end_stats)):
            print(f"Generation {i}:")
            print(f"  Collections: {end[0] - start[0]}")
            print(f"  Objects collected: {end[1] - start[1]}")

# -----------------------------
# 6. ADVANCED CONCURRENCY
# -----------------------------
print("\n=== Advanced Concurrency ===")

import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from queue import Queue
import multiprocessing

# Thread-Safe Singleton
class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Producer-Consumer Pattern
class ProducerConsumer:
    def __init__(self, size):
        self.queue = Queue(size)
    
    def producer(self, items):
        for item in items:
            self.queue.put(item)
    
    def consumer(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            # Process item
            print(f"Processing {item}")
            self.queue.task_done()

# Process Pool with Shared Memory
def parallel_process(func):
    def wrapper(*args, **kwargs):
        with ProcessPoolExecutor() as executor:
            return executor.map(func, *args)
    return wrapper

# -----------------------------
# 7. ADVANCED CONTEXT MANAGERS
# -----------------------------
print("\n=== Advanced Context Managers ===")

from typing import Optional, Any, ContextManager
from types import TracebackType
from contextlib import contextmanager, ExitStack

# Reentrant Context Manager
class ReentrantLock:
    def __init__(self):
        self._lock = threading.RLock()
        self._depth = 0
    
    def __enter__(self):
        self._lock.acquire()
        self._depth += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._depth -= 1
        self._lock.release()
        return False

# Dynamic Context Manager
class DynamicContext:
    def __init__(self, enter_func, exit_func):
        self.enter_func = enter_func
        self.exit_func = exit_func
    
    def __enter__(self):
        return self.enter_func()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exit_func(exc_type, exc_val, exc_tb)

# Nested Context Managers
@contextmanager
def nested_contexts(*managers):
    with ExitStack() as stack:
        yield tuple(stack.enter_context(mgr) for mgr in managers)

# -----------------------------
# 8. ADVANCED INTROSPECTION
# -----------------------------
print("\n=== Advanced Introspection ===")

import inspect
import sys

# Class Inspector
class Inspector:
    @classmethod
    def inspect_class(cls, target_class):
        # Get all members
        members = inspect.getmembers(target_class)
        
        # Categorize members
        methods = inspect.getmembers(target_class, predicate=inspect.isfunction)
        properties = inspect.getmembers(target_class, predicate=inspect.isdatadescriptor)
        attributes = {name: value for name, value in members 
                     if not name.startswith('__') 
                     and not inspect.isfunction(value)
                     and not inspect.isdatadescriptor(value)}
        
        return {
            'methods': methods,
            'properties': properties,
            'attributes': attributes
        }
    
    @staticmethod
    def get_source(obj):
        return inspect.getsource(obj)
    
    @staticmethod
    def get_signature(func):
        return inspect.signature(func)

# -----------------------------
# 9. ADVANCED DEBUGGING
# -----------------------------
print("\n=== Advanced Debugging ===")

import sys
import traceback

# Custom Exception Hook
def custom_exception_hook(exc_type, exc_value, exc_traceback):
    print("Exception occurred:")
    print("Type:", exc_type.__name__)
    print("Value:", str(exc_value))
    print("Traceback:")
    traceback.print_tb(exc_traceback)

# Debug Context
@contextmanager
def debug_context():
    old_hook = sys.excepthook
    sys.excepthook = custom_exception_hook
    try:
        yield
    finally:
        sys.excepthook = old_hook

# Traceback Manager
class TracebackManager:
    def __init__(self):
        self.stored_traceback = None
    
    def capture(self):
        try:
            raise Exception("Capture point")
        except Exception:
            self.stored_traceback = sys.exc_info()[2].tb_next
    
    def print_traceback(self):
        if self.stored_traceback:
            traceback.print_tb(self.stored_traceback)