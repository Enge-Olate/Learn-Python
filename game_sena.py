import random

TOTAL_NUMBERS = 6
MIN_NUMBER = 1
MAX_NUMBER = 60

def get_user_Numbers():
    """ Get six unique numbers from the user. """
    user_numbers =[]
    print(f'Enter {TOTAL_NUMBERS} unique numbers between {MIN_NUMBER}and {MAX_NUMBER}:')
    while len(user_numbers) < TOTAL_NUMBERS:
        try:
            num = int(input(f'Number {len(user_numbers) + 1}:'))
            if num < MIN_NUMBER or num > MAX_NUMBER:
                print(f'Number must be between {MIN_NUMBER} and {MAX_NUMBER}. Try again.')
            elif num in user_numbers:
                print('Number already entered. Try again.')
            else:
                user_numbers.append(num)
        except ValueError:
            print('Invalid input. Please enter a number.')
    return user_numbers

def draw_prize(user_numbers):
    """ Doing the draw and return the winning numbers. """
    winning_numbers = random.sample(range(MIN_NUMBER, MAX_NUMBER +1), TOTAL_NUMBERS)
    user_set = set(user_numbers)
    winning_numbers_set = set(winning_numbers)
    hits = user_set & winning_numbers_set
    print("\nYours numbers:", sorted(user_numbers))
    print("Numbers drawn:", sorted(winning_numbers))
    print(f"Your hits: {len(hits)} - {sorted(hits)}")

    if len(hits) == TOTAL_NUMBERS:
        print("Congratulations! You won the prize!")
    else:
        print("Sorry, better luck next time.")

def main():
    user_numbers = get_user_Numbers()
    draw_prize(user_numbers)

if __name__ == "__main__":
    main()