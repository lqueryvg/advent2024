f = 'input.txt'
# f = 'input-example.txt'
cache = {}

def possible(design, patterns, l, count): # dfs
  # print(f"{' '*l} {design=} {l=}")

  if design in cache:
    return cache[design]

  if design == '': return 1

  for pattern in patterns:
    if design.startswith(pattern):
      count += possible(design[len(pattern):], patterns, l+1, 0)
  
  cache[design] = count
  return count

def go(patterns, designs):
  count = 0
  for design in designs:
    print(f"TEST {design=}")
    count += possible(design, patterns, 0, 0)
  return count

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    patterns = []
    designs = []
    for line in lines:
      if line == '': continue
      if ',' in line:
        patterns = line.split(", ")
        continue
      designs.append(line)
    return go(patterns, designs)

if __name__ == '__main__':
  print(main())