vals = {}

val = 1
for typey in (range(65,91), range(97,123)): # a-z = (65,91), A-Z = (97,123)
  for char in typey:
    vals[chr(char)] = val
    val += 1

def func(string: str) -> int:
  mid = round(len(string) / 2)
  firsto = string[:mid]
  secondo = string[mid:]
  for char in firsto:
    if char in secondo: 
      return vals[char]
  return 0

priorty = 0
with open('./input.txt', 'r') as nf:
  for line in nf.readlines():
    string = line.replace('\n', '') # remove that linebreak -_-
    priorty += func(string)

print(priorty)