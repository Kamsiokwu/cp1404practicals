"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters a non-integer value for the numerator or denominator.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the user enters zero as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
No, it's not possible to avoid a ZeroDivisionError.
"""

numerator_input = input("Enter the numerator: ")

# Check if the input is a valid number
if numerator_input.isdigit():
    numerator = int(numerator_input)

    denominator_input = input("Enter the denominator: \n ")

    # Check if the input is a valid number
    if denominator_input.isdigit():
        denominator = int(denominator_input)

        # Check if the denominator is 0
        if denominator == 0:
            print("Cannot divide by zero!")
        else:
            fraction = numerator / denominator
            print(fraction)
    else:
        print("Denominator must be a valid number!")
else:
    print("Numerator must not be 0 please try again!")

print("Finished.")

#Answers:
# When will a ValueError occur?
#
# A ValueError occurs when the user inputs something that cannot be converted to an integer (e.g., entering a letter or symbol like & instead of a number).
# When will a ZeroDivisionError occur?
#
# A ZeroDivisionError occurs when the user enters 0 as the denominator, which is mathematically undefined.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
#
# Yes, we can avoid the ZeroDivisionError by adding a condition to check if the denominator is zero before attempting the division. Here’s how to modify the code: