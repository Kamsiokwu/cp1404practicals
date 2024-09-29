import random


def main():
    """Main function to get user input and create random scores."""
    score = float(input("Enter the score: "))
    result = results(score)
    print(result)

    # Generate a random score between 0 and 100
    random_score = random.randint(0, 100)
    print(f"Random score is: {random_score}")
    random_result = results(random_score)
    print(random_result)

def results(score):
    """Function to calculate the result based on the score entered in the first place of the program."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passed"
    else:
        return "Bad"

main()
