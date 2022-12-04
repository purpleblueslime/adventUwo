ROCK = 1 # rock
PAPER = 2 # paper
SCISSORS = 3 # scissors

WIN = 6
LOOSE = 0
DRAW = 3

def func(a: str, b: str) -> int:
  if a == 'A': # if rock
    if b == 'Y' : return ROCK + DRAW
    if b == 'X': return SCISSORS + LOOSE
    if b == 'Z': return PAPER + WIN
  if a == 'B': # if paper
    if b == 'Y' : return PAPER + DRAW
    if b == 'X': return ROCK + LOOSE
    if b == 'Z': return SCISSORS + WIN
  if a == 'C': #if scissors
    if b == 'Y' : return SCISSORS + DRAW
    if b == 'X': return PAPER + LOOSE
    if b == 'Z': return ROCK + WIN

myScore = 0

with open('./input.txt', 'r') as nf:
  for line in nf.readlines():
    args = line.replace('\n', '') # remove that linebreak -_-
    a, b = args.split(' ')
    myScore += func(a, b)

print(myScore)