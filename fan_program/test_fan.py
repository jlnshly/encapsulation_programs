from fan_class import Fan

def main():
    fan_one = Fan(speed=Fan.FAST, radius=10.0, color="yellow", on=True)
    fan_two = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", on=False)

    print("Fan Status")
    print(fan_one)
    print(fan_two)

if __name__ == "__main__":
    main()