#!/usr/bin/env python3

class Person:
    # Class body goes here

    #Instance method definition
    def talk(self):
        print("Hello World!")
    def walk(self):
        print("The person is walking.")
        
person1 = Person()
print(dir(person1))

person1.walk()
person1.talk()
