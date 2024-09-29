def fahrenheit_to_celsius(fahrenheit):
    """code to convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    with open("temps_input.txt", "r") as input_file:
        temperatures = input_file.readlines()

    with open("temps_output.txt", "w") as output_file:
        for line in temperatures:
            fahrenheit = float(line.strip())
            celsius = fahrenheit_to_celsius(fahrenheit)
            output_file.write(f"{celsius}\n")

    print("Converted temperatures have been written to temps_output.txt.")

main()
