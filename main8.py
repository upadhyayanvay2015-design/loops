x=int(input("Enter base: "))
n=int(input("Enter number of terms: "))
s=0
for i in range(n):
    t=x**i
    s=s+t
    if i<n-1:
        print(f"{t}",end=" + ") 
    else:
        print(f"{t}")
print("Sum is: ",s)          
