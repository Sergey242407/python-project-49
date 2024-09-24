import random
import brain_games.cli as cli


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    return number, is_even(number)


def main():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds = 3

    for _ in range(rounds):
        number, correct_answer = generate_question()
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        if (user_answer == "yes" and correct_answer) or \
           (user_answer == "no" and not correct_answer):
            print("Correct!")
        else:
            correct_str = "yes" if correct_answer else "no"
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_str}'.")
            print(f"Let's try again, {name}!")
            break

        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
