import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PROXYS GUESSING GAME")
print(ascii_banner)

number = random.randint(1, 999)

playerName = input('What is your name? ')

print('Hello', playerName)
number_of_guesses = 0
print('Lets play a game shordieee only 3 tries, pick a number 1 thru 999')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('ahh too low damn try again lol' )
    if guess > number:    
        print('ahh too high damn try again lol')
    if guess == number:
        break
if guess == number:
    print('haha smart guy')
else:
    print('just go run it back, u trippin :[')
