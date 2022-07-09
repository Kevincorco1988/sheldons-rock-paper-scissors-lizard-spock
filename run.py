import random
import emoji

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

sheldon_attack = random.choice(attack_options)

# Prints the start of game options to the player
print(emoji.emojize('The game is Rock :brick:, Paper :scroll:, Scissors :scissors:, Lizard :lizard:, Spock \U0001F47D \U0001F596 and it will be the best out of 5 games 🙂'))
print('Choose your weapon from the options below 👀: ')
print(emoji.emojize(' -> 0 for Rock :brick:\n -> 1 for Paper :scroll:\n -> 2 for Scissors :scissors:\n -> 3 for Lizard :lizard:\n -> 4 for Spock \U0001F47D \U0001F596'))

player_input = int(input('Enter your choice of attack (0-4): '))

player_attack = attack_options[player_input]

# Gives the result of the game and a statement from Sheldon regarding the result#
if sheldon_attack == player_attack:
    result = 'Judge rules...Draw!!... It seems that I may have met my match 😏'

elif (player_attack, sheldon_attack) in winning_losing_pairs:
    result = 'Judge rules...You win that round... Lets see if you can keep it up 🤨'

else:
    result = 'Judge rules...I win!!....another step towards victory 😃'

print('-----------------------------------')
print('Players attack: ', player_attack)
print('Sheldons attack: ', sheldon_attack)
print('Sheldons judgement: ', result)
print('-----------------------------------')