def main():
    print("Welcome to this temperature converter software !!.")

    # Get input from the user
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")


def celsius_to_fahrenheit(celsius):
    # Convert Celsius back to Fahrenheit
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit back to Celsius
    return (fahrenheit - 32) * 5 / 9


main()
