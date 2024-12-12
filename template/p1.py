f = 'input.txt'

lines = []

def go():
  global lines
  print(f"{lines=}")
  return 999

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = lines[0].split(' ')
    return go()

if __name__ == '__main__':
  print(main())