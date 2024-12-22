import math
# from typing import  TypeAlias, Literal

f = 'input-example.txt'
f = 'input-tiny.txt'
f = 'input.txt'

# type Point = tuple[int, int]

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

029A
980A
179A
456A
379A

140A
180A
176A
805A
638A
"""
npaths = {
  # A029A
  "A0": ["<"],
  "02": ["^"],
  "29": ["^^>", "^>^", ">^^"],
  "9A": ["vvv"],

  # A980A
  "A9": ["^^^"],
  "98": ["<"],
  "80": ["vvv"],
  "0A": [">"],
  # A179A
  "A1": ["<^<", "^<<"],
  "17": ["^^"],
  "79": [">>"],
  # "9A": [],
  # A456A
  "A4": ["^^<<", "^<<^", "<^<^", "<^^<", "^<^<"],
  "45": [">"],
  "56": [">"],
  "6A": ["vv"],
  # A379A
  "A3": ["^"],
  "37": ["<<^^", "<^^<", "^<^<", "<^<^", "^<<^", "^^<<"],
  #"79": [],
  # "9A": [],
  # A140A
  #"A1": [],
  "14": ["^"],
  "40": ["v>v", ">vv"],
  # "0A": [],
  # A180A
  #"A1": [],
  "18": ["^^>", "^>^", ">^^"],
  # "80": [],
  # "0A": [],
  # A176A
  #"A1": [],
  # "17": [],
  "76": [">>v", ">v>", "v>>"],
  # "6A": [],
  # A805A
  "A8": ["<^^^", "^<^^", "^^<^", "^^^<"],
  # "80": [],
  "05": ["^^"],
  "5A": [">vv", "v>v", "vv>"],
  # A638A
  "A6": ["^^"],
  "63": ["v"],
  "38": ["<^^", "^<^", "^^<"],
  "8A": ["vvv>", "vv>v", "v>vv", ">vvv"],
}
# nCoords: dict[str, Point] = {
#   '7': (0,0),
#   '8': (1,0),
#   '9': (2,0),
#   '4': (0,1),
#   '5': (1,1),
#   '6': (2,1),
#   '1': (0,2),
#   '2': (1,2),
#   '3': (2,2),
#   #' ': (0,3),
#   '0': (1,3),
#   'A': (2,3),
# }

"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
# kCoords: dict[str, Point] = {
#   # ' ': (0,0),
#   '^': (1,0),
#   'A': (2,0),
#   '<': (0,1),
#   'v': (1,1),
#   '>': (2,1),
# }
dpaths = {
  "^^": [""],
  "^A": [">"],
  "^<": ["v<"],
  "^v": ["v"],
  "^>": [">v","v>"],
  "AA": [""],
  "A^": ["<"],
  "A<": ["<v<", "v<<"],
  "Av": ["<v", "v<"],
  "A>": ["v"],
  "<<": [""],
  "<^": [">^"],
  "<A": [">^>", ">>^"],
  "<v": [">"],
  "<>": [">>"],
  "vv": [""],
  "v^": ["^"],
  "vA": ["^>",">^"],
  "v<": ["<"],
  "v>": [">"],
  ">>": [""],
  ">^": ["^<", "<^"],
  ">A": ["^"],
  "><": ["<<"],
  ">v": ["<"],
}

def ncombinations(s: str) -> list[str]:
  if len(s) == 1:
    return [""]

  ret = []
  paths = npaths[s[0] + s[1]]
  for path in paths:
    rest = ncombinations(s[1:])
    for r in rest:
      ret.append(path + "A" + r)
  return ret

def dcombinations(s: str) -> list[str]:
  if len(s) == 1:
    return [""]

  ret = []
  paths = dpaths[s[0] + s[1]]
  for path in paths:
    rest = dcombinations(s[1:])
    for r in rest:
      ret.append(path + "A" + r)
  return ret

def go(lines):
  print(f"{lines=}")
  cost = 0
  for line in lines:
    print(f"{line=}")
    digits = line[:3] # first 3 chars
    minLen = math.inf
    for n in ncombinations("A" + digits + "A"):
      for d in dcombinations("A" + n):
        for d2 in dcombinations("A" + d):
          minLen = min(minLen, len(d2))
          # print(f"{n=}, {d=}, {d2=}")

    t = minLen * int(digits)
    print(f"{line=} {t=}")
    cost += t
    # print(ncombinations("A" + digits + "A"))

  return cost

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    # lines = lines[0].split(' ')
    return go(lines)

if __name__ == '__main__':
  print(main())