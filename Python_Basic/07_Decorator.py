#Write a program using a Decorator.
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before Decorator!!")
        res=func(*args, **kwargs)
        print("After Decorator use!!")
        return res
    return wrapper


@decorator
def sum(*args):
    total=0
    for i in args:
        total=total+i
    print(total)

sum(1,2,3,45,12,85)

