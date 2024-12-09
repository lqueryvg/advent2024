# f = 'input-example.txt'
# f = 'input-example-tiny.txt'
f = 'input.txt'

disk = [] # one element for each block; the value is the file id or '.' for free

def readDisk(line):
  def extend(c, l):
    disk.extend([c for _x in range(l)])

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
  right = len(disk) - 1
  while True:
    if right <= left:
      break
    if disk[left] != '.':
      left += 1
      continue
    if disk[right] == '.':
      right -= 1
      continue

    disk[left] = disk[right]
    disk[right] = '.'
    right -= 1

def calcChecksum():
  checksum = 0
  for i in range(0, len(disk)):
    id = disk[i]
    if id == '.':
      break
    checksum += i * id
  return checksum

def main(line):

  global disk
  readDisk(line)
  moveBlocks()
  return calcChecksum()

if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()

    lines = [line.strip() for line in lines]
    print(main(lines[0]))