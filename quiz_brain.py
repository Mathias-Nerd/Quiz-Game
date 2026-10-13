class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.score =  0
        self.question_number = 0

    def still_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        while True:
            self.answer = input(f"Q{self.question_number}. {question.question_text} True or False?: ").lower()
            if self.answer in ["true", "false"]:
                break
            else:
                print("\nEnter True or False\n")
        return self.answer, question.answer

    def check_answer(self, player_answer, correct_answer):
        self.player_answer = player_answer
        self.correct_answer = correct_answer
        if self.player_answer.lower() == self.correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print(f"Wrong, the correct answer is {self.correct_answer}")
        print(f"Score: {self.score}/{len(self.questions)}")


    
        