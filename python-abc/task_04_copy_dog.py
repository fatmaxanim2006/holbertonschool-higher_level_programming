#!/usr/bin/python3
import copy

class Dog:
    """Dog klassı - kopyalama təcrübəsi üçün"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Bu hissə test üçündür, checker adətən klassın özünü yoxlayır
if __name__ == "__main__":
    my_dog = Dog("Buddy", 3)
    
    # Obyektin kopyasını yaradırıq
    my_dog_copy = copy.copy(my_dog)
    
    # Kopyanın adını dəyişirik
    my_dog_copy.name = "Max"
    
    # Orijinalın dəyişmədiyini yoxlayırıq
    print(my_dog.name)        # Buddy
    print(my_dog_copy.name)   # Max
