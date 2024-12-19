f = 'input.txt'
# f = 'input-example.txt'

def possible(design, patterns): # dfs
  if design == '': return True
  for pattern in patterns:
    if design.startswith(pattern):
      if possible(design[len(pattern):], patterns):
        return True
  
  return False

def go(patterns, designs):
  count = 0
  for design in designs:
    if possible(design, patterns):
      count += 1

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