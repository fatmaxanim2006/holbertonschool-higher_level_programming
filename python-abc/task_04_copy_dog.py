#!/usr/bin/python3
import copy

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    my_dog = Dog("Buddy", 3)
    print(my_dog.name)
    print(my_dog.age)

    # Obyektin kopyasını yaradırıq
    my_dog_copy = copy.copy(my_dog)
    my_dog_copy.name = "Max"
    
    print(my_dog.name)
    print(my_dog_copy.name)
