# each option leads to a certain result
class Option:
    def __init__(self, option_text, result=0):
        self.option_text = option_text
        self.result = result # result is index of result that option leads to