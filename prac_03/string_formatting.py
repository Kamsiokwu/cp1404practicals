"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

model = "1922 Gibson L-5 CES"
price = 16036
print(f"{model} for about ${price:,.2f}!")

# Using a for loop with f-string formatting
for i in range(11):
    result = 2 ** i
    print(f"2 ^ {i:<2} is {result:>4}")
