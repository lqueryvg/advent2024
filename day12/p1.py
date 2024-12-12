f = 'input.txt'

grid = []
visited = set()

def isOutOfBounds(x, y):
  return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def go(x: int, y: int, plant: str) -> tuple[int, int]:

    # Check end conditions
    if isOutOfBounds(x, y):
        return (0, 1)  # add fence

    # Different plant
    if grid[y][x] != plant:
        return (0, 1)  # different plant so add 1 fence

    if (x, y) in visited:
        # Same plant, already visited
        return (0, 0)  # add nothing

    # Same plant, not visited yet
    visited.add((x, y))
    area = 1
    fences = 0

    for direction in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        dx, dy = direction
        (a, f) = go(x + dx, y + dy, plant)
        area += a
        fences += f

    return (area, fences)


def main():
  global f, grid
  with open(f) as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
    
    cost = 0
    for y in range(0, len(grid)):
      for x in range(0, len(grid[y])):
        (area, fences) = go(x, y, grid[y][x])
        cost += area * fences

    return cost

if __name__ == '__main__':
  print(main())