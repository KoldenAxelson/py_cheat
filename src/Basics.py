# Python Basics Cheat Sheet

# -----------------------------
# 1. NUMBERS AND MATH
# -----------------------------
print("\n=== Numbers and Mathematical Operations ===")

# Integers
integer_num = 42
negative_num = -17
large_num = 1_000_000  # Using underscore for readability
print(f"Integers: {integer_num}, {negative_num}, {large_num}")

# Floats
float_num = 3.14
scientific = 2e-3
print(f"Floats: {float_num}, {scientific}")

# Math Operations
add = 5 + 3
subtract = 5 - 3
multiply = 5 * 3
divide = 5 / 3
floor_divide = 5 // 3
modulo = 5 % 3
power = 5 ** 3
print(f"Basic Math: +: {add}, -: {subtract}, *: {multiply}")
print(f"Division: /: {divide}, //: {floor_divide}, %: {modulo}, **: {power}")

# -----------------------------
# 2. STRING OPERATIONS
# -----------------------------
print("\n=== String Operations ===")

# String Creation
single_quotes = 'Hello'
double_quotes = "World"
multiline = """This is a
multiline string"""

# String Methods
text = "Hello, Python!"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Strip: {'  spaces  '.strip()}")
print(f"Replace: {text.replace('Python', 'World')}")
print(f"Split: {'one,two,three'.split(',')}")

# String Formatting
name = "Alice"
age = 30
print(f"F-string: {name} is {age}")
print("Format method: {} is {}".format(name, age))
print("Old style: %s is %d" % (name, age))

# -----------------------------
# 3. COLLECTIONS - LISTS
# -----------------------------
print("\n=== List Operations ===")

# List Creation and Access
my_list = [1, 2, 3, "four", 5.0]
print(f"Original list: {my_list}")
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")
print(f"Slicing: {my_list[1:4]}")

# List Methods
my_list.append(6)        # Add to end
my_list.insert(0, 0)    # Insert at position
my_list.extend([7, 8])  # Add multiple items
popped = my_list.pop()  # Remove and return last item
my_list.remove("four")  # Remove specific value
print(f"Modified list: {my_list}")

# List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
repeated = list1 * 2
print(f"Concatenated: {concatenated}")
print(f"Repeated: {repeated}")

# -----------------------------
# 4. COLLECTIONS - TUPLES
# -----------------------------
print("\n=== Tuple Operations ===")

# Tuple Creation
empty_tuple = ()
single_tuple = (1,)  # Note the comma
mixed_tuple = (1, "two", 3.0)

# Tuple Methods
coordinates = (3, 4)
print(f"Count: {coordinates.count(3)}")
print(f"Index: {coordinates.index(4)}")

# Tuple Unpacking
x, y = coordinates
point3d = (1, 2, 3)
x, *rest = point3d  # Unpacking with rest
print(f"Unpacked: x={x}, rest={rest}")

# -----------------------------
# 5. COLLECTIONS - DICTIONARIES
# -----------------------------
print("\n=== Dictionary Operations ===")

# Dictionary Creation
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Dictionary Methods
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Dictionary Operations
person.update({"email": "john@example.com"})
age = person.get("age", 0)  # Get with default
person.setdefault("country", "USA")  # Set if key missing
popped_value = person.pop("city")    # Remove and return value
print(f"Modified dict: {person}")

# -----------------------------
# 6. COLLECTIONS - SETS
# -----------------------------
print("\n=== Set Operations ===")

# Set Creation
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Sets: {set1}, {set2}")

# Set Methods
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")
print(f"Symmetric Difference: {set1.symmetric_difference(set2)}")

# Set Modifications
set1.add(4)        # Add single element
set1.update([5, 6])  # Add multiple elements
set1.remove(6)     # Remove (raises error if missing)
set1.discard(7)    # Remove (no error if missing)

# -----------------------------
# 7. CONTROL FLOW - CONDITIONALS
# -----------------------------
print("\n=== Conditional Statements ===")

# If-elif-else
score = 85
if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("Below C grade")

# Conditional Expressions (Ternary)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# -----------------------------
# 8. CONTROL FLOW - LOOPS
# -----------------------------
print("\n=== Loop Structures ===")

# For Loops
print("\nBasic for loop:")
for i in range(3):
    print(i)

# For with enumerate
print("\nEnumerate:")
for i, char in enumerate("abc"):
    print(f"{i}: {char}")

# While Loops
print("\nWhile loop:")
count = 0
while count < 3:
    print(count)
    count += 1

# Loop Control
print("\nLoop control:")
for i in range(5):
    if i == 2:
        continue  # Skip iteration
    if i == 4:
        break    # Exit loop
    print(i)

# -----------------------------
# 9. FUNCTIONS - BASICS
# -----------------------------
print("\n=== Function Basics ===")

# Basic Function
def greet(name):
    return f"Hello, {name}!"

# Default Parameters
def power(base, exponent=2):
    return base ** exponent

# Multiple Return Values
def divide_and_remainder(a, b):
    return a // b, a % b

# Args and Kwargs
def flexible_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

# -----------------------------
# 10. FUNCTIONS - ADVANCED
# -----------------------------
print("\n=== Advanced Functions ===")

# Lambda Functions
square = lambda x: x**2
print(f"Lambda result: {square(5)}")

# Function as Parameter
def apply_operation(func, value):
    return func(value)

print(f"Applied operation: {apply_operation(square, 4)}")

# Decorators
def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

# -----------------------------
# 11. ERROR HANDLING
# -----------------------------
print("\n=== Error Handling ===")

# Try-Except-Else-Finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
except TypeError:
    print("Type error!")
else:
    print(f"Result: {result}")  # Runs if no exception
finally:
    print("Cleanup code")  # Always runs

# Custom Exceptions
class CustomError(Exception):
    pass

# Raising Exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

# -----------------------------
# 12. COMPREHENSIONS
# -----------------------------
print("\n=== Comprehensions ===")

# List Comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(5)}
print(f"Square dict: {square_dict}")

# Set Comprehension
even_set = {x for x in range(10) if x % 2 == 0}
print(f"Even set: {even_set}")

# Generator Expression
sum_of_squares = sum(x**2 for x in range(5))
print(f"Sum of squares: {sum_of_squares}")