# Question has actual question text and array of answers

class Question:
    def __init__(self, text, options=[], answer=""):
        self.text = text
        self.options = options
        self.answer = answer

    def display_question_and_options(self):
        print(self.text)
        for x in range(len(self.options)):
            print("\t", (x + 1), ". ", self.options[x].option_text)

    def ask_for_answer(self):
        ans = input('Enter your response with the answer number: ')
        while len(ans) == 1 and not ans.isdigit():
            ans = input('Error with response, enter response again: ')

        self.answer = ans
        return ans





