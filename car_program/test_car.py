from car_class import Car

def main():
    car = Car(2024, "Honda Civic")
    print(f"Test Drive for: {car.get_year_model()}{car.get_make()}")

    print("ACCELERATING:")
    car.accelerate()
    print(f"Current Speed: {car.get_speed()}km/h")

    print("BRAKING:")
    car.brake()
    print(f"Current Speed: {car.get_speed()}km/h")

if __name__ == "__main__":
    main()