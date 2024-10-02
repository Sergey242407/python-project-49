import random
from brain_games.games import play_game


def is_prime(num):
    if num < 2:
        return True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def get_correct_answer(number):
    return 'yes' if is_prime(number) else 'no'


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    number = random.randint(1, 1000)
    return number, get_correct_answer(number)


def main():
    play_game(generate_question, rules)


if __name__ == '__main__':
    main()
