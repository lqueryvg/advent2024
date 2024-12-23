F = 'input.txt'
F = 'input-example.txt'

def go(lines: list[str]) -> int:
  print(f"{lines=}")
  return 999

def main():
  with open(F) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    return go(lines)

if __name__ == '__main__':
  print(main())