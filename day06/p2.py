# f = 'input-example.txt'
# f = 'example-tiny.txt'
f = 'input.txt'

grid = []
startX = -1
startY = -1

def findStart():
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      if grid[y][x] == '^':
        return x, y

  raise Exception(f"Unable to find guard")

def turn(direction):
  dx, dy = direction
  if dx == 0:
    return [-dy, 0]
  if dy == 0:
    return [0, dx]
  
  raise ValueError(f"invalid direction {direction}")

def isInBounds(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def makesLoop(ox, oy): # obstacle coords
  visited = set()
  gx, gy = startX, startY

  d = [0, -1] # direction

  def addVisited():
    s = f"{gx},{gy},{d}"
    visited.add(s)
  
  addVisited()

  while True:
    x = gx + d[0]
    y = gy + d[1]

    if not isInBounds(x, y):
      break

    if (x == ox and y == oy) or grid[y][x] == '#':
      d = turn(d)
      addVisited()
      continue

    gx = x
    gy = y
    s = f"{gx},{gy},{d}"
    if s in visited:
      return True

    addVisited()

  return False

def main():
  count = 0
  global startX, startY
  startX, startY = findStart()

  for y in range(0, len(grid)):
    print(f"{y=}")
    for x in range(0, len(grid[y])):
      if makesLoop(x, y):
        count += 1

  return count

if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    print(main())
