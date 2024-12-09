# f = 'input-example.txt'
# f = 'input-example-tiny.txt'
f = 'input.txt'

"""
Approach: two pointers
1. Convert line into a list of blocks, the value is either 
2. search gap blocks from the left and file blocks from the right
   moving the file blocks to the gaps until left and right pointers meet
"""

diskBlocks = [] # one element for each block; the value is the file id or '.' for free

def readDisk(line):
  def extend(c, l):
    diskBlocks.extend([c for _ in range(l)])

  isFree = False
  id = 0
  for i in range(0, len(line)):
    l = int(line[i])
    if isFree:
      extend('.', l)
    else:
      extend(id, l)
      id += 1
    isFree = not isFree

def moveBlocks():
  left = 0
  right = len(diskBlocks) - 1
  while True:
    if right <= left:
      break
    if diskBlocks[left] != '.':
      left += 1
      continue
    if diskBlocks[right] == '.':
      right -= 1
      continue

    diskBlocks[left] = diskBlocks[right]
    diskBlocks[right] = '.'
    right -= 1

def calcChecksum():
  checksum = 0
  for i in range(0, len(diskBlocks)):
    id = diskBlocks[i]
    if id == '.':
      break
    checksum += i * id
  return checksum

def main(line):

  readDisk(line)
  moveBlocks()
  return calcChecksum()

if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()

    lines = [line.strip() for line in lines]
    print(main(lines[0]))