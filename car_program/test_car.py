from car_class import Car

def main():
    car = Car("2024 Civic", "Honda")
    print(f"Test Drive for: {car.get_year_model()}{car.get_make()}")

    print("ACCELERATING:")
    for i in range(1, 6):
        car.accelerate()
        print(f"Current Speed: {car.get_speed()}km/h")

    print("BRAKING:")
    for i in range(1, 6):
        car.brake()
        print(f"Current Speed: {car.get_speed()}km/h")

if __name__ == "__main__":
    main()