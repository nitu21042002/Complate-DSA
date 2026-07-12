#Write a program to reverse a string.

#with slicing
str="Nitu Yadav"
print(str[::-1])

#without slicing
rev=""
for i in str:
    rev=i+rev
print(rev)

#Using reversed()
print("".join(reversed(str)))

#using while loop
i = len(str) - 1
while i >= 0:
    print(str[i], end="")
    i -= 1
print()


#using recursion
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse(str))