# a=input("Enter the Name:")
# b=a[::-2]
# print(b)




# k=int(input("enter the total numbers:"))
# b=[]
# for i in range(0,k):
#     a=int(input("enter number: "))
#     b.append(a)
# print(b)
# b.sort()
# print(b[k-1])

#    Write a Python program that:
# Takes n numbers from the user (user decides how many)
# Stores them in a list
# Prints the sum of all numbers

# a=int(input("enter the upto number:::"))
# c=[]
# for i in range (a):
#     b=int(input("enter number:"))
#     c.append(b)
# print(c)
# sum=0
# for r in c:
#     sum=sum+r
# print(sum)


# a=input("enter 5 number seperated by space:").split()
# a=[int(num) for num in a]
# largest=max(a)
# print(largest)

# Write a Python program that:
# Takes multiple numbers from user (in one line, space separated)
# Store them in a list
# Print only the even numbers from that list

# a=input("Enter 5 number :").split()
# a=[int(num) for num in a]
# for i in a:
#     if(i%2==0):
#         print(i)
        
# Write a Python program that:
# Asks the user to enter a sentence
# Counts how many vowels (a, e, i, o, u) are in that sentence
# Prints the total count

# st=input("enter the string:")
# count=0
# for char in st:
#     if char.lower() in "aeiou":
#         count=count+1
# print(count)

   
   
   
# Write a Python program to print the multiplication table of a given number.
   
   
# a=int(input("enter the number:::"))
# for i in range (1,10):
#     b=a*i
#     print(f"{a} * {i} = {b}")
   
   
   
# Write a Python program that:
# Asks the user how many numbers they want to enter
# Takes all numbers as input and stores them in a list
# Prints only the odd numbers from the list
# a=int(input("enter the total:::::::"))
# c=[]
# for i in range (a):
#     r=int(input("enter::"))
#     c.append(r)
# for i in c:
#     if i%2!=0:
#         print(f"the odd number are {i}")
     
     
     
     
        
# Write a Python program that:
# Asks the user how many numbers they want to enter
# Takes all numbers as input and stores them in a list
# Prints:
# Largest number
# Smallest number
# Sum of all numbers

a=int(input("enter upto number::::"))
c=[]
for i in range (a):
    p=int(input("Enter number::"))
    c.append(p)
print(c)
lar=max(c)
sma=min(c)
sum=0
for i in c:
    sum=sum+i
print(f"the smallest is{sma} , the largest is {lar} and total is {sum} ")