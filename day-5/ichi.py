stacks = {
  '1': ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
  '2': ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
  '3': ['C', 'B', 'S', 'N', 'W'],
  '4': ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
  '5': ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
  '6': ['J', 'V', 'T', 'W', 'M', 'N'],
  '7': ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
  '8': ['B', 'D', 'Z'],
  '9': ['M', 'N', 'Z', 'W']
} # ik this is kinda scummy but im too busy with highschool sorry >,<

def func(move: int, frm: str, to: str) -> None:
  for i in range(move):
    stacks[to].append(
      stacks[frm].pop()
    )
  return

with open('./input.txt', 'r') as r:
  for line in r.readlines():
    line = line.replace('\n', '') # remove that linebreak -_-
    args = line.split(' ')
    for arg in args:
      try: int(arg) 
      except: args.remove(arg)
    move, frm, to = args
    func(int(move), frm, to)

for stack in stacks:
  print(stacks[stack].pop(), end='')