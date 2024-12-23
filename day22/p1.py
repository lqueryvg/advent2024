f = 'input-tiny.txt'
f = 'input-example.txt'
f = 'input.txt'
# ITERATIONS = 10
ITERATIONS = 2000
def evolveSecret(num):
  num = ((num * 64) ^ num) % 16777216
  num = ((num // 32) ^ num) % 16777216
  num = ((num * 2048) ^ num) % 16777216
  return num

def go(nums):
  total = 0
  for num in nums:
    new = num
    for i in range(0, ITERATIONS):
      new = evolveSecret(new)
    total += new
  return total

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    nums = [int(line.strip()) for line in lines]
    return go(nums)

if __name__ == '__main__':
  print(main())