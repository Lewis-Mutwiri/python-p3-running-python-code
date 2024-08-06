# lib/app.py

print("Hello World! Pass this test, please.");
dog_name = "Lucy"
print(f"my dogs name is {dog_name}")
list = ['A' , 'B' , 'C']
list.append('D')
print(list)
list.pop()
print(list)
list.sort()
print(list)
list.insert(0, "Baby")
print(list)
import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    guess = None
    number_of_guesses = 0
    
    while guess != number_to_guess:
        guess = int(input("Take a guess: "))
        number_of_guesses += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number in {number_of_guesses} tries.")
            
if __name__ == "__main__":
    guess_the_number()
