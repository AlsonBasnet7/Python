# class Animal:
#     def __init__(self,sound):
#         self.sound=sound
#     def sound(self):
#         some_sound="Some Sound"
#         return some_sound
# class Dog(Animal):
#     def sound(self):

#         print("Bark")
# dog=Dog.sound('')

class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark!")


dog = Dog()   # create object
dog.sound()   # call method
