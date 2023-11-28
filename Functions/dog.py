class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")
    def sayAge(self):
        print(f"I am {self.age} years old woof")

dog1 = Dog("Covid",3)
dog2 = Dog("Virus",3)
dog3 = Dog("Tamawo",10)
dog4 = Dog("Pute",2)

print(dog1.name)
dog2.bark()
dog2.sayAge()

class GoldenRetriever(Dog):
    def fetch(self):
        print(f"{self.name} is fetching the ball")

GoldenRetriever.fetch(dog1)

def introduce_pet(pet):
    print(f"I am {pet.name}, and I am {pet.age} years old.")

introduce_pet(dog1)    # Output: I am Buddy, and I am 3 years old.
introduce_pet(dog2)  # Output: I am Charlie, and I am 2 years old.