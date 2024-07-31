class Owner:
    def __init__(self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if isinstance (pet, Pet):
            pet.owner = self
        else:
            raise TypeError ("enter a Pet class object")
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key= lambda pet: pet.name)
    
class Pet:    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not  pet_type in self.PET_TYPES:
            raise TypeError("enter a type that is in the PET_TYPES list")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
