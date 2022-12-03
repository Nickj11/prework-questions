#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    user_name="Egg McWaffles"
    print("Hello!," + user_name.title() + "!")

#question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    odd_numbers = list(range(1,100,2))
    print(odd_numbers)

#quesion3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max_num_in_list = ['23' , '577' , '845' ]
    max(max_num_in_list)
    print("the max number in the list: " + max(max_num_in_list))

#question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_a_leap_year(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
print (is_a_leap_year(1997))

#question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consectutive(a_list):
    a_list = [13,11,21,32,43]
    range_list=list(range(min(a_list), max(a_list)+1))
    if a_list == range_list:
        print("the list has consecutive numbers")
    else:
        print("the list has no consecutive numbers")





