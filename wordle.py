import requests
import random
import sys 


def main():

    playGame()


def playGame():

    answer = generateRandomWord()

    current_guess = 1

    letters_left = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    total_wrong_letters = []

    while current_guess < 7:
        guess = getGuess(current_guess)
        
        if guess == answer:
            print('You win!')
            print(f'You guessed the correct word in {current_guess} guess(es): {guess.upper()}')
            sys.exit()
        
        else:
            # show result after guess
            print(getString(guess, answer))

            # show letters guessed that are not in answer
            wrong_letters = [l for l in guess if l not in list(answer)]

            for _ in wrong_letters:
                if _ not in total_wrong_letters:
                    total_wrong_letters.append(_)

            letters_left = [l for l in letters_left if l not in wrong_letters]

            print(f'Letters remaining: {letters_left}')   
            print(f'Wrong letters: {total_wrong_letters}')                 
            current_guess += 1
    
    print('Sorry, you\'re out of turns.')
    print(f'The correct answer was: {answer.upper()}')
    sys.exit()

def getString(guess, answer):
    string = []
    for g, a in zip(list(guess), list(answer)):
        if g == a:
            string.append(g.upper())
        else:
            string.append('_')
    return ' '.join(string)

def getRedLetters(guess, answer):
    red_letters = []
    for g in guess:
        if g not in list(answer):
            red_letters.append(g)
    
    return red_letters

def getYellowLetters(guess, answer):
    green_letters = [g for g, a in zip(list(guess),list(answer)) if g == a]
    yellow_letters = [g for g, a in zip(list(guess),list(answer)) if g != a]

    return [y for y in yellow_letters if y not in green_letters and y in list(answer)]

        
# this function generates a 5 letter word at random
def generateRandomWord():
    url = 'https://www.mit.edu/~ecprice/wordlist.10000'
    word_list = requests.get(url).text.split()
    return random.choice([l for l in word_list if len(l) == 5])


def getGuess(guess_num):
    return input(f'Guess #{guess_num}: ').lower()

if __name__ == '__main__':
    main()