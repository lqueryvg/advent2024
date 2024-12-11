f = 'input.txt'

"""
0 -> 1
even digits -> 2 stones withdigits split, leading zeros removed
else -> *= 2024
"""
cache = {}

def mutate(stone):
  if stone == '0':
    return ['1']

  l = len(stone)
  if l % 2 == 0:
    # chop stone in half
    l2 = l // 2
    left = stone[0:l2]
    right = str(int(stone[l2:])) # remove leading zeros
    return [left, right]

  return [str(int(stone) * 2024)]

def countStones(stone, iterations):
  # check cache
  if (stone, iterations) in cache:
    return cache[(stone, iterations)]

  if iterations == 0:
    return 1
  
  newStones = mutate(stone)
  total = 0
  for newStone in newStones:
    count = countStones(newStone, iterations - 1)
    cache[(newStone, iterations-1)] = count # update cache
    total += count

  return total

def go(stones, iterations):
  total = 0
  for stone in stones:
    total += countStones(stone, iterations)
  return total

def main(iterations=75):
  global f
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    stones = lines[0].split(' ')
    return go(stones, iterations)

if __name__ == '__main__':
  print(main())