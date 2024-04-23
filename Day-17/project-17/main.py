# Project 17
# Quiz Game

# ------------------------------------------------------------------------------------------------------------------------------------------
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# list of questions
question_bank = []

# appending questions to the 'question_bank'.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# calling the 'QuizBrain' class.
quiz = QuizBrain(question_bank)

# keep asking questions
while quiz.still_has_question():
    quiz.next_question()

# message after the quiz end.
print(
    f"You've completed the quiz. Your final score is {
        quiz.score}/{quiz.question_number}."
)
# ------------------------------------------------------------------------------------------------------------------------------------------
