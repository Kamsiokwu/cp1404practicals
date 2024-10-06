LOWER = 33
UPPER = 127

char = input("Enter a character: ")
ascii_code = ord(char)
print("The ASCII code for '{char}' is {ascii_code}")

num = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
while num < LOWER or num > UPPER:
    print("Please enter a number within the range {LOWER}-{UPPER}.")
    num = int(input(f"Enter a number between {LOWER} and {UPPER}: "))

char_from_num = chr(num)
print("The character for {num} is '{char_from_num}'")

print("ASCII Table:")
print("{'ASCII Code':<12}{'Character':<12}\n")
print("-" * 24)  # Separator
for i in range(LOWER, UPPER + 1):
    print(f"{i:<12}{chr(i):<12}")
