from collections import Counter

F = 'input-example2.txt'
F = 'input-example1.txt'
F = 'input.txt'

"""
This creates a dot file.
View it at https://edotor.net (or similar).
Then use visual analysis to spot the wires which should be swapped.
(Not too difficult.)
"""

def go(lines) -> int:
  print("digraph {")
  print("  rankdir=LR;")
  print("  subgraph z_nodes {")
  print('    node [style="filled,solid", fillcolor="green"];')
  print("    " + ";".join([f"z{z:02d}" for z in range(46)]))
  print("  }")
  print("  subgraph xor_nodes {")
  print('    node [style="filled,solid", fillcolor="blue"];')
  print("    " + ";".join([f"XOR{z:02d}" for z in range(0, 90)]))
  print("  }")
  print("  subgraph and_nodes {")
  print('    node [style="filled,solid", fillcolor="red"];')
  print("    " + ";".join([f"AND{z:02d}" for z in range(0, 90)]))
  print("  }")
  print('  {rank="same"; ' + "; ".join([f"x{i:02d}; y{i:02d}" for i in range(45)]) + " }")
  print('  {node [style="filled,solid", fillcolor="yellow"]; rank="same"; ' + "; ".join([f"OR{i:02d}" for i in range(45)]) + " }")

  gateCounts = Counter()
  for line in lines:
    if " -> " in line:
      gate, output = line.split(" -> ")
      input1, type, input2 = gate.split(" ")
      global gateNum
      gateName = f"{type}{gateCounts[type]:02d}"
      print(f"{input1} -> {gateName};")
      print(f"{input2} -> {gateName};")
      print(f"{gateName} -> {output};")
      gateCounts[type] += 1

  print("}")
  # print(gateCounts)
  return 999

def main():
  with open(F) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    return go(lines)

if __name__ == '__main__':
  print(main())