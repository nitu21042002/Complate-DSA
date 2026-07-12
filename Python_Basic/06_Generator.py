#Write a program using a decorator.
def is_even():
    for i in range(1,21):
        if i%2==0:
            yield i

print(list(is_even()))