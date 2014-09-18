import Tkinter
import random
import questions

correct_answers = []
questions_asked = []

print(questions.Boolean_tables_questions)

# This is an empty bank
Multiple_choice_questions = [{Category - Key: [(Q & A - tuple), (Q & A - tuple2)]}]


def greeting():
    #Cue music and greeting-voice-over
    #Cue snake hissing
    greeting = raw_input("Welcome to Test Your Python Knowledge!  Dare to try?")


def overview():
    #Cue overview-voice-over:
    overview = raw_input(“There
    are
    64
    questions.You
    must
    answer
    45
    to
    pass.If
    you
    do
    not
    pass, you
    fail.You’ll
    be
    tested
    on
    Collections,
    Operators, Stacks and Qeues, Built - in Functions, Modules, Commands, Packages, Imports, Decorators, String
    Operations,
    Boolean
    Values, Arguments, Conditions, Loops, Classes, I / O
    Methods, PEP
    8 and DRY.Ready?")


def inventory():
    #Within Total_Multiple_choice_questions[], there are 16 dictionaries, one for each category.
    #Within each dictionary, there is a key--which is its category name-- and a value, which is a list
    #of nine tuples. Each tuple contains a question and answer.
    #Multiple_choice_questions[] is an empty list. Each time inventory() is called, the total number of tuples
    #(questions) in Multiple_choice_questions[] is added up.  Which should be something like:
    if Multiple_choice_questions.sum < 48:
        terms_categories()
    #Below, this just checks to see if 2 questions from each remaining "super" category have been asked.
    #If not, the tester gets another question from that super-category. If so, it skips that super-category.
    Elif
    boolean_tables_questions[] > 8:
    #Send the [1] offset from Total_test to question() as an argument, because [1]
    #represents Total_Boolean_questions[].
    Elif
    debugging_syntax_questions[] > 8:
    #Send the [2] offset from Total_test to question() as an argument, because [2]
    #represents Total_Debugging_questions[].
    Elif
    Pep8_DRY
    questions[] > 8:
    #Send the [3] offset from Total_test to question() as an argument, because [3]
    #represents Total__questions[].
    Elif
    Prove_You_Can_Code[] > 8:
    #Send the [4] offset from Total_test to question() as an argument, because [4]
    #represents Total__questions[].

    #Create a for_loop for above, maybe with every value in Total_Test.

    def terms_categories():
        #This function exists solely to organize the filtering of Total_Multiple_choice_questions[] into
        #Multiple_choice_questions[].  All it does is make sure that no more than three questions of each
        #category get asked. To accomplish this, it does inventory of each category/dictionary within M_c_q[].
        #Once a category contains three questions/tuples, that category's dictionary gets removed from
        #Total_Test[]. This way, the randomizer can no longer ask a question from that category.
        For
        every_offset in Multiple_choice_questions[]:
        #Offsets being dictionaries in this case.
        if len(category / dictionary) < 6:
            #If each categories’ dictionary is full, we don’t ask questions from that category anymore.
            Total_Test.remove[said
            dictionary]
            question()
            #Also, send the zero offset from Total_test to question() as an argument, because zero
            #represents Total_Multiple_choice_questions[].
        else:
            question()


#Question: do I send a question at the end of the inventory function or at the beginning of question function?
#What about terms/categories?

def question():
    Total_test.random
    #Calls question in Total_Test[] by argument for offset in list (offset determined by inventory and terms_cats).
    Tag()
    #Tag() is not called within the Test() function, only locally in the question function.
    Total_test.remove
    #Remove that question from the Total_test[] bank, so as not to be asked twice.


def tag():
    #Assigns categories to each question based on the keywords of each of A) the 16 categories of multiple
    #choice questions; and B) The remaining 4 categories of the total_test hierarchy.
    For
    the
    argument
    of
    the
    current
    randomly
    chosen
    question,
    print its
    keyword
    value.


def verifier():
    hurrah_bank = [“Yay!", "
    My
    hero!]
    jeers_bank = [“You
    suck!”, "Shit for brains!"]
    hurrah_sound = []
    jeers_sound = []
    #Adds one to total questions[]
    total_questions.append[]
    If
    input == is correct:
    correct_answers.append[]
    print random.hurrah[]
    #print_sound random.hurrah_sound[]


Else:
print random.jeer[]
#print_sound random.jeer_sound[]

def scorecard():
    current_score = correct_answers[] / questions_asked[]
    print current_score
    if questions_asked = 64:
        final_score()
    else:
        pass


def final_score():
    final_score = correct_answers[] / questions_asked[]
    print final_score
    if final_score > 69 %:
        print "Congratulations, you passed!"
    if final_score <= 69 %:
        print "Sorry, you failed. Try again."


def Test():
    While
    questions_asked < 56:
    Inventory()
    Question()
    Verify()
    Scorecard()


break

Greeting()
Overview()
Test()