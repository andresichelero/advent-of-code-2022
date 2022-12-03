import fileinput

final_points = 0
for line in fileinput.input(files=('input.txt')):
    if line != '\n':
        test = line.split(' ')
        points = 0            
        if (test[0] == "A" and test[1] == "X\n") or (test[0] == "B" and test[1] == "Y\n") or (test[0] == "C" and test[1] == "Z\n"):
            points += 3
            if test[1] == "X\n":
                points += 1
            elif test[1] == "Y\n":
                points += 2
            elif test[1] == "Z\n":
                points += 3                    
        elif (test[0] == "A"):
            if test[1] == "Y\n":
                points += 8
            elif test[1] == "Z\n":
                points += 3                
        elif (test[0] == "B"):
            if test[1] == "X\n":
                points += 1
            elif test[1] == "Z\n":
                points += 9 
        elif (test[0] == "C"):
            if test[1] == "X\n":
                points += 7
            elif test[1] == "Y\n":
                points += 2
        final_points += points
        print(final_points)