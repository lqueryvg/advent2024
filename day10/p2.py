TARGET_VALUE=9
# f = 'input-example.txt'
f = 'input.txt'

reachables = set()
global grid
start = (-1,-1)

def isOutOfBounds(x, y):
  return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def hike(prev, x, y):
  if isOutOfBounds(x, y):
    return 0

  g = grid[y][x]
  
  if g == '.':
    return 0

  value = int(g)
  if value != prev + 1:
    return 0

  if value == TARGET_VALUE:
    reachables.add((start, (x, y)))
    return 1

  total = 0
  for direction in [ [0,1], [0,-1], [1,0], [-1,0] ]:
    dx, dy = direction
    total += hike(value, x + dx, y + dy)
  
  return total

def go():
  global start
  total = 0
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      if grid[y][x] == '0':
        start = (x, y)
        total += hike(-1, x, y)
  return total

def main():
  global f, grid
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    return go()

if __name__ == '__main__':
  print(main())