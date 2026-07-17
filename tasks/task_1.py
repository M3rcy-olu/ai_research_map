# ==========================================
# Task 1: Data Types, Variables, and Printing
# ==========================================

# --- Part 1: Data Types ---
# In Python, we have different types of data. The most common ones are:
# 1. Integer (int): Whole numbers (e.g., 5, -10, 42)
# 2. Float (float): Decimal numbers (e.g., 3.14, -0.5)
# 3. String (str): Text, surrounded by quotes (e.g., "Hello", 'World')

# --- Part 2: Operations ---
# The '+' operator does different things depending on the data type!
# For numbers (int, float), it does mathematical addition: 5 + 5 = 10
# For strings, it does concatenation (joins them together): "Hello " + "World" = "Hello World"

# --- Part 3: Variables ---
# Variables are like containers for storing data. 
# You assign data to a variable using the '=' sign.

example_number = 10
example_string = "Apples"

# --- Part 4: Printing ---
# We use the print() function to display output to the terminal.
# You can print strings (like line 26), variables (like line 27) or a combination of both (like line 28).
print("Welcome to Task 1!")
print(example_number, example_string)
print("I have", example_number, example_string)

#There are also multiple ways to format strings in Python. These are the two primary ways to do it:
# 1. Using f-strings
print(f"My favorite number is {example_number} and I like {example_string}.")
# 2. Using commas
print("My favorite number is", example_number, "and I like", example_string + ".")

#Typically when you have a lot of variables to print, f-strings are the preferred method because they are easier to read and write.


print("\n--- YOUR TURN ---\n")

# TODO 1: Create a variable called 'my_name' and assign it a string with your name.
my_name = "Joy Dada"


# TODO 2: Create a variable called 'my_age' and assign it an integer with your age.
my_age = 13


# TODO 3: Create a variable called 'favorite_number' and assign it a float (decimal number).
favorite_number = 8.0


# TODO 4: Use the print() function to print your name, age, and favorite number to the terminal.
print(f"My name is {my_name}, I am {my_age} years old, and my favorite number is {favorite_number}.")


# TODO 5: Create two integer variables, add them together using '+', and assign the result to a new variable.
# Then, print the result.
one = 1
two = 2
print(one + two)


# TODO 6: Create two string variables (e.g., a first name and last name), combine them using '+', 
# and assign the result to a new variable. Then, print the result.
first_name = "Mercy "
last_name = "Dada"
full_name = first_name + last_name
print(full_name)



# ==========================================
# Great job! Now it's time to submit your work.
# 1. Open the terminal.
# 2. Run: git status
# 3. Run: git add tasks/task_1.py
# 4. Run: git commit -m "Completed Task 1"
# 5. Run: git push
# ==========================================
