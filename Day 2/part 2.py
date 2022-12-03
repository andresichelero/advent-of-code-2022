import fileinput

final_points = 0
for line in fileinput.input(files=('input.txt')):
    if line != '\n':
        test = line.split(' ')
        points = 0            
        #Draw
        if test[1] == "Y\n":
            if test[0] == "A":
                points += 4
            elif test[0] == "B":
                points += 5
            elif test[0] == "C":
                points += 6
        #Win                    
        elif (test[1] == "Z\n"):
            if test[0] == "A":
                points += 8
            elif test[0] == "B":
                points += 9
            elif test[0] == "C":
                points += 7               
        #Lose
        elif (test[1] == "X\n"):
            if test[0] == "A":
                points += 3
            elif test[0] == "B":
                points += 1
            elif test[0] == "C":
                points += 2   
        final_points += points
        print(final_points)