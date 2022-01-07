import random
lst = ['rock', 'scissor', 'paper']
#  conditions:
#  1. if rock & scissor = rock win
#  2. if scissor & paper = scissor win
#  3. if paper & rock = paper win

while True:
    print('''START GAME 
            1. Play/yse 
            2. Exit/no ''')
    user_input = int(input("enter your choice= "))
    if user_input == 1:
        print('GAME START NOW.....')
        user_score = 0
        computer_score = 0
        for i in range(1, 6):
            computer_choice = random.choice(lst)
            # print(computer_input)
            print("round", i, ''' \n Choose
              1. ROCK
              2. scissor
              3. PAPER
              4. EXIT ''')
            user_choice = int(input())
            if user_choice == 1:
                user_choice = 'rock'
            elif user_choice == 2:
                user_choice = 'scissor'
            elif user_choice == 3:
                user_choice = 'paper'
            else:
                break


            if user_choice == computer_choice:
                user_score = user_score + 1
                computer_score = computer_score + 1
                print(" draw game no ", i)
            elif(user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'scissor' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):

                user_score = user_score+2
                print('you win this game')
            else:
                computer_score = computer_score + 2
                print('computer win this game')

            print(f'you chose {user_choice}, computer chose {computer_choice}, ')
            print(f'Your score ={user_score},computer score = {computer_score}')

        print(f'final result : \n computer total score is {computer_score},\n your score is {user_score}')

        if user_score == computer_score:
            print('GAME DRAW ')
        elif user_score > computer_score:
            print("YOU WIN")
        else:
            print("YOU LOST")
            break

    elif user_input == 2:
        print("you Exit this game")
        break
    else:
        print('Wrong Input')




