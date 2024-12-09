# f = 'input-example.txt'
f = 'input.txt'

ants = {}
nodes = set()
global grid

def isOutOfBounds(x, y):
  return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def addLine(point, delta):
  x, y = point
  while True:
    nodes.add(f"{x},{y}")
    x += delta[0]
    y += delta[1]
    if isOutOfBounds(x, y):
      return

def main():
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      f = grid[y][x]
      if f != '.':
        if f not in ants:
          ants[f] = []
        ants[f].append([x,y])
  
  for k in ants:
    kants = ants[k]
    for l in range(0, len(kants)):
      for r in range(l + 1, len(kants)):
        [lx, ly] = kants[l]
        [rx, ry] = kants[r]
        [dx, dy] = [rx - lx, ry - ly]

        addLine(kants[l], [-dx, -dy])
        addLine(kants[r], [dx, dy])

  return len(nodes)
 
if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    print(main())