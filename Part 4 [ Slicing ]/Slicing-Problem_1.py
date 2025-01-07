"""
Question 2 :
Write a python function that takes a string as input and returns the substring from the 3rd to the 8th character
"Data Science"
"Hello World, I am Learning Python"
"All the best"
"""
def get_substring(input_string):
    """Returns the substring from the 3rd to the 8th character."""
    return input_string[2:8]

# Test cases
print(get_substring("Data Science"))                 # Output: "ta Sci"
print(get_substring("Hello World, I am Learning Python"))  # Output: "llo Wo"
print(get_substring("All the best"))                 # Output: "l the "