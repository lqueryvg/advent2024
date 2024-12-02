# f = 'day02/input-example.txt'
f = 'day02/input.txt'

def getDiffs(line):
  return [line[i + 1] - line[i] for i in range(len(line) - 1)]

def getDirection(n):
  if n > 0:
    return 1
  if n < 0:
    return -1
  return 0

def getExpectedDirection(diffs):
    # get the direction of the sum of all directions of the differences
    return getDirection(sum([getDirection(diff) for diff in diffs]))

def isSafe(report):
  errorCount = 0
  reportDiffs = getDiffs(report)
  expectedDirection = getExpectedDirection(reportDiffs)

  if expectedDirection == 0:
    # can't predict the direction so the report can't be safe
    return False

  def diffIsValid(diff):
    return abs(diff) <= 3 and getDirection(diff) == expectedDirection

  for diffIndex, thisDiff in enumerate(reportDiffs):

    if not diffIsValid(thisDiff):
      errorCount += 1
      if errorCount > 1:
        return False # don't tolerate 2 errors

      if diffIndex == 0:
        newDiff = reportDiffs[diffIndex+1] + thisDiff
        if diffIsValid(newDiff):
          # the second level is wrong: ignore it by
          # merging the first diff into the second
          reportDiffs[diffIndex+1] = newDiff
        continue
        
      elif diffIndex < len(reportDiffs) - 1:
        reportDiffs[diffIndex+1] += thisDiff
  
  return True

def main(lines):
  safeCount = 0
  for line in lines:
    a = list(map(int, line))
    if isSafe(a):
      safeCount += 1
  print(safeCount)

with open(f) as f:
  lines = f.readlines()
  lines = [line.strip().split(' ') for line in lines]
  main(lines)