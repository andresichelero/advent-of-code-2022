pairs = []
with open("input.txt", "r+") as f:
  for line in f.readlines():
    start1, end1 = map(int, line.split(",")[0].split("-"))
    start2, end2 = map(int, line.split(",")[1].split("-"))
    pairs.append((start1, end1, start2, end2))

count = 0
for (start1, end1, start2, end2) in pairs:
  if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
    count += 1
print(count)