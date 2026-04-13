 #Decorator is typically a callable fucntion that usually takes another function
#as a argument and returns a replacement function. The replacement funciton 
# typically extends or alters the behavior of the original function.

#This fucntion is the example of nested function.

def decorator(func):
    def wrapper():
        print("I am about to execute a function")
        func()
        print("I have executed this function")
    return wrapper
def say_hello():
    print("hello")
# say_hello()
f=decorator(say_hello)
f()