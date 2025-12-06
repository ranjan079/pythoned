# Write a Python program that:
# Takes n numbers from the user
# Stores them in a list
# Creates another list that contains only the numbers greater than 10
# Print the new list

# a=int(input("enter numbers up to::"))
# c=[]
# for i in range (a):
#     b=int(input("Enter number::"))
#     c.append(b)
# print(c)
# r=[]
# for num in c:
#     if num>10:
#         r.append(num)
# print(r)



# Write a Python program to check whether a number is prime or not.

# a=int(input("enter the number:::"))
# for i in range (2,a):
#     if a%i==0:
#         print(f"the number {a} is not prime")
#         break
# else:
#         print(f"the number  {a} is  prime")
        

# Write a Python program that:
# Takes n numbers from the user
# Stores them in a list
# Creates two new lists:
# one containing even numbers
# one containing odd numbers
# Prints both lists separately

# a=int(input("enter up to number:::"))
# c=[]
# for i in range (a):
#     r=int(input("Enter:::"))
#     c.append(r)
# e=[]
# f=[]
# for num in c:
#     if num%2==0:
#         e.append(num)
#     else:
#         f.append(num)
# print(f"The even numbers are {e} and odd numbers are{f}")


# Write a program that:
# Takes n numbers from the user
# Stores them in a list
# Prints the numbers in ascending order (small → big)
# Prints the numbers in descending order (big → small)

# a=int(input("Enter up to numbers:::"))
# c=[]
# for i in range (a):
#     r=int(input("enter::"))
#     c.append(r)
# c.sort()
# print(f"the ascending order is {c}")
# c.reverse()
# print(f"the descending order is {c}")

# a=int(input("Enter up to :::"))
# c=[int(input("Enter number:")) for _ in range(a)]
# print("the sorted number is ",sorted(c))
# print("the descending number is ",sorted(c,reverse=True))

# Write a program that:
# Takes a sentence from the user
# Splits it into individual words
# Print:
# Total number of words
# Longest word
# Shortest word

# a=input("Enter the string::")
# c=a.split()
# print(c)
# print("length of word:",len(c))
# print("longest lenght:",max(c, key=len))
# print("shortest length",min(c, key=len))


# Write a Python program that:
# Takes a sentence from the user
# Stores all words in a list
# Creates a new list containing only words that start with a vowel (a, e, i, o, u)
# Prints the new list


# a=input("enter the string:::")
# d=a.split()
# c=[]
# print(d)
# for r in d:
#     if r[0].lower() in 'aeiou':
#         c.append(r)
# print(c)

# Write a Python program that:
# Takes n numbers from the user
# Stores them in a list
# Creates a new list containing only the prime numbers from the original list
# Prints the new list

# a=int(input("enter value of n::::"))
# a=[int(input("enter number::::::")) for _ in range(a)]
# c=[]
# for i in a:
#     print(i)
#     for r in range (2,i):
#         if i%r==0:
#             break
#     else:
#         c.append(i)          
# print(c)


# Write a Python program that:
# Takes n numbers from the user
# Stores them in a list
# Prints:
# Sum of all prime numbers
# Sum of all non-prime numbers

# a=int(input("enter the value of n:::"))
# a=[int(input("enter number::::")) for _ in range(a)] #4,6,7
# nsum=0
# sum=0
# for i in a: #4
#     for r in range (2,i):#2,3,4,5,6
#         if i%r==0:
#             nsum=nsum+i
#             break
#     else:
#         sum=sum+i
# print("the non prime sum is " ,nsum, "the prime sum is" ,sum)
        
        
# Takes n numbers from the user
# Stores them in a lis
# Creates two separate lists:
# One containing numbers divisible by 3
# Another containing numbers divisible by 5
# Prints both lists

a=int(input("enter value of n::::::"))
a=[int(input("Enter number:::")) for _ in range(a)]
c=[]
d=[]
for i in a:
   if i%3==0:
       c.append(i)
   if i%5==0:
       d.append(i)
print("the multiple of 3 are",c, "the multiple of 5 are",d)
       
       
       
