sum = 0
with open("input.txt", "r+") as f:
  for line in f.readlines():
    inside = [el for el in line.rstrip()]
    comp1 = set(inside[:len(inside)//2])
    comp2 = set(inside[len(inside)//2:])
    el = list(comp1.intersection(comp2))[0]
    if el == el.upper():
      char = ord(el) - 65 + 27
    else:
      char = ord(el) - 97 + 1
    sum += char
print(sum)