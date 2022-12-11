def func(cmd: str) -> int:
  args = cmd.split(' ')
  for arg in args:
    try: return int(arg)
    except: return 0
  return 0

dirs = {}
cat = []

with open('./input.txt', 'r') as r:
  for line in r.readlines():
    cmd = line.replace('\n', '') # remove that linebreak -_-
    if '$ cd' in cmd: # on cd cmd
      a, b, c = cmd.split(' ')
      if c == '..': # went back in dir
        cat.pop()
      if c != '..': # went ahead in dir
        cat.append(c)
    if '$' in cmd: continue # skip func(cmd) on cmd with $
    loc = '' # we need full dir location cause of dirs with same names
    for d in cat:
      pth =  f'{loc}{d}'
      if pth not in dirs: dirs[pth] = 0  # if dir isn't already there in dirs 
      dirs[pth] += func(cmd)
      if d == '/': loc += d
      else: loc += f'{d}/'

som = 0
for d in dirs:
  if dirs[d] <= 100000: # 100000 = size cap
    som += dirs[d]

print(som)