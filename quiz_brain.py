class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        self.score = self.update_score(user_answer, current_question.answer)
        print(f"your score is{self.score}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
        else:
            print("It is wrong")
        print(f"{correct_answer} is the correct answer.")

    def update_score(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        return self.score



