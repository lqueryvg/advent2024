import re
f = 'input.txt'
# f = 'input-example.txt'

lines = []

# width = 11
# height = 7
width = 101
height = 103

robots = []

iterations = 100

def go():
  global lines
  patt = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

  mx = width // 2
  my = height // 2

  print(f"{mx=}, {my=}")
  
  for line in lines:
    # print(f"{line=}")
    matches = re.findall(patt, line)
    m = matches[0]
    (x, y, xi, yi) = map(int, m)

    robots.append((x, y, xi, yi))

  iteration = 1
  while True:
    moveRobots()
    printGrid(iteration)
    iteration += 1

def moveRobots():
  for i in range(0, len(robots)):
    robot = robots[i]
    (x, y, xi, yi) = robot
    nx = (x + xi) % width
    ny = (y + yi) % height
    robots[i] = (nx, ny, xi, yi)

def printGrid(iteration):

  printIt = False
  for y in range(0, height):
    line = ""
    for x in range(0, width):
      for robot in robots:
        if robot[0] == x and robot[1] == y:
          # print("#", end='')
          line += "#"
          break
      else:
        line += "."
    if "#######" in line:
      printIt = True

  if printIt:
    print(f"==={iteration}===")

    for y in range(0, height):
      for x in range(0, width):
        for robot in robots:
          if robot[0] == x and robot[1] == y:
            print("#", end='')
            break
        else:
          print(".", end='')
      print() 
    print("=========================================================")
    print("=========================================================")
    print("=========================================================")
    print("=========================================================")

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    # lines = lines[0].split(' ')

    return go()

if __name__ == '__main__':
  print(main())