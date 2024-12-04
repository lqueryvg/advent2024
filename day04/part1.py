import re

# f = 'day04/input-example.txt'
f = 'day04/input.txt'

word = 'XMAS'
grid = []

def search(x, y, direction, wordIndex):
  if wordIndex >= len(word):
    return 1
  if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
    return 0
  if grid[x][y] != word[wordIndex]:
    return 0
  return search(x + direction[0], y + direction[1], direction, wordIndex + 1)

def main():
  directions = [ [0,-1], [0,1], [1,-1], [1,0], [1,1], [-1,-1], [-1,0], [-1,1] ]
  count = 0
  for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
      for direction in directions:
        count += search(x, y, direction, 0)
  return count
 
with open(f) as f:
  lines = f.readlines()
  grid = [line.strip() for line in lines]
  print(main())