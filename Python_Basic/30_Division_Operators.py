#Write a program to demonstrate /, //, and %.

a, b = map(int, input("Enter two numbers: ").split())

print(a/b) #normal division it will return output with dicimel points
print(a//b) #floor division it will return output without dicimel points or remove digits after dicimal
print(a%b) #module it will give us reminder of division