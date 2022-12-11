def func(cmd: str) -> int:
  args = cmd.split(' ')
  for arg in args:
    try: return int(arg)
    except: return 0
  return 0

dirs = {}
cat = []
totl = 0

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
    _ = func(cmd) # taking this bad boy outside loop cause i can
    totl += _
    for d in cat:
      pth =  f'{loc}{d}'
      if pth not in dirs: dirs[pth] = 0  # if dir isn't already there in dirs 
      dirs[pth] += _
      if d == '/': loc += d
      else: loc += f'{d}/'

ava = 70000000 - totl # space available - sum(alll)
smollst = []
for d in dirs:
  if 30000000 <= ava + dirs[d]: # space required <= ava + dirs[d] 
    smollst.append(dirs[d])

print(min(smollst))