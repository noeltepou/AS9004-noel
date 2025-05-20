score = 0 

# Define the questions and answers
questions = [
    "Question 1: How many sets of brothers have played in the All Blacks?",
    "Question 2: The oldest player to play a test for the All Blacks is Ned Hughes. How old was he?",
    "Question 3: The All Blacks have scored more than 100 points on how many occasions in a test match?",
    "Question 4: There have been how many fathers and sons to have represented the All Blacks?",
    "Question 5: In their history, the All Blacks have selected players born in how many countries outside of New Zealand?"
]

correct_answers = [
    "47",
    "40",
    "5",
    "19",
    "13"
]

# Ask the questions
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ").strip()
    if user_answer == correct_answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answers[i]}.\n")

# Print the final score
print("Quiz complete.")
print("Your final score is:", score)

# Optional feedback
if score >= 2:
    print("good job!")
else:
    print("boo hoo, try harder!")
