# f = 'input-example.txt'
# f = 'example-tiny.txt'
f = 'input.txt'

def check(target, values, index):
  # indent = " " * ((len(values) - index) * 2)
  # print(f"{indent} {target=}, {values=}, {index=}, {op=}")
  if index < 0:
    # print(f"{indent} NOT found")
    return False

  # print(f"{indent} try +")
  newTarget = target - values[index]
  if newTarget == 0 and index == 0: return True
  if check(newTarget, values, index - 1):
    # print(f"{indent} found + {target=}, {values=}, {index=}")
    return True

  # print(f"{indent} try *")
  newTarget = target / values[index]
  if newTarget == 1 and index == 0: return True
  if check(newTarget, values, index - 1):
    # print(f"{indent} found * {target=}, {values=}, {index=}")
    return True
  
  # print(f"{indent} not found")
  return False
  
def main(lines):
  total = 0

  for line in lines:
    sp = line.split(': ')
    target = int(sp[0])
    values = [int(x) for x in sp[1].split()]
    # print(f"{line=}, {sp=} {target=}, {values=}")

    if check(target, values, len(values) - 1):
      total += target

  return total
  
if __name__ == '__main__':
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    print(main(lines))
