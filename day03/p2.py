import re

#f = 'input-example2.txt'
f = 'input.txt'

def main(lines):
  total = 0
  enabled = True
  for line in lines:

    pattern = r"(mul)\((\d{,3}),(\d{,3})\)|(do)\(\)|(don't)\(\)"

    m = re.findall(pattern, line)
    for match in m:
      if match[4] == 'don\'t':
        enabled = False
        continue
      if match[0] == 'mul' and enabled:
        total += int(match[1]) * int(match[2])
        continue
      if match[3] == 'do':
        enabled = True
 
  return total


if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(main(lines))
