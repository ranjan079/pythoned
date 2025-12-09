# Write a program to:
# Take n numbers from the user and store them in a list
# Create a new list containing only the squared values of each number
# Print the original list and the squared list

# a=int(input("Enter the value of n::::"))
# a=[int(input("Enter value:::")) for _ in range(a)]
# c=[]
# for i in a:
#     c.append(i*i)
# print(c)


# Write a Python program to:
# Take n numbers into a list
# Find the min and max values
# Normalize each number using the formula:
# normalized​
# Print both original and normalized lists

# a=int(input("Enter value of n:::"))
# a=[int(input("Enter value:::")) for _ in range(a)]
# ma=max(a)
# mi=min(a)
# c=[]
# for i in a:
#     r=(i-mi)/(ma-mi)
#     c.append(r)
# print(a)
# print(c)

# Write a program to calculate:
# Mean (Average)
# Median
# Mode

# import statistics as st
# a=[10,20,30,40,50,20,10,20]
# print("Mean:",st.mean(a))
# print("Median:",st.median(a))
# print("Mode:",st.mode(a))



# !!!!!!!!!!!funtion!!!!
# def add(a,b):
#     return (a+b)
# print(add(2,3))

# def ty(name):
#     print(f"Name:{name}")
# ty("ranjan")


# Write a function count_numbers(lst) that takes a list of numbers as input.
# The function should count how many numbers are:
# Positive
# Negative
# Zero
# Return these counts and print them.
# Ask the user to enter n numbers and store them in a list to pass to the function.

# def count(a):
#     pcount,ncount,count=0,0,0
#     for i in a:
#         if i>0:
#             pcount +=1
#         elif i<0:
#             ncount +=1
#         else:
#             count=1
#     return pcount,ncount,count
# n=int(input("ENter value of n"))
# a=[int(input("ENter value:")) for _ in range(n)]
# positive,negative,zero=count(a)
# print("positive numbers total::",positive)
# print("negative numbers total::",negative)
# print(zero)

# Write a function average_positive(lst) that:
# Takes a list of numbers as input
# Calculates the average of all positive numbers in the list
# Returns the average (ignore negative numbers and zeros)
# Ask the user to enter n numbers to store in a list and pass it to the function.

# a=int(input("ENter the value of n:::"))
# a=[int(input("Enter value:::")) for _ in range(a)]
# def count(a):
#     count=0
#     for i in a:
#         if i>0:
#             count +=1
#     print(count)
#     return count
# def averag(a):
#     avg=0
#     for i in a:
#         if i>0:
#             avg=avg+i
#     print(avg)
#     r=0
#     r=avg/count(a)
#     return r
# print("the average is :",averag(a))

# Write a function square_positives(lst) that:
# Takes a list of numbers as input
# Filters out all positive numbers
# Returns a new list containing the square of each positive number
# Ask the user to enter n numbers to store in a list and pass it to the function.

# a=[-1,0,2,3,-5,-4,8]
# c=[]
# def square(a):
#     for i in a:
#         if i>0:
#             c.append(i*i)
#     return c
# print(square(a))

# #using list comprehension
# a=[-1,0,2,3,-5,-4,8]
# def square(a):
#     result=[i**2  for i in a if i>0 ]
#     return result
# print(square(a))

# Write a function process_numbers(lst) that:
# Returns three lists:
# All even numbers
# All odd numbers
# Squares of all numbers
# Use list comprehension inside the function.
# Ask user for input list and pass it to the function.

a=[2,4,6,3,5,7,0,1,9,8]
def all(a):
    even=[i  for i in a if i%2==0]
    odd=[i  for i in a if i%2!=0]
    square=[i**2 for i in a]
    return even,odd,square
even,odd,square=all(a)
print("Even numbers:::",even)
print("Odd numbers::",odd)
print("Square numbers::",square)