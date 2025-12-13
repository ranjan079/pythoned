# n=int(input("Enter the number of player::"))
# a=list(input(f"Enter the name of player {i}::") for i in range(n))
# print(a)
o=int(input("Enter the number of over ::"))
def over(o):
    r=[]
    total=[]
    for i in range(1,o+1):
        sum=0
        print(f"{i} OVER:")
        for j in range(1,7):
            z=int(input(f"run at {i}.{j}over::"))
            r.append(z)
        for d in r:
            sum =+d
        total.append(sum)
        return total
result=over(o)
print("Total ::",result)
        
        
 
 