from pet_class import Pet

def main():
    pet_name = input("Enter pet name: ")
    pet_type = input("Enter pet type: ")
    pet_age = input("Enter pet age: ")

    my_pet = Pet(name=pet_name, animal_type=pet_type, age=pet_age)
    my_pet.set_name(pet_name)
    my_pet.set_animal_type(pet_type)
    my_pet.set_age(pet_age)

    print("\nRegistering pet into the system...")
    print("\nHere's your registration details:")
    print(f"Name: {my_pet.get_name()}")
    print(f"Type: {my_pet.get_animal_type()}")
    print(f"Age: {my_pet.get_age()}")

if __name__ == "__main__":
    main()

