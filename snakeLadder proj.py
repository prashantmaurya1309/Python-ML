import random

max_limit = 100
n = int(input('enter numbers of player participating:'))

name=[]
game={}
roll_dice_value=[1,2,3,4,5,6]
# name is list of players participating
for i in range(n):
    name.append(input(f'enter player{i+1} name:'))


# 2 dictionaries are made to represent where ladders and snakes are


Position_of_snakes= {17 : 7, 54 : 34, 62 : 19, 98 : 79}
Position_of_ladders= {3 : 38, 24 : 33, 42 : 93, 72 : 84}


# game is another dictionary in which we take player name as key and its value as its
# curent postion in game

for i in range(n):
    game[name[i]] = 0

print('*'*10,'LETS START','*'*10)
print('enter roll to roll the dice \n or write a number to enter manual mode')

# we run 2 loops
# in outer loop will break only if anyone of player reach at max position i.e. 100
# inner loop will run the player one by one until one win

while game[name[0]] != max_limit and game[name[1]] != max_limit:

    for i in range(n):
        # we are taking comand here to know what does player want to do
        # in this case we have two active command i.e. manual and roll


        cmd = input(f'player {i}: ')


        # if we get roll as cmd then a random number will be given from 1-6 and player will change his
        # position according to it

        if cmd.lower() == 'roll':
            value = random.choice(roll_dice_value)
            print(f'player {i} got {value}')

            # after rolling if the player next position is in limit then

            if game[name[i]] + value < max_limit:

                # if next position is in ladder foot then he will clib ladder and his next postion will become
                # at head of the ladder

                if game[name[i]] + value in Position_of_ladders.keys():
                    game[name[i]] = Position_of_ladders[game[name[i]] + value]
                    print('YAY!! took the ladder')
                    print(f'player {i} at {game[name[i]]} position')


                elif (game[name[i]] + value) in Position_of_snakes.keys():

                    # if next position of player is at head of snake then he will reach at tail of the snake

                    game[name[i]] = Position_of_snakes[game[name[i]] + value]
                    print('got BITTEN BY snake SAD!!!')
                    print(f'player {i} at {game[name[i]]} position')
                else:

                    # if next postion is free of ladders and snakes then he will update his position accordingly

                    up_date = {name[i]: game[name[i]] + value}
                    game.update(up_date)
                    print(f'player {i} at {game[name[i]]} position')

            elif (game[name[i]] + value) == max_limit:

                # if next position reach at max limit of game then he will win and game will get overr

                print(f'player {i} won the game')
                break
            else:

                # if his next position is out of range i.e. more than 100 then he has to wait for next turn
                # and no change will be there at his position

                print('you got value that exceed max value \n so wait')

        elif cmd.lower() == 'manual':

            # if comand is manual then player can enter any number he wants and his poition will change accordingly

            v= int(input('enter number:'))
            print(f'player {i} chose manual mode \n and will be moved by {v} ')
            if (game[name[i]] + v) < max_limit:
                if (game[name[i]] + v) in Position_of_ladders.keys():
                    game[name[i]] = Position_of_ladders[game[name[i]] + v]
                    print('YAY!! took the ladder')
                    print(f'player {i} at {game[name[i]]} position')
                elif (game[name[i]] + v) in Position_of_snakes.keys():
                    game[name[i]] = Position_of_snakes[game[name[i]] + v]
                    print('got BITTEN BY snake SAD!!!')
                    print(f'player {i} at {game[name[i]]} position')
                else:
                    up_date = {name[i]: game[name[i]] + v}
                    game.update(up_date)
                print(game[name[i]])
            elif (game[name[i]] + v) == max_limit:
                print(f'player {i} won the game')
                game[name[i]] = game[name[i]] + v
                break
            else:
                print('you got value that exceed max value \n so wait')

        elif cmd.lower() == 'quit':
            game.pop(name[i])
            n =-1
            if len(game) == 1:
                print('game is over other player won by default')
                game[name[0]] = max_limit