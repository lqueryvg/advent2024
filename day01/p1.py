# f = 'day01/input-example.txt'
f = 'day01/input.txt'

def main(lines):
  left = []
  right = []

  for line in lines:
    a = list(map(int, line))
    left.append(a[0])
    right.append(a[1])
  
  total = 0
  for l, r in zip(sorted(left), sorted(right)):
    total += abs(l - r)

  print(total)

with open(f) as f:
  lines = f.readlines()
  lines = [line.strip().split() for line in lines]
  main(lines)