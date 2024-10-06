import random

bool_value1 = random.choice([True, False])
print("Random Boolean (Version 1):", bool_value1)

#  2
bool_value2 = random.randint(0, 1) == 1
print("Random Boolean (Version 2):", bool_value2)

bool_value3 = bool(random.getrandbits(1))
print("Random Boolean (Version 3):", bool_value3)
