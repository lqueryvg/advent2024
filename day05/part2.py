# f = 'input-example2.txt'
# f = 'input-example.txt'
f = 'input.txt'

def getMiddleIfBad(line, rules):
  swapsNeeded = False
  for i in range(0, len(line)):
    for j in range(i + 1, len(line)):
      l = line[i]
      r = line[j]
      if f"{r}|{l}" in rules:
        swapsNeeded = True
        line[i] = r
        line[j] = l
  
  return line[len(line) // 2] if swapsNeeded else 0

def main(rules, lines):
  total = 0
  for line in lines:
    total += getMiddleIfBad(line, rules)
  return total

if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    rules = set()
    numbers = []
    for line in lines:
      if '|' in line:
        rules.add(line)

      elif ',' in line:
        numbers.append([int(x) for x in line.strip().split(',')])

    print(main(rules, numbers))
