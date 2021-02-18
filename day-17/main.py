"""
    TRUE-FALSE QUIZ APP
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# questions bank
question_bank = []
for dictionary in question_data:
    question = Question(dictionary["question"], dictionary["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score is {quiz.score} out of {quiz.question_number}")