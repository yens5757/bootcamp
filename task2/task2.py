import random

def generate_number():
    return random.randint(1, 100)

def user_guess(low, high):
    while True:
        guess = input(f"guess a number between {low} and {high}: ")
        # checks if guess is a correct input
        if not guess.isdigit():
            print(f"please enter a number from {low} to {high}")
            continue
        guess = int(guess)
        if guess < low or guess > high:
            print(f"please enter a number within {low} to {high}")
            continue
        else:
            return guess
        
def check_guess(ans, guess, low, high):
    if guess > ans:
        print("Lower!")
        return low, guess
    elif guess < ans:
        print("Higher!")
        return guess, high
    else:
        return ans, ans

def game_over(tries):
    print(f"You win! You got it in {tries} tries!")

def main():
    ans = generate_number()
    low, high = 1, 100
    tries = 0
    while True:
        tries += 1
        guess = user_guess(low, high)
        low, high = check_guess(ans, guess, low, high)
        if low == high:
            break
    game_over(tries)
    

main()