'''
 Chaining mutiple decorators

'''
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
def exclaim(func):
    def wrapper():
        return func()+"!!!"
    return wrapper
@uppercase
@exclaim
def great():
    return "hello"
print(great())
