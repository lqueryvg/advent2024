# f = 'input-example.txt'
# f = 'example-tiny.txt'
f = 'input.txt'

ants = {}
nodes = set()
global grid

def addNode(x, y):
  # print(f"l({lx=},{ly=}), r({rx=},{ry=}) d({dx=},{dy=}) n=({nx=}, {ny=})")
  if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
    return
  nodes.add(f"{x},{y}")

def main():
  # print(grid)
  for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
      v = grid[y][x]
      if v != '.':
        if v not in ants:
          ants[v] = []
        ants[v].append([x,y])
  
  # print(f"{ants=}")

  for k in ants:
    kants = ants[k]
    # print(f"{k=} {kants=}")
    for l in range(0, len(kants)):
      for r in range(l + 1, len(kants)):
        [lx, ly] = kants[l]
        [rx, ry] = kants[r]
        [dx, dy] = [rx - lx, ry - ly]

        [nx, ny] = [rx + dx, ry + dy]
        # print(f"l({lx=},{ly=}), r({rx=},{ry=}) d({dx=},{dy=}) n=({nx=}, {ny=})")
        addNode(nx, ny)

        [nx, ny] = [lx - dx, ly - dy]
        # print(f"l({lx=},{ly=}), r({rx=},{ry=}) d({dx=},{dy=}) n=({nx=}, {ny=})")
        addNode(nx, ny)

      # count += 1
  # print(f"{nodes=}")
  return len(nodes)
 
if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    print(main())