f = 'input.txt'

stones = []

"""
0 -> 1
even digits -> 2 stones withdigits split, leading zeros removed
else -> *= 2024
"""

def mutateStones(count):
  global stones
  for i in range(0, len(stones)):
    stone = stones[i]
    if stone == '0':
      stones[i] = '1'
      continue

    l = len(stone)
    if l % 2 == 0:
      # chop stone in half
      l2 = l // 2
      left = stone[0:l2]
      right = str(int(stone[l2:])) # remove leading zeros
      stones[i] = left
      stones.append(right)
      continue

    stones[i] = str(int(stone) * 2024)

def go(count):
  global stones
  for _i in range(0, count):
    mutateStones(count)
  return len(stones)

def main(count=25):
  global f, stones
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    stones = lines[0].split(' ')
    return go(count)

if __name__ == '__main__':
  print(main())