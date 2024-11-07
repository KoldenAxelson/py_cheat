# Python Basics Cheat Sheet

# -----------------------------
# 1. PRIMITIVE VARIABLES
# -----------------------------
print("\n=== Variables and Data Types ===")

# Numbers
integer_num = 42
float_num = 3.14
print(f"Integer: {integer_num} (type: {type(integer_num)})")
print(f"Float: {float_num} (type: {type(float_num)})")

# Strings
text = "Hello, Python!"
multiline_text = """This is a
multiline string"""
print(f"\nString: {text}")
print(f"String length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Multiline: {multiline_text}")

# Boolean
is_active = True
is_complete = False
print(f"\nBoolean value: {is_active}")
print(f"Boolean operations: AND: {is_active and is_complete}, OR: {is_active or is_complete}")

# -----------------------------
# 2. DATA STRUCTURES
# -----------------------------
print("\n=== Data Structures ===")

# Lists (mutable, ordered)
my_list = [1, 2, 3, "four", 5.0]
print(f"\nList: {my_list}")
my_list.append(6)
print(f"After append: {my_list}")
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")
print(f"Slicing: {my_list[1:4]}")

# Tuples (immutable, ordered)
my_tuple = (1, 2, "three")
print(f"\nTuple: {my_tuple}")
print(f"Tuple length: {len(my_tuple)}")

# Dictionaries (key-value pairs)
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"\nDictionary: {my_dict}")
print(f"Access value: {my_dict['name']}")
print(f"Dictionary keys: {my_dict.keys()}")
print(f"Dictionary values: {my_dict.values()}")

# -----------------------------
# 3. CONTROL FLOW
# -----------------------------
print("\n=== Control Flow ===")

# If-elif-else
age = 20
print("\nChecking age...")
if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")

# For loops
print("\nFor loop examples:")
# Loop through list
for item in ["a", "b", "c"]:
    print(f"Item: {item}")

# Range-based loop
for i in range(3):
    print(f"Number: {i}")

# While loop
print("\nWhile loop example:")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1

# -----------------------------
# 4. FUNCTIONS
# -----------------------------
print("\n=== Functions ===")

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(f"\nBasic function: {greet('Alice')}")

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(f"Power function: {power(3)}")
print(f"Power function with custom exponent: {power(2, 3)}")

# Function with multiple returns
def divide_and_remainder(a, b):
    return a // b, a % b

quot, rem = divide_and_remainder(7, 3)
print(f"\nDivision result - Quotient: {quot}, Remainder: {rem}")

# -----------------------------
# 5. ERROR HANDLING
# -----------------------------
print("\n=== Error Handling ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always executes")

# -----------------------------
# 6. LIST COMPREHENSION
# -----------------------------
print("\n=== List Comprehension ===")

# Traditional way
squares_traditional = []
for i in range(5):
    squares_traditional.append(i**2)
print(f"Traditional squares: {squares_traditional}")

# List comprehension way
squares_comprehension = [i**2 for i in range(5)]
print(f"List comprehension squares: {squares_comprehension}")

# With conditional
even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")