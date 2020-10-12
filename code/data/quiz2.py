"""
----------------------------------------------------------------------
Q1. complete the following function
----------------------------------------------------------------------
"""


def has202020(data):
    """
    Given a list of integers, return True if the list contains three adjacent 20.
    """
    pass


# # Uncomment the following lines to test
# data_1 = [10, 12, 2020, 20]
# data_2 = [10, 12, 20, 20, 20]
# data_3 = [20, 10, 12, 20, 20]
# print(has202020(data_1))
# print(has202020(data_2))
# print(has202020(data_3))

## Expected output:
## False
## True
## False


"""
----------------------------------------------------------------------
Q2. names.txt is a text file that contains all the names of students.
 Please complete the function to read the names into a list. Each name 
 will be one item in the list.
----------------------------------------------------------------------
"""


def read_names_to_list(filename):
    """
    filename: a string
    Return: a list of names
    """
    pass


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(read_names_to_list("data/names.txt")) # if names.txt is under "data" folder

## Expected output:
# ['Aidan', 'Anna', 'Brandon', 'Caroline', 'Daniel', 'Eoghan', 'Jiaying', 'Jeff', 'Joy', 'Mason', 'Neha', 'Prafful', 'Palida', 'Qi', 'Susanna', 'Shoaib', 'Ryan', 'Weijia', 'Diana', 'Yuwei', 'Noah', 'Julia', 'Liam', 'Deedee', 'Wei', 'Taewoong', 'Allyson', 'YeRi', 'Minghui', 'Ziyu', 'Kevin', 'Mateos', 'Kimberly', 'Blake', 'Oorja', 'Vivian', 'Cameron']


"""
----------------------------------------------------------------------
Q3. Please complete the function that gets names from a list
to run a simulation of 200 times of class cold-callings. In this 
simulation, each student has equal chance to be called. This function 
should return a dictionary that records how many times each student
gets called. Please do not change any code outside function.
----------------------------------------------------------------------
"""

# Please do not modify the following two lines
import random


random.seed(42)


def call_simulation(names, num_of_calls):
    """
    names: a list of names
    num_of_calls: total times of cold-calls in the simulation
    Return: a dictionary of name: positive integer pairs
    """
    pass


# When you've completed your function, uncomment the
# following lines and run this file to test!

# name_list = read_names_to_list("data/names.txt")
# print(call_simulation(name_list, 200))
## Expected output:
## {'Aidan': 5, 'Anna': 5, 'Brandon': 5, 'Caroline': 4, 'Daniel': 9, 'Eoghan': 8, 'Jiaying': 5, 'Jeff': 7, 'Joy': 6, 'Mason': 4, 'Neha': 8, 'Prafful': 1, 'Palida': 4, 'Qi': 7, 'Susanna': 12, 'Shoaib': 7, 'Ryan': 6, 'Weijia': 9, 'Diana': 3, 'Yuwei': 3, 'Noah': 4, 'Julia': 5, 'Liam': 3, 'Deedee': 7, 'Wei': 6, 'Taewoong': 4, 'Allyson': 1, 'YeRi': 6, 'Minghui': 3, 'Ziyu': 6, 'Kevin': 1, 'Mateos': 5, 'Kimberly': 6, 'Blake': 4, 'Oorja': 10, 'Vivian': 7, 'Cameron': 4}

"""
----------------------------------------------------------------------
Q4. Please complete the following function
----------------------------------------------------------------------
"""
# Please do not change the following line
random.seed(42)


def print_hist(data):
    """
    given a dictionary of name: positive integer pairs,
    print rows with the name and a number of asterisks equal
    to the positive integer.
    The rows should be printed in alphabetical order of names.
    No return is required.
    """
    pass


## When you've completed your function, uncomment the
## following lines and run this file to test!
# name_list = read_names_to_list("data/names.txt")
# name_dict = call_simulation(name_list, 200)
# print_hist(name_dict)

## Expected output:
# Aidan: *****
# Allyson: *
# Anna: *****
# Blake: ****
# Brandon: *****
# Cameron: ****
# Caroline: ****
# Daniel: *********
# Deedee: *******
# Diana: ***
# Eoghan: ********
# Jeff: *******
# Jiaying: *****
# Joy: ******
# Julia: *****
# Kevin: *
# Kimberly: ******
# Liam: ***
# Mason: ****
# Mateos: *****
# Minghui: ***
# Neha: ********
# Noah: ****
# Oorja: **********
# Palida: ****
# Prafful: *
# Qi: *******
# Ryan: ******
# Shoaib: *******
# Susanna: ************
# Taewoong: ****
# Vivian: *******
# Wei: ******
# Weijia: *********
# YeRi: ******
# Yuwei: ***
# Ziyu: ******


"""
----------------------------------------------------------------------
Q5. Please complete the following function to use your APIKEY to 
get current temperature (in Fahrenheit) in your current place 
from openweathermap.org.
If you don't have YOUR_OWN_APIKEY, you can use the APIKEY below,
but you will lose 10 points.
APIKEY = '8f62260aa7890d58d9a026e2810341ea'
----------------------------------------------------------------------
"""


def get_current_temp():
    """
    Returns current temperature in Fahrenheit in your current place
    from api.openweathermap.org
    Notice: the temperature returned from the API is in Kelvin.
    Below is the conversion formula form Kelvin to Fahrenheit:
    T(°F) = T(°K) × 9/5 - 459.67
    """
    pass

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(get_current_temp())

## Expected output:
## maybe 55 in Wellesley?