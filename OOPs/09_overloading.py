class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age #Convention: _age indicate it's inteded ot be "private"

    def get_age(self):# we are making getter for age
        return self._age
    
    def get_name(self):
        return self.name
    
    def set_age(self,new_age): # we are making setter for age
        if new_age>=0 and new_age<=150: # we are setting up the conditions
            self._age=new_age
        else:
            print("Invalid age")
person =Person("Alson",22)
print(person.get_age())# we are expecting the output here
print(person.get_name())


# we will use the set method here
person.set_age(40)
print(person.get_age())

person.set_age(-6) # we will check whether the entered age is correct or not
print(person.get_age()) #here the age value wont be change.


    