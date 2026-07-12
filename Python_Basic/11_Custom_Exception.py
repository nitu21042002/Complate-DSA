#Write a program to raise a custom exception.
class NumberNotFound(Exception):
    pass

l = [1, 2, 3, 4, 5]
for i in l:
    if i == 27:
        print("Found")
        break
else:
    raise NumberNotFound("23 is not present in the list.")
