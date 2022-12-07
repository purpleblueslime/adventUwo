def func(a: int, aa: int, b: int, bb: int) -> int:
  return not (
    (a < b and aa < b) or (a > bb and aa > bb)
  )

elves = 0
with open('./input.txt', 'r') as nf:
  for line in nf.readlines():
    args = line.replace('\n', '') # remove that linebreak -_-
    a, b = args.split(',') 
    a, aa = a.split('-')
    b, bb = b.split('-')
    elves += func(int(a), int(aa), int(b), int(bb))

print(elves)