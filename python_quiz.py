# Welcome the user into playing the quiz
print("Welcome to my quiz about fun ANIMAL FACTS 🐈‍⬛🦒🐆🐍🦞🦅🦩")

quiz_begin = input("Would you like to begin the quiz now? (You should say yes 😸) ").strip().lower()

if quiz_begin != "yes":
    print("😿 Maybe another time then, goodbye!")
    quit()

print("Woohoo let's begin!")

# Quiz Variables
quiz_questions = ("Question 1. What are the only wild cats that live together in groups? ",
                  "Question 2. What animal uses its tough scales as armour, and will roll into a ball when threatened? ",
                  "Question 3. What animal has a fold of fur in their armpit that they use as a pocket? ",
                  "Question 4. What scavenger bird has an increased stomach acid content, making it immune to food poisoning? ")

answer_options = (("A. House Cats", "B. Tigers", "C. Lions"),
                ("A. Hedgehog", "B. Pangolin", "C. Woodlouse"),
                ("A. Sea Otter", "B. Kangaroo", "C. Chimps"), 
                ("A. Pigeons ", "B. Crows", "C.Vultures"))

# Answer Functions
correct_answers = ("C", "B", "A", "C")
user_answers = []
user_score = 0
question_number = 0

for quiz_question in quiz_questions:
    print("\n")
    print(quiz_question)
    for answer_option in answer_options[question_number]:
        print(answer_option)
    
    make_guess = input("Is the correct answer either A, B, or C? ").strip().upper()
    user_answers.append(make_guess)
    if make_guess == correct_answers[question_number]:
        user_score += 1
        print("That's right! 🐼")
    else:
        print("That's not quite right! 🙈")
        print(f"{correct_answers[question_number]} is the answer")
        question_number += 1


# Results Section
print("----------------------")
print("    Your Results:     ")
print("----------------------")

print("Correct Answers: ", end="")
for correct_answer in correct_answers:
    print(correct_answer, end=" ")
print()

print("Your Answers:   ", end="")
for user_answer in user_answers:
    print(user_answer, end=" ")
print()

score = (user_score / len(quiz_questions)) * 100
print(f"Your score is: {score:.0f}%")
