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

a=list(map(int,input("Enter number::").split()))
# a=int(input("Enter value ::"))
# a=[int(input("ENter the value::")) for _ in range (a)]
def avg(a):
    sum=0
    j=0
    try:
        for i in a:
            j=len(a)
            sum=sum+i
        return (sum/j)
    except ZeroDivisionError:
        print("Enter valid number.")
    except TypeError:
        print("Enter correct value:")
print("Average is :",avg(a))

