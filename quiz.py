#Fill in the blanks quiz

blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]
#Array of blanks that will be replaced by the answer arrays

easy_block = '''\nPython is a computer programming ___1___ that acts as an
interpreter for a program that has been written. ___2___ only requires
a few lines of code to describe something complicated. Python also requires
code to be written with a specific ___3___. In Python you can use a name to
keep track of values by using ___4___. Once a variable is defined, you can
always change the ___5___ of the variable.'''
easy_answer = ["language", "Python", "syntax", "variables", "value"]
# Easy level of fill in the blank as well as the answers

medium_block = '''\nThe test ___1___ determines what block to execute, the one
inside the if statement or the one inside the ___2___ statement. True and
False are ___3___ and they are always written with a ___4___ letter. It is
preferred that code is ___5___, rather than bigger.'''
medium_answer = ["expression", "else", "booleans", "capital", "shorter"]
# Medium level of fill in the blank as well as the answers

hard_block = '''\nA string is a sequence of ___1___ surrounded by quotes.
In python, you can't ___2___ a string with an ___3___. ___4___ is
a short notation for giving a variable a value. Python knows how to trace
the ___5___ between multiple variables in order to find the root of
the very first variable.'''
hard_answer = ["characters", "concatenate", "integer", "+=", "relationship"]
# Hard level of fill in the blank as well as the answers
def user_input(data):
    '''Allows for player to input the amount of guesses that
    they would like for the quiz.'''
    data = raw_input("\nHow many guesses would you like: ")

def select_level(level):
    '''Asks the player to input their desired level and returns
    the corresponding paragraph(blocks) with the answer key.'''
    if level == "easy":
        return easy_block, easy_answer
    elif level == "medium":
        return medium_block, medium_answer
    elif level == "hard":
        return hard_block, hard_answer

def restart():
    '''Asks the player if they would like to restart the game after
     completing the game.'''
    restart = raw_input("\nDo you want to play again: ")
    if restart == "yes":
        return main()
        #returns player back to the start of the game
    else:
        return exit()
        #exits the game and returns player back to the command line

def rules(blanks, blocks, answers, data):
    '''Defines the quiz rules by using a while loop and if
    statement to compare player answer with the answer key
    in the level that was chosen. Also prompts player to play
    again when the conditions have been met.'''
    index = 0
    guesses = int(data)
    #assigns data from user_input to guesses as an integer
    while index < len(blanks):
        answer = raw_input("\nFill in the blanks when prompted: ")
        if answer == answers[index]:
            blocks = blocks.replace(blanks[index], answers[index])
            #the .replace method allows for the blanks to be replaced
            #with the answers in the right order by using the defined index
            print "\nThat's right!"
            print blocks
            index += 1
            #prints the paragraph with the blanks that have been filled in
            #and moves on to the next blank that needs to be filled in
        else:
            guesses -= 1
            print "\nSorry, try again"
            #prompts player to try again and removes a guess

        if guesses == 0:
            print "\nBetter luck next time."
            return restart()
        elif index == len(blanks):
            print "\nNICE JOB! You filled in all the blanks correctly"
            return restart()

def main():
    '''Starts the game by prompting player for their name and
    level of difficulty. Then it runs through the rules of the
    game.'''
    name = raw_input("\nEnter your player name: ")
    print "\nWelcome " + str(name) + " to my quiz about Python."
    level = raw_input("\nSelect a level (easy|medium|hard): ")
    levels = ["easy", "medium", "hard"]
    while level not in levels:
         level = raw_input("\nSelect a level (easy|medium|hard): ")
         #a while loop that prints the levels again if player inputs level that
         #does not exist in the options given
    data = raw_input("\nHow many guesses would you like: ")
    #prompts player to input number of guesses
    print "\nFill in the blanks when prompted. You have " + str(data) + " guesses to answer correctly."
    blocks, answers = select_level(level)
    #assigns the correct paragraph(blocks) and answers to the select_level
    #function in order to replace the blanks throughout the quiz
    print blocks
    return rules(blanks, blocks, answers, data)
    restart = raw_input("\nDo you want to play again: ")
    #prompts user to restart the game if they wish to do so

main()
