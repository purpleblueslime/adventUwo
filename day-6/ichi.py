def func(chars) -> int:
  for i in range(len(chars)):
    for char in chars[i+1:]: # i+1 cause you don't want that char itself
      if char == chars[i]: return 1
  return 4 # to makw up for nested loop 'for char in chars[i:i+4]'

som = 0
with open('./input.txt', 'r') as r:
  chars = r.read()
  for i in range(len(chars)):
    chrs = []
    for char in chars[i:i+4]:
      chrs.append(char)
    _ = func(chrs)
    som += _
    if (_ == 4): break # if _ == 4: found first start-of-packet

print(som)