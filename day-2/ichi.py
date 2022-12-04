Y = 2 # paper
X = 1 # rock
Z = 3 # scissors

WIN = 6
LOOSE = 0
DRAW = 3

def func(a: str, b: str) -> int:
  if a == 'A': # if rock
    if b == 'Y' : return Y + WIN
    if b == 'X': return X + DRAW
    if b == 'Z': return Z + LOOSE
  if a == 'B': # if paper
    if b == 'Y' : return Y + DRAW
    if b == 'X': return X + LOOSE
    if b == 'Z': return Z + WIN
  if a == 'C': #if scissors
    if b == 'Y' : return Y + LOOSE
    if b == 'X': return X + WIN
    if b == 'Z': return Z + DRAW

myScore = 0

with open('./input.txt', 'r') as r:
  for line in r.readlines():
    args = line.replace('\n', '') # remove that linebreak -_-
    a, b = args.split(' ')
    myScore += func(a, b)

print(myScore)