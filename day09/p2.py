# f = 'input-example.txt'
# f = 'input-example-tiny.txt'
f = 'input.txt'

"""
Approach:
- convert line in a list of "run" tuples each describing
  the file id, run start position and run length (file id='.' for gaps).
- for each file run starting from the right:
  - find the first gap run large enough to fit the file, starting from the left
  - if no gap is found, continue to the next file
  - if a gap large enough was found, reduce the size of the gap (or delete it)
    and insert the file before it
"""

runs = []   # [ (id, pos, len), ... ]

def diskToString():
  # useful for debugging
  # only works on small examples where id is a single char

  s = ''
  for i in range(0, len(runs)):
    id, _, length = runs[i]

    s += str(id) * length # repeat id len time
  return s

def readDisk(line):
  isFree = False
  id = 0
  pos = 0 # position on disk
  for i in range(0, len(line)):
    l = int(line[i]) # length
    runs.append(('.' if isFree else id, pos, l))
    id += 0 if isFree else 1
    pos += l
    isFree = not isFree

def findFirstGapWhichFitsFile(fileIndex):
  (_, fpos, flen) = runs[fileIndex]
  # find first gap to the left of the file which can fit the file
  for i in range(0, fileIndex):
    (gid, gpos, glen) = runs[i]
    if gid == '.' and gpos <= fpos and glen >= flen:
      return i
  return -1

def moveFileIntoGap(fileIndex, gapIndex):
  (gid, gpos, glen) = runs[gapIndex]
  (fid, fpos, flen) = runs[fileIndex]

  # replace file with a gap
  runs[fileIndex] = ('.', fpos, flen)
  
  if glen == flen:
    # gap is full, delete it
    del runs[gapIndex]
  else:
    # gap is now smaller and will come after the file
    runs[gapIndex] = (gid, gpos+flen, glen - flen)

  # insert file before gap
  runs.insert(gapIndex, (fid, gpos, flen))

def moveIfPossible(fileIndex):
    gapIndex = findFirstGapWhichFitsFile(fileIndex)
    if gapIndex < 0:
      return
    moveFileIntoGap(fileIndex, gapIndex)
    # print(diskToString())

def moveFiles():
  fileIndex = len(runs) # for every file starting with the last
  while True:
    fileIndex -= 1
    if fileIndex < 0:
      break

    (fid, _, _) = runs[fileIndex]
    if fid == '.':
      continue

    moveIfPossible(fileIndex)


def calcChecksum():
  checksum = 0
  for i in range(0, len(runs)):
    (id, pos, length) = runs[i]
    if id == '.':
      continue
    for j in range(length): # for each block of the file
      checksum += id * (pos + j)
  return checksum

def main(line):

  readDisk(line)
  moveFiles()
  return calcChecksum()

if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()

    lines = [line.strip() for line in lines]
    print(main(lines[0]))