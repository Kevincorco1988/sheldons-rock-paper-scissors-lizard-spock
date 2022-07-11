import random
import emoji


def runGame():
    # While loop which allows player to choose best out of 3 or 5.
    while True:
        try:
            best_of = int(input('Shall we play best of (3 or 5) rounds?:\n '))
            if best_of == 3 or best_of == 5:
                break
            else:
                print('Invalid choice...You' 
                      'must choose either' 
                      'best of 3 or 5.')
        except ValueError:
            print('Invalid choice...You must choose either best of 3 or 5.')


    needed_wins = int(best_of/2) + 1

    player_wins = 0
    sheldon_wins = 0

    # Pairing the attack options to determine who wins and loses
    winning_losing_pairs = [('Scissors', 'Paper'),
                            ('Paper', 'Rock'),
                            ('Rock', 'Lizard'),
                            ('Lizard', 'Spock'),
                            ('Spock', 'Scissors'),
                            ('Scissors', 'Lizard'),
                            ('Lizard', 'Paper'),
                            ('Paper', 'Spock'),
                            ('Spock', 'RocK'),
                            ('Rock', 'Scissors')]

    attack_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


    while True:
        sheldon_attack = random.choice(attack_options)

        # Prints the start of game options to the player
        print(emoji.emojize('The game is Rock :brick:,'
                            'Paper :scroll:, Scissors :scissors:, Lizard :'
                            'lizard:, Spock \U0001F47D \U0001F596\n 🙂'))
        print('Choose your attack from the options below 👀: ')
        print(emoji.emojize(' -> 0 for Rock'
                            ':brick:\n -> 1 for Paper'
                            ':scroll:\n -> 2 for Scissors'
                            ':scissors:\n -> 3 for Lizard'
                            ':lizard:\n -> 4 for Spock \U0001F47D \U0001F596'))

        while True:
            try:
                player_input = int(input('Enter' 
                                         'your choice'
                                         'of attack (0-4): '))
                if player_input not in range(5):
                    raise IndexError

                break
            except IndexError:
                print('You must choose a number from (0-4)')

        player_attack = attack_options[player_input]

        # Gives the result of the round 
        # and a statement from Sheldon regarding the result.
        if sheldon_attack == player_attack:
            result = ('Judge rules...Draw!!'
                      '... It seems that I may' 
                      'have met my match 😏')
            player_wins += 1

        elif (player_attack, sheldon_attack) in winning_losing_pairs:
            result = ('Judge rules...'
                      'You win that round...' 
                      'Lets see if you can keep it up 🤨')
            sheldon_wins += 1
        else:
            result = 'Judge rules...I win!!....another step towards victory 😃'
            sheldon_wins += 1

        print('-----------------------------------')
        print('Players attack: ', player_attack)
        print('Sheldons attack: ', sheldon_attack)
        print('Sheldons judgement: ', result)
        print('-----------------------------------')
        if sheldon_wins == needed_wins or player_wins == needed_wins:
            break

    # Displays the outcome/winner of the best_of game.
    if player_wins > sheldon_wins:
        print('You have defeated me. Live long and prosper \U0001F596')
    else:
        print('You lose... Bazinga!! 😈')

    while True:
        challenge_again = input('Would you like to challenge' 
                                'me again?🏆 (Y/N): ')
        if challenge_again.lower() == 'n':
            break
        elif challenge_again.lower() == 'y':
            runGame()


runGame()