import random

debug = True

print('================================')
print('Rock Paper Sissors Lizard Spock')
print('================================')
print('')

player = 0
cpu = 0

print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')

player = int(input('Pick a number: '))
cpu = random.randint(1, 5)
print('')

if debug == True:
    print(player)
    print(cpu)4

if cpu == player:
    print('Its a draw!')

if cpu == 1 and player != 3 and player != 4:
    print('You win!')
elif cpu == 2 and player != 3 and player != 4:
    print('You win!')
elif cpu == 3 and player != 1 and player != 5:
    print('You win!')
elif cpu == 4 and player != 1 and player != 3:
    print('You win!')
elif cpu == 5 and player == 4 and player == 2:
    print('You win!')
else:
    print('You lose')

if player == 1:
    player = '✊'
elif player == 2:
    player = '✋'
elif player == 3:
    player = '✌️'
elif player == 4:
    player = '🦎'
elif player == 5:
    player = '🖖'

if cpu == 1:
    cpu = '✊'
elif cpu == 2:
    cpu = '✋'
elif cpu == 3:
    cpu = '✌️'
elif cpu == 4:
    cpu = '🦎'
elif cpu == 5:
    cpu = '🖖'


print('You chose: ' + player)
print('Cpu chose: ' + cpu)