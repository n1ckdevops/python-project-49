import prompt
from brain_games.cli import welcome_user


def set_out(module):
    # WELCOME LINES
    player_name: str = welcome_user()
    print(module.GAME_MESSAGE)
    # SETTING OUT THE GAME
    attempts = 0
    while attempts != 3:
        question: str
        question, correct_answer = module.game_settings()
        print(question)
        player_answer = prompt.string("Answer: ")
        attempts += 1
        if player_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{player_answer} is wrong answer ;(. Correct "
                  f"answer was {correct_answer}")
            print(f"Let's try again, {player_name}!")
            attempts = 3
    print(f"Congratulations, {player_name}!")
