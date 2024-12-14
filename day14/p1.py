import re
f = 'input.txt'
# f = 'input-example.txt'

lines = []

# width = 11
# height = 7
width = 101
height = 103


iterations = 100

counts = {}

def move(x, xi, n, size):
  return (x + (xi*n)) % size

def go():
  global lines
  patt = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

  mx = width // 2
  my = height // 2

  print(f"{mx=}, {my=}")
  
  for line in lines:
    # print(f"{line=}")
    matches = re.findall(patt, line)
    m = matches[0]
    (x, y, xi, yi) = map(int, m)
    nx = move(x, xi, iterations, width)
    ny = move(y, yi, iterations, height)
    print(f"{nx},{ny}")

    if nx == mx or ny == my:
      print("middle")
      continue

    if nx < mx and ny < my:
      counts[1] = counts.get(1, 0) + 1
      print("1")
      continue

    if nx > mx and ny < my:
      counts[2] = counts.get(2, 0) + 1
      print("2")
      continue

    if nx < mx and ny > my:
      counts[3] = counts.get(3, 0) + 1
      print("3")
      continue

    if nx > mx and ny > my:
      counts[4] = counts.get(4, 0) + 1
      print("4")
      continue

  total = 1
  for c in counts:
    total *= counts[c]
  print(f"{total=}")

  print(f"{counts=}")
  return total

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    # lines = lines[0].split(' ')

    return go()

if __name__ == '__main__':
  print(main())