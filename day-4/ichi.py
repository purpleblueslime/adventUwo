def func(a: int, aa: int, b: int, bb: int) -> int:
  return (a <= b and aa >= bb) or (a >= b and aa <= bb)

elves = 0
with open('./input.txt', 'r') as r:
  for line in r.readlines():
    args = line.replace('\n', '') # remove that linebreak -_-
    a, b = args.split(',') 
    a, aa = a.split('-')
    b, bb = b.split('-')
    elves += func(int(a), int(aa), int(b), int(bb))

print(elves)