# Write a function convert_data(values) that:
# Converts the input into a tuple
# Converts the same input into a set (removes duplicates)
# Returns a sorted list of unique elements
# Input can be list or tuple, output must follow format:
# tuple version
# set version
# sorted unique list

# a=list(map(int,input("Enter numbers:::").split()))
# print(a)
# def data(a):
#     i=tuple(a)
#     j=set(a)
#     k=sorted(j)
#     print("Tuple::",i)
#     print("Set:",j)
#     print("Sorted::",k)
#     return 0
# print(data(a))


# Write a function safe_average(lst) that:
# Calculates the average of numbers in a list
# Uses try / except to handle errors
# Handle these cases:
# Empty list (avoid division by zero)
# Non-numeric values in the list
# Always return a number (or a meaningful message).

# a=list(map(int,input("Enter number::").split()))
# # a=int(input("Enter value ::"))
# # a=[int(input("ENter the value::")) for _ in range (a)]
# def avg(a):
#     sum=0
#     j=0
#     try:
#         for i in a:
#             j=len(a)
#             sum=sum+i
#         return (sum/j)
#     except ZeroDivisionError:
#         print("Enter valid number.")
# print("Average is :",avg(a))

# Write a function factorial(n) that calculates the factorial of a number n
# Input the number from the user and print the factorial using the function

# def fact(a):
#     for i in range (1,a):
#         a=a*i
#     return a
# a=int(input("Enter number :"))
# print("The factorial is :::",fact(a))

# Write a function count_vowels(s) that takes a string s as input
# Counts the number of vowels (a, e, i, o, u) in the string
# Returns the coun


# a=input("Enter string::")
# def coun(a):
#     count=0
#     for i in a:
#         if i.lower() in 'aeiou':
#             count +=1
#     return count
# print("Total vowel count is ::",coun(a))

# Write a function unique_sorted(lst) that:
# Takes a list of numbers as input
# Returns a sorted list of unique elements

def sort(a):
    l=set(a)
    print(l)
    m=sorted(l)
    return m
a=list(map(int,input("enter number seperated by space::").split()))
print("SOrted number is::",sort(a))