import ipdb

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("Not a valid pet type!")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if owner is None:
            return None
        else:
            self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Invalid Pet Type")
    
    def sort_pets_by_name(self):
        list_of_pets = self.pets()
        sorted_pets = sorted(list_of_pets, key=lambda pet:pet.name)
        return sorted_pets

owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)

owner.sort_pets_by_name()

# ipdb.set_trace()