# f = 'input-example.txt' # 36
f = 'input.txt'

TARGET_VALUE=9
reachables = set()
global grid
start = (-1,-1)

def isOutOfBounds(x, y):
  return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def hike(prev, x, y):
  if isOutOfBounds(x, y):
    return

  g = grid[y][x]
  
  if g == '.':
    return

  value = int(g)
  if value != prev + 1:
    return

  if value == TARGET_VALUE:
    reachables.add((start, (x, y)))
    return

  for direction in [ [0,1], [0,-1], [1,0], [-1,0] ]:
    dx, dy = direction
    hike(value, x + dx, y + dy)
  
def go():
  global start
  global grid
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      if grid[y][x] == '0':
        start = (x, y)
        hike(-1, x, y)
  return len(reachables)

def main():
  global f, grid
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    return go()

if __name__ == '__main__':
  print(main())