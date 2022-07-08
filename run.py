import random

# Pairing the attack options determine who wins and loses
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

sheldon_attack = random.choice(attack_options)

# Prints the start of game options to the player
print('Choose your weapon from the options below: ')
print(' -> 0 for Rock\n -> 1 for Paper\n -> 2 for Scissors\n -> 3 for Lizard\n -> 4 for Spock')

player_input = int(input('Enter your choice of attack (0-4): '))

player_attack = attack_options[player_input]
