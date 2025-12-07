# Takes n numbers from the user
# Stores them in a list
# Counts and prints:
# How many positive numbers
# How many negative numbers
# How many zeroes

# a=int(input("enter the value of n::::"))
# a=[int(input("enter number::")) for _ in range (a)]
# ncount=0
# pcount=0
# count=0
# i=[]
# j=[]
# k=[]
# for r in a:
#     if r>0:
#         i.append(r)
#         pcount +=1
#     elif r<0: 
#         j.append(r)
#         ncount +=1
#     else:
#         k.append(r)
#         count+=1
# print(f"the total {pcount} positive number are",i,"the total",ncount," negative number are",j,"the total",count, "zero are",k)

# Take n numbers from the user
# Store them in a list
# Find and print:
# Maximum number in the list
# Minimum number in the list
# Average of all numbers

# p=int(input("Enter up to value:::"))
# n=[int(input("Enter:")) for _ in range(p)]
# l=max(n)
# print(l)
# s=min(n)
# print(s)
# sum=0
# total=0
# for i in n:
#     sum=sum+i
# total=sum/p
# print(total)

# Write a Python program to:
# Take n numbers from the user
# Store them in a list
# Create a new list containing only unique elements
# (remove duplicates)
# Print the unique list

p=int(input("Enter up to value:::"))
n=[int(input("Enter:")) for _ in range(p)]
c=[]
for i in n:
    if i not in c:
        c.append(i)
print(c)
        

        