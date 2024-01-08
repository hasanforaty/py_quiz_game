from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
questions = question_data["results"]
for question in questions:
    question_bank.append(Question(question_text=question['question'], question_answer=question['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("you've completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")


