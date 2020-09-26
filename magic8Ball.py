import random

#Opens Response txt file
a = open('Magic_8_Ball_Project/8_ball_responses.txt', 'r')

#x is the txt file
#Splits the lines from each other and randomly chooses a line from the file
def answer(x):
    line = open(x).read().splitlines()
    return random.choice(line)

#Main function
#Asks questions and checks for responses
def main():
    print('Welcome to the Magic 8 Ball Program')
    print("Please feel free to ask the program any question, but be wary because we do not guarantee satisfaction")

    #Please note: As long as you spell the answer correctly, the program will accept it
    
    question = input('Ask a yes or no question to the Magic 8 Ball: ')
    question = question.upper()

    if question == 'QUIT':
        print('So you are too scared to see the future, hope you gain the courage to face me again. See you soon...')
        import sys
        sys.exit()
        
    print(question)
    print(answer('Magic_8_Ball_Project/8_ball_responses.txt'))

    q = input('Would you like to play again, yes or no?: ')
    q = q.upper()

    if q == 'NO':
        print('Thank you for using the program, have a great day!')
        import sys
        sys.exit()

    if q == 'YES':
        print('You can quit at anytime by typing in "QUIT" in any answer box')
        main()


main()
