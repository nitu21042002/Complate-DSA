#Write a program to check whether a number is even or odd using a lambda function.


check=lambda n: ["Even" if i % 2 == 0 else "Odd" for i in range(1, n+1)]
#lambda variable: [value_if_true if condition else value_if_false for loop]
print(check(20))

#using dictinory comprenhension
check = lambda n: { i: "Even" if i % 2 == 0 else "Odd" for i in range(1, n + 1)}
print(check(20))

