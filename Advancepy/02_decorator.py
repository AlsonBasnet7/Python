def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
    # def number():
    #     int =5
    # f=decorator(number)
    # f()
        
#  number():
#     n=4
# f=repeat(number)
# f()
@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")
say_hello("Harry")




