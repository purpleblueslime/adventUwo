grps = []
val = 0

with open('input.txt', 'r') as r:
  for line in r.readlines():
    if (line == '\n'):
      grps.append(val)
      val = 0
      continue
    i = line.replace('\n', '') # remove that linebreak -_-
    val += int(i)

grps.append(val) # to append last group's val

grps.sort()
som = sum([grps.pop(), grps.pop(), grps.pop()])
print(som)