# f = 'input-example.txt'
# f = 'example-tiny.txt'
f = 'input.txt'

def check(target, values, index):
  if index < 0:
    return False

  if index == 0 and target == values[0]:
    return True

  newTarget = target - values[index]
  if newTarget >= 0:
    if check(newTarget, values, index - 1):
      return True

  if target % values[index] == 0:
    newTarget = target // values[index]
    if check(newTarget, values, index - 1):
      return True

  return False
  
def main(lines):
  total = 0

  for line in lines:
    sp = line.split(': ')
    target = int(sp[0])
    values = [int(x) for x in sp[1].split()]

    if check(target, values, len(values) - 1):
      total += target

  return total
  
if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    print(main(lines))
