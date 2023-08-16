import pandas as pd
import numpy as np

# Creating variables
number_var = 42
string_var = "Hello, Health!"
my_list = [1, 2, 3, 4, 5]
my_dict = {
    'Name': 'Nimrat',
    'Age': 21,
    'data_points': [10, 20, 30],
    'dict_values': {
        'key1': 'value1',
        'key2': 'value2'
    }
}

# Creating a function
def calculate_health_score(weight, height):
    bmi = weight / ((height / 100) ** 2)
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Print statements for variables
print("Number Variable:", number_var)
print("String Variable:", string_var)
print("List:", my_list)
print("Dictionary:", my_dict)

# Example data for function
weight = 66  # in kg
height = 172 # in cm

# Running the function and printing the output
health_result = calculate_health_score(weight, height)
print("Health Analysis:", health_result)




