import re
f = 'input.txt'

lines = []

def is_integer_within_tolerance(number, tolerance=1e-2):
  integer_part = int(round(number))
  difference = abs(number - integer_part)
  return difference <= tolerance

def calculate(tx, ty, ax, ay, bx, by):
  # gradients
  ga = ay / ax
  gb = by / bx

  multiplier = ty - (gb * tx) # common term

  # intersection
  x1 = multiplier / (ga - gb)
  y1 = multiplier / (1 - (ax * by)/(bx * ay))

  if not is_integer_within_tolerance(x1) or \
     not is_integer_within_tolerance(y1):
    return 0

  # B delta
  dbx = tx - x1

  aPushes = x1 / ax 
  bPushes = dbx / bx

  score = (3 * aPushes) + bPushes
  return score

def go():
  global lines
  (ax, ay, bx, by, tx, ty) = (0, 0, 0, 0, 0, 0)
  total = 0
  for line in lines:

    if line.startswith("Button"):
      matches = re.findall(r"Button ([AB]): X\+(\d+), Y\+(\d+)", line)
      m = matches[0]
      button = m[0]
      if button == "A":
        ax, ay = int(m[1]), int(m[2])
        continue

      bx, by = int(m[1]), int(m[2])
      continue

    if line.startswith("Prize"):
      matches = re.findall(r"Prize: X=(\d+), Y=(\d+)", line)
      m = matches[0]
      tx, ty = int(m[0]), int(m[1])

      total += calculate(tx, ty, ax, ay, bx, by)

  return total

def main():
  global f, lines
  print("file is", f)
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    return go()

if __name__ == '__main__':
  print(main())