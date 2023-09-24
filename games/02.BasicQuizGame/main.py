def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
def display_score(correct_guesses, guesses):
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end= " ")
    print()
    
    score = int(correct_guesses/len(questions)*100)
    print("Your score is: "+str(score)+"%")
def play_again():
    response = input("Do you want to play again? (yes or no)? ").upper()
    if response == "YES":
        return True
    else:
        return False

# Using dictionary to store questions and correct option

questions = {
    "Who created Python?: ": "A",
    "Which country is the first one to successfully land on south pole of moon?": "B",
    "Who is the owner of X.com?: ": "C",
    "Is the Earth round?: ": "A"
}

# 2D SET
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. China", "B. India", "C. Russia", "D. USA"],
           ["A. Changpeng Zhao", "B. Jeff Bezos", "C. Elon Musk", "D. Jack Dorsey"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth"]]

new_game()
while play_again():
    new_game()
print("Bye!")