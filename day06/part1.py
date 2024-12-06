# f = 'input-example.txt'
# f = 'example-tiny.txt'
f = 'input.txt'

grid = []

def findStart():
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      if grid[y][x] == '^':
        return x, y

  raise Exception(f"Unable to find guard")

def rotateDirectionClockwise(d):
  # print("turn")
  if d[0] == 0:
    if d[1] == -1:
      return [1, 0]
    if d[1] == 1:
      return [-1, 0]
  if d[1] == 0:
    if d[0] == -1:
      return [0, -1]
    if d[0] == 1:
      return [0, 1]
  raise Exception(f"Invalid direction: {d}")

def isInBounds(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def main():
  visited = set()
  gx, gy = findStart()
  s = f"{gx},{gy}"
  visited.add(s)

  d = [0, -1] # direction
  while True:
    # print(f"{gx=}, {gy=} {d=}")
    x = gx + d[0]
    y = gy + d[1]

    if not isInBounds(x, y):
      break

    if grid[y][x] == '#':
      d = rotateDirectionClockwise(d)
      continue

    gx = x
    gy = y
    s = f"{gx},{gy}"
    if s not in visited:
      visited.add(s)

  return len(visited)
  
if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]

    print(main())
