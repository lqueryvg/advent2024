from collections import defaultdict

f = 'input-tiny.txt'
f = 'input-example.txt'
f = 'input.txt'
NUM_ROBOTS = 2
NUM_ROBOTS = 25

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
"""
NPadButtonTransitions = {
  # A029A
  "A0": "<",
  "02": "^",
  "29": "^^>",
  "9A": "vvv",
  # A980A
  "A9": "^^^",
  "98": "<",
  "80": "vvv",
  "0A": ">",
  # A179A
  "A1": "^<<",
  "17": "^^",
  "79": ">>",
  "A4": "<^<^",
  "45": ">",
  "56": ">",
  "6A": "vv",
  # A379A
  "A3": "^",
  "37": "<<^^",
  # A140A
  "14": "^",
  "40": ">vv",
  # A180A
  "18": "^^>",
  # A176A
  "76": "v>>",
  # A805A
  "A8": "<^^^",
  "05": "^^",
  "5A": "vv>",
  # A638A
  "A6": "^^",
  "63": "v",
  "38": "<^^",
  "8A": "vvv>",
}

"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
DpadButtonTransitions = {
  "AA": "",
  "A^": "<",
  "A<": "v<<",
  "Av": "<v",
  "A>": "v",
  "^^": "",
  "^A": ">",
  "^<": "v<",
  "^>": "v>",
  "<<": "",
  "<^": ">^",
  "<A": ">>^",
  "<v": ">",
  "vv": "",
  "vA": "^>",
  "v<": "<",
  "v>": ">",
  ">>": "",
  ">^": "<^",
  ">A": "^",
  ">v": "<",
}

def getShortestSequenceLength(code: str) -> float:
  if len(code) == 1:
    return 0

  sequenceCounts = defaultdict(int)
  codePath = ""
  # for each pair of characters in code
  for i in range(len(code) - 1):
    keys = code[i] + code[i+1]
    path = NPadButtonTransitions[keys] + "A"
    sequenceCounts[path] += 1
    codePath += path

  for _robotNumber in range(1, NUM_ROBOTS+1):
    # update sequence_counts
    for sequence, count in list(sequenceCounts.items()):
        sequenceCounts[sequence] -= count
        sequence = "A" + sequence
        for i in range(len(sequence) - 1):
          buttonPair = sequence[i] + sequence[i+1]
          path = DpadButtonTransitions[buttonPair] + "A"
          sequenceCounts[path] += count

  totalButtonPresses = 0
  for sequence, count in sequenceCounts.items():
    totalButtonPresses += count * len(sequence)

  return totalButtonPresses


def go(lines):
  global minLen
  total = 0
  for code in lines:
    numericPart = int(code[:3]) # first three digit chars
    complexity = numericPart * getShortestSequenceLength("A" + code)
    total += complexity
  return total

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    return go(lines)

if __name__ == '__main__':
  print(main())