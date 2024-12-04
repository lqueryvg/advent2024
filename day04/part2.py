# f = 'day04/input-example.txt'
f = 'day04/input.txt'

grid = []
def checkCell(x, y, char):
  if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
    return False
  return grid[x][y] == char

def checkCross(x, y, chars):
  return \
    checkCell(x-1, y-1, chars[0]) and \
    checkCell(x+1, y+1, chars[1]) and \
    checkCell(x-1, y+1, chars[2]) and \
    checkCell(x+1, y-1, chars[3])
  
def main():
  count = 0
  for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
      if grid[x][y] == 'A' and (\
        checkCross(x,y, 'MSMS') or \
        checkCross(x,y, 'MSSM') or \
        checkCross(x,y, 'SMMS') or \
        checkCross(x,y, 'SMSM') \
      ):
        count += 1
  return count
 
with open(f) as f:
  lines = f.readlines()
  grid = [line.strip() for line in lines]
  print(main())