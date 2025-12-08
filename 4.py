#creating a program that shows multiplication for 1 to n
# a=int(input("Enter up to multiplication"))
# for i in range (1,a+1):
#         print(f"The multiplication of {i} is:")
#         for r in range (1,10):
#          print(i,"*",r,"=",i*r)
#program that value of n and ask for n value form user and show max and min value,positive and negative value,prime value , odd value ,even values
# a=int(input("Enter the value of n:::"))
# a=[int(input(f"ENter value {i}::")) for i in range(1,a+1)]
# lar=max(a)
# sma=min(a)
# p,n,z,e,o=[],[],[],[],[]
# for r in a:
#     if r>0:
#         p.append(r)
#     elif r<0:
#         n.append(r)
#     else:
#         z.append(r)
# print("largest:",lar,"smalles",sma)
# print("positive:",p,"negative::",n,"zero:",z)
# for r in a:
#     if r%2==0:
#         e.append(r)
#     elif r%2!=0:
#         o.append(r)
# print("Even numbers :::",e,"Odd numbers:::",o)
# l=[]
# for i in a:
#     if i>0:
#      for m in range (2,i):
#         if(i%m==0):
#             break
#      else:
#          l.append(i)
# print("Prime numbers:",l)

# Write a Python program that:
# Takes a sentence as input
# Converts it into a list of words
# Prints:
# Total number of words
# First word
# Last word
# Words sorted alphabetically

# a=input("Enter the sentence:::")
# r=a.split()
# print(r)
# count=0
# for i in r:
#     count +=1
# j=count
# print(f"total words are {count}")
# print("first word::",r[0],"last word::",r[-1])
# r.sort()
# print("Alphabet order is",r)

# Ask the user to enter n numbers
# Store them in a list
# Count and print
# How many positive numbers
# How many negative numbers
# How many zeros
# a=int(input("Enter value of n:::"))
# a=[int(input(f"enter {i}")) for i in range (a)]
# pcount,ncount,count=0,0,0
# for i in a:
#     if i>0:
#         pcount +=1
#     elif i<0:
#         ncount +=1
#     else:
#         count +=1
# print("positive numbers::",pcount,"negative numbers:::",ncount,"zero",count)


# Ask the user to input a sentence.
# Count the number of vowels (a, e, i, o, u) in the sentence. 
# Count the number of consonants.
# Print both counts.

# a=input("Enter the sentence::")
# r=len(a)
# print(r)
# count=0
# for char in a:
#     if char.lower() in 'aeiou':
#         count +=1
# print("The vowels count ::",count,"The constant count ::",r-count)

# a=input("Enter the sentence::")
# vowel,constant=0,0
# for char in a:
#     if char.isalpha():
#         if char.lower() in 'aeiou':
#             vowel +=1
#         else:
#             constant +=1
# print("The vowel::",vowel,"The constant::",constant)

# Ask the user to enter n numbers
# Store them in a list
# Count how many times each number appears
# Print each number with its frequency
# a=int(input("enter value of n:::"))
# a=[int(input("Enter::")) for _ in range(a)]
# c={}
# for i in a:
#     if i in c:
#         c[i] +=1
#     else:
#         c[i] =1
# for i in c:
#     print("number:",i,"occour:",c[i])
    
    
# Ask the user to input a string (sentence or word)
# Print:
# The reversed string
# Every second character of the string
# Every second character in reverse

a=input("Enter the sentence or string:::")
print(a[::2])#[start:stop:step]
print(a[1::2])
# print(a[::-1])
# print(a[::-2])
