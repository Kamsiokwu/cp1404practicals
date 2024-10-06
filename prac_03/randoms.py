import random

def main():
    print(random.randint(5, 20))  # line 1
    print(random.randrange(3, 10, 2))  # line 2
    print(random.uniform(2.5, 5.5))  # line 3

    # Line 1: Generates a random integer between 5 and 20, inclusive.
    # Smallest number: 5, Largest number: 20

    # Line 2: Generates a random number from the sequence [3, 5, 7, 9].
    # Smallest number: 3, Largest number: 9
    # Can it produce a 4? No

    # Line 3: Generates a random floating-point number between 2.5 and 5.5.
    # Smallest number: 2.5, Largest number: 5.5

if __name__ == "__main__":
    main()
