import random

# values = []
# for i in range(1,10):
#     values.append(i)

# List Comprehension
values = [i for i in range(1,10)]

def gameBoard():
    print("""
        {}   |   {}   |   {}
     -----------------------
        {}   |   {}   |   {}
     -----------------------
        {}   |   {}   |   {}
    """.format(values[0],values[1],values[2],values[3],values[4],values[5],values[6],
               values[7],values[8]))

def checkWinner(pos_1,pos_2,pos_3,player):
    if values[pos_1] == player and values[pos_2] == player and values[pos_3] == player:
        return True

def checkConditions(player):
    # if values[0] == 'X' and values[1] == 'X' and values[2] == 'X':
    #     pass
    # elif values[0] == 'X' and values[3] == 'X' and values[6] == 'X':
    #     pass
    if checkWinner(0,1,2,player):
        return True
    elif checkWinner(0,3,6,player):
        return True
    elif checkWinner(0,4,8,player):
        return True
    elif checkWinner(1,4,7,player):
        return True
    elif checkWinner(2,5,8,player):
        return True
    elif checkWinner(3,4,5,player):
        return True
    elif checkWinner(6,7,8,player):
        return True
    elif checkWinner(2,4,6,player):
        return True

def main():
    game = True
    choice = True
    cpu = True
    posOccupied = []

    while choice:
        userCh = input("Enter your choice (X or 0): ")
        if userCh == "0":
            cpuCh = 'X'
            choice = False
        elif userCh == 'X':
            cpuCh = '0'
            choice = False
        else:
            print("Invalid Choice")
            choice = True

    while game:
        gameBoard()

        positionTaken = True
        while positionTaken:
            pos = int(input("Enter your position : "))
            if len(posOccupied) > 1:
                for position in posOccupied:
                    if position == pos:
                        print("Position Already Occupied, Enter Again...")
                        break
                else:
                    positionTaken = False
            elif pos > 9 :
                print("Invalid choice")
            else:
                positionTaken = False

        values[pos - 1] = userCh
        posOccupied.append(pos)

        gameBoard()
        if checkConditions(userCh):
            print("User Wins...")
            game = False
            break

        cpu = True
        while cpu:
            cpu_pos = random.randrange(1,10)
            if cpu_pos not in posOccupied:
                values[cpu_pos - 1] = cpuCh
                print("CPU Picked", cpu_pos)
                posOccupied.append(cpu_pos)
                cpu = False
            elif cpu_pos in posOccupied:
                cpu = True
        if checkConditions(cpuCh):
                print("CPU Wins...")
                game = False

main()