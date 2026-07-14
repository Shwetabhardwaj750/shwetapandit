# odd_even 
x = int(input("enter a number:"))
if x%2==0:
    print("x is even")
else:
    print("x is odd")

#using boolean
def main():
    y = int(input("enter a number:"))
    if is_even(y):
        print("even")
    else:
        print("odd")
def is_even(n):
    if n%2==0:
        return True
    else:
     return False
main()
#harry potter
name = (input("enter your name:"))
if name=="harry"or name=="hermoine"or name=="ron":
    print("gryffindor")
elif name=="draco":
    print("slytheryn")
else:
    print("who")
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end="")
        else:
            print("",end="")
    print()
n=4


