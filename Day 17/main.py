import question_model
import data
import quiz_brain
question_bank = []

for question in data.question_data:
    q_holder = question_model.Question(question["question"], question["correct_answer"])
    question_bank.append(q_holder)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")