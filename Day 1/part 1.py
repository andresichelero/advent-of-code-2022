import fileinput
elfs = []
iter = 0
sum = 0
for line in fileinput.input(files=('input.txt')):
    if line != '\n':
        sum += int(line)
    else:
        elfs.append(sum)
        iter += 1
        sum = 0
elfs.sort()
print(elfs)