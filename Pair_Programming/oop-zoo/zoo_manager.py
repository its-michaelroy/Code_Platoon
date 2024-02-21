class Animal:
    # Model of all the Zoo Animals
    def __init__(self,name,species):
        self.species = species
        self.name = name
        self.speak = "Animal sound"
        
    def speak(self):
        print(f"{self.speak}")
    
    
    def __str__(self):
        return f"Species:{self.species} Name: {self.name}"
    
class Mammal(Animal):
    # Model of all the Mammals
    def __init__(self, species, name ):
        super().__init__(species, name)
    
    def give_birth(self):
        print(f"has given birth {self.species}")
        
class Bird(Animal):
    # Model of all the birds
    def __init__(self, species,name, wingspan):
        super().__init__(species, name)
    
        self.wingspan = wingspan
    
    
class Reptile(Animal):
    # Model of all the Reptiles
    def __init__(self, species, name):
        super().__init__(species, name)
        
    def bask_in_sun(self):
        print(f"{self.name} the {self.species} is bask in the sun.") 
    

# Cat = Animal("Feline", "Momo")
# print(Cat)