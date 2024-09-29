def main():
    score = get_valid_score()
    while True:
        print("Choose from the list, enter one first letter:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Exited")
            break
        else:
            print("Invalid choice, please try again.")

def get_valid_score():
    """Get a valid score from the user."""
    while True:
        score = float(input("Enter your score (0:100): "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score, please try entering a score between 0 and 100.")

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

def show_stars(score):
    """Printing stars based on the user's score."""
    print('*' * int(score))

main()
