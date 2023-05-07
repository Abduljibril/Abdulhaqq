print("Welcome to the Python Program!")
play = input("Do you want to play? (yes/no): ")

if play.lower() == "yes":
    print("Great! Let's get started.")
    correct_answers = 0
    
    # Question 1
    answer1 = input("What is the capital of France? ")
    if answer1.lower() == "paris":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")
    
    # Question 2
    answer2 = input("What is the largest planet in our solar system? ")
    if answer2.lower() == "jupiter":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")
    
    # Question 3
    answer3 = input("What is the smallest country in the world? ")
    if answer3.lower() == "vatican city":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")
    
    # Results
    total_questions = 3
    percentage_score = (correct_answers / total_questions) * 100
    print(f"You answered {correct_answers} out of {total_questions} questions correctly.")
    print(f"Your percentage score is {percentage_score}%.")
else:
    print("Okay, maybe next time. Goodbye!")