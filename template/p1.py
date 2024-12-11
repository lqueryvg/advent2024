f = 'input.txt'


def go(count):
  pass
  return 999

def main(count=25):
  global f, stones
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    stones = lines[0].split(' ')
    return go(count)

if __name__ == '__main__':
  print(main())