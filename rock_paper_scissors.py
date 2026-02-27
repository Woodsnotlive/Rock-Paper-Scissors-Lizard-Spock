import random

# simple text-based Rock-Paper-Scissors-Lizard-Spock game
# adds replay logic after each round and on invalid input

debug = False  # set to True to show player and cpu choices before results

SYMBOLS = {
    1: '✊',
    2: '✋',
    3: '✌️',
    4: '🦎',
    5: '🖖',
}

# winning relationships: key beats all in the associated list
WINNING_MAP = {
    1: [3, 4],  # rock beats scissors & lizard
    2: [1, 5],  # paper beats rock & spock
    3: [2, 4],  # scissors beats paper & lizard
    4: [2, 5],  # lizard beats paper & spock
    5: [1, 3],  # spock beats rock & scissors
}


def prompt_play_again(message="Play again? (y/n): "):
    resp = input(message).strip().lower()
    return resp == 'y'


def get_player_choice():
    """Prompt the player for a choice and handle invalid input.

    Returns an integer between 1 and 5, or None if the user elects
    not to continue after an invalid attempt.
    """
    while True:
        try:
            choice = int(input('Pick a number: '))
        except ValueError:
            print('Invalid input, that is not a number.')
            if not prompt_play_again('Try again? (y/n): '):
                return None
            continue

        if 1 <= choice <= 5:
            return choice
        else:
            print('Invalid input, number must be 1–5.')
            if not prompt_play_again('Try again? (y/n): '):
                return None


def determine_result(player, cpu):
    if cpu == player:
        return "It's a draw!"
    if cpu in WINNING_MAP.get(player, []):
        return 'You win!'
    return 'You lose'


def show_menu():
    print('1) ✊')
    print('2) ✋')
    print('3) ✌️')
    print('4) 🦎')
    print('5) 🖖')


def main():
    print('================================')
    print('Rock Paper Sissors Lizard Spock')
    print('================================\n')

    while True:
        show_menu()
        player = get_player_choice()
        if player is None:
            break

        cpu = random.randint(1, 5)
        print('')

        if debug:
            print('DEBUG:', player, cpu)

        print(determine_result(player, cpu))
        print('You chose:', SYMBOLS[player])
        print('Cpu chose:', SYMBOLS[cpu])
        print('')

        if not prompt_play_again():
            break


if __name__ == '__main__':
    main()
