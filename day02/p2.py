# f = 'input-example.txt'
# f = 'input-example2.txt'
f = 'input.txt'

"""
No sorting.
No brute force.
This is done by analysing the diffs.
"""

def getDiffs(line):
  return [line[i + 1] - line[i] for i in range(len(line) - 1)]

def getDirection(n):
  if n > 0:
    return 1
  if n < 0:
    return -1
  return 0

def getExpectedDirection(diffs):
    # get the direction of the sum of all drections of the differences
    return getDirection(sum([getDirection(diff) for diff in diffs]))

def isSafe(report):
  errorAlreadyFound = False
  reportDiffs = getDiffs(report)
  expectedDirection = getExpectedDirection(reportDiffs)

  if expectedDirection == 0:
    # can't predict the direction so the report can't be safe
    return False

  def diffIsValid(diff):
    return abs(diff) <= 3 and getDirection(diff) == expectedDirection

  for diffIndex, thisDiff in enumerate(reportDiffs):

    if not diffIsValid(thisDiff):
      if errorAlreadyFound: return False # do not tolerate more than one error
      errorAlreadyFound = True
      
      # the last diff has the error, we can skip it and declare the report safe
      if diffIndex >= len(reportDiffs) - 1:
        return True 

      if diffIndex == 0:
        # if next diff is valid, the left level
        # must be invalid so skip it
        if diffIsValid(reportDiffs[diffIndex+1]): continue

        # the next diff is ok, so the level on the right must be invalid
        # skip it by merging the first diff into the second
        reportDiffs[diffIndex+1] += thisDiff

        continue
      
      # an error somewhere between first and last diff
      # skip the level on the right by merging this diff into the next diff
      reportDiffs[diffIndex+1] += thisDiff
  
  return True

def main(lines):
  safeCount = 0
  for line in lines:
    a = list(map(int, line))
    if isSafe(a):
      safeCount += 1
  print(safeCount)

if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip().split(' ') for line in lines]
    main(lines)