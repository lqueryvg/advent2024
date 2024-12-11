# f = 'input-example.txt'
f = 'input.txt'

stones = []

def go():
  return 1000

def main():
  global f, stones
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    stones = lines[0].split(' ')
    return go()

if __name__ == '__main__':
  print(main())