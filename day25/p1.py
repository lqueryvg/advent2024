F = 'input-example.txt'
F = 'input.txt'

def readKeysAndLocks(lines: list[str]) -> tuple[list[list[int]], list[list[int]]]:
  locks: list[list[int]] = []
  keys: list[list[int]] = []

  rankNum = 0
  isLock = False
  heights = [0,0,0,0,0]
  def addHeights():
    if isLock:
      locks.append(heights)
    else:
      keys.append(heights)

  for line in lines:
    if line == '':
      addHeights()
      rankNum = 0
      continue

    if rankNum == 0:
      isLock = line == "#####"
      if isLock:
        heights = [0,0,0,0,0]
      else:
        heights = [5,5,5,5,5]

      rankNum += 1
      continue

    for i, c in enumerate(line):
      if isLock:
        if c == '#':
          heights[i] = rankNum
      else:
        if c == '.':
          heights[i] = 5 - rankNum

    rankNum += 1

  addHeights()

  return (keys, locks)

def keyFitsLock(key, lock):
  for i, k in enumerate(key):
    if k + lock[i] > 5:
      return False
  return True

def go(lines) -> int:
  locks, keys = readKeysAndLocks(lines)
  count = 0
  for key in keys:
    for lock in locks:
      fits = keyFitsLock(key, lock)
      if fits:
        count += 1


  return count

def main():
  with open(F) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    return go(lines)

if __name__ == '__main__':
  print(main())