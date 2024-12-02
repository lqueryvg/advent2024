
# f = 'day02/input-example.txt'
f = 'day02/input.txt'

def getDirection(n):
  if n > 0:
    return 1
  if n < 0:
    return -1
  return 0

def isSafe(report):
  previousValues = {
    'level': None,
    'direction': None
  }
  for level in report:
    level = int(level)
    direction = 0
    if previousValues['level'] is not None:
      diff = level - previousValues['level']
      direction = getDirection(diff)
      if abs(diff) > 3 or diff == 0:
        return False
      if previousValues['direction'] != 0 and direction != previousValues['direction']:
        return False
    
    previousValues['level'], previousValues['direction'] = level, direction
  
  return True

def main(lines):
  safeCount = 0
  for report in lines:
    if isSafe(report):
      safeCount += 1
  
  print(safeCount)

with open(f) as f:
  lines = f.readlines()
  lines = [line.strip().split(' ') for line in lines]
  main(lines)