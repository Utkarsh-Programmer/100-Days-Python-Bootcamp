class QuizBrain:
    """This class functions all the quiz logic."""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        """Return True if quiz still has questions."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieve the current question number from the 'question_list'."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {
                current_question.text} (True/False)? "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks the answer and increase the score if answer is correct, else print the correct answer."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
            print(f"The correct answer was: {correct_answer}")
        print(
            f"Your current score is {
                self.score}/{self.question_number}."
        )
        print()
