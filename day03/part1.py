import re

# f = 'day03/input-example1.txt'
f = 'day03/input.txt'


def main(lines):
  total = 0
  for line in lines:
    print(f"{line=}")

    m = re.findall(r"mul\((\d{,3}),(\d{,3})\)", line)
    print(f"{m=}")
    for match in m:
      total += int(match[0]) * int(match[1])
 
  print(total)

with open(f) as f:
  lines = f.readlines()
  lines = [line.strip() for line in lines]
  main(lines)