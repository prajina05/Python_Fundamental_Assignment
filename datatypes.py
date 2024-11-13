""" 1. Write a script, data_types.py, to:
○ Create variables of each primitive data type (int, float, str, bool).
○ Perform a few operations: arithmetic (on int and float), string concatenation, and
logical operations.
○ Create a dictionary to store and display these variables by their types as keys
(e.g., int: [10, 20]).
 """

# Creating variables of each primitive data type
data_int = 15  # integer
data_float = 7.5  # float
data_str = "prajina"  # string
data_bool = True  # boolean

# Performing operations on each primitive data type
int_result = data_int + 5  # Arithmetic operation on int
float_result = data_float * 2  # Arithmetic operation on float
str_result = data_str + " maharjan!"  # String concatenation
bool_result = data_bool or False  # Logical operation

# Creating a dictionary to store and display these variables by their types
data_dict = {
    'int': [data_int, int_result],
    'float': [data_float, float_result],
    'str': [data_str, str_result],
    'bool': [data_bool, bool_result]
}

# Displaying the dictionary
print("Data Types Dictionary:", data_dict)
