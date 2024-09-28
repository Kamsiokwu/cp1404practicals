scores = float(input("Enter your score: "))

#if conditions to test scores
if scores < 0 or scores > 100:
    print("Invalid score")
elif scores >= 90:
    print("Excellent")
elif scores >= 50:
    print("Passed")
else:
    print("Bad")