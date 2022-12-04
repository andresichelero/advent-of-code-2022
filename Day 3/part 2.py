common = set()
elves = 0
sum = 0
with open("input.txt", "r+") as f:
  for line in f.readlines():
    elves += 1
    carry = set([el for el in line.rstrip()])
    common = carry if elves % 3 == 1 else common.intersection(carry)    
    if (elves % 3 == 0):      
      badge = list(common)[0]
      common = set()       
      if badge == badge.upper():
        p = ord(badge) - 65 + 27        
      else:
        p = ord(badge) - 97 + 1      
      sum += p
print(sum)