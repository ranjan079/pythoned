# Write a function convert_data(values) that:
# Converts the input into a tuple
# Converts the same input into a set (removes duplicates)
# Returns a sorted list of unique elements
# Input can be list or tuple, output must follow format:
# tuple version
# set version
# sorted unique list

a=list(map(int,input("Enter string seperated by comma::").split()))
print(a)
def what(a):
    i=tuple(a)
    j=set(a)
    k=sorted(j)
    print("Tuple:",i)
    print("Set(without duplicate):",j)
    print("Sorted::",k)
print(what(a))