#Write a program to demonstrate mutable default arguments.
def add(x,y=[]):
    y.append(x)
    return y

print(add(1))
print(add(2))
print(add(3))
print(add(3.2))