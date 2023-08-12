# each quiz has many questions
# each quiz holds all possible responses
# each question has multiple answers
# each option leads to a certain result

# use dictionary- question number is key
# Question has actual question text and array of answers

from Question import Question
from Option import Option

all_possible_results = {
    0: "“Took my life from negative to positive” - Mr. Worldwide, Give Me Everything (0:07)",
    1: "“Y’all call it a moment, I call it life” -Mr. Worldwide, Feel This Moment (0:11) ",
    2: "“Believe me, been there done that. But everyday above ground is a great day. Remember that” -Mr. Worldwide, "
       "Time of Our Lives (3:08)",
    3: "“This is the last $20 I got, But I'ma have a good time ballin' or out, Tell the bartender, line up some "
       "shots. ‘Cause I’ma get loose tonight” -Mr. Worldwide, Time of Our Lives (0:32)",
    4: "“Time is money, only difference is I own it. Like a stopwatch, let's stop time and enjoy this moment” -Mr. "
       "Worldwide, Feel This Moment (2:41) "
}

quiz_questions = {
    1: Question("What is your favorite subject in school?",
                [Option("Math", 4), Option("English", 3), Option("Science", 0), Option("Social Studies", 2)]),
    2: Question("What is your favorite Mr. Worldwide song?",
                [Option("Give Me Everything", 0), Option("Feel This Moment", 1), Option("Time of Our Lives", 2),
                 Option("Who is mr. worldwide?", 1)]),
    3: Question("Are you single?",
                [Option("Yes", 3), Option("No", 2), Option("It's complicated", 4)]),
    4: Question("What’s your go-to COVID vaccine?",
                [Option("Pfizer", 4), Option("Moderna", 2), Option("Johnson & Johnson", 0), Option("Cocktail Mix", 3)]),
    5: Question("What kind of muffin are you?",
                [Option("Chocolate chip", 4), Option("Blueberry", 2), Option("Coffee Cake", 1),
                 Option("Cranberry Orange", 3)]),
    6: Question("What is your favorite form of cheese?",
                [Option("Straight up cheese", 4), Option("Mozzarella sticks", 1), Option("Cheese curbs", 2),
                 Option("Fondue", 0)])
}

collect_answer_results = []


# after every answer, get option_answer.result for the number
# --> at end, can get all result numbers and see which one has the most

def get_result():
    # for number of keys in all_possible_results, find the one with the max number of answers
    result = -1
    curr_count = 0
    for x in all_possible_results.keys():
        if x in collect_answer_results and collect_answer_results.count(x) > curr_count:
            curr_count = collect_answer_results.count(x)
            result = x
    return all_possible_results[result]


def start():
    print("Find out what Mr. Worldwide quote you embody from answering these random questions!")  # name of quiz
    strt = input("\nAre you ready to get started? (y/n): ")
    print("------------------------------\n")

    if strt == 'y' or strt == 'yes':
        # start game
        # go through each question in dictionary and ask_for_answer
        # for q in range(len(quiz_questions)):
        for q in quiz_questions:
            current_quest = quiz_questions[q]
            current_quest.display_question_and_options()
            ans = current_quest.ask_for_answer()
            collect_answer_results.append(int(ans))
            print("\n")

        # add response to collect_answer_results
        # print results of quiz
        res = get_result()

        print("Your Mr. Worldwide quote is...\n", res)

    else:
        print("Thanks for playing!")


start()
