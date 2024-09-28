import random


def determine_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passed"
    else:
        return "Bad"


def main():
    """Main function to generate scores and write results to a file."""
    scores = int(input("Enter the number of scores to generate: "))

    with open("results.txt") as file:
        for _ in range(scores):
            score = random.randint(0, 100)  # Generate random scores between 0 and 100
            result = determine_result(score)
            file.write(f"{score} is {result}")

    print("Results have been written or copied to results.txt file on your pc")


main()
