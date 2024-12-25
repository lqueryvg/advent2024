F = 'input-example2.txt'
F = 'input-example1.txt'
F = 'input.txt'

def resolve(wireName: str, wireValues):
  wireValue = wireValues[wireName]
  if isinstance(wireValue, int):
    return wireValue
  
  gateName = wireValue
  gateOutput = getGateOutput(gateName, wireValues)
  wireValues[wireName] = gateOutput
  return gateOutput


def getGateOutput(gate, wireValues) -> int:
  input1, type, input2 = gate.split(" ")

  input1 = resolve(input1, wireValues)
  input2 = resolve(input2, wireValues)
  if type == "AND":
    return input1 & input2
  elif type == "OR":
    return input1 | input2
  elif type == "XOR":
    return input1 ^ input2
  
  raise Exception(f"Unknown gate type {type}")

def go(lines) -> int:
  wireValues = {}
  maxZNum = 0
  for line in lines:
    if ": " in line:
      wire, value = line.split(": ")
      wireValues[wire] = int(value)
    elif " -> " in line:
      gate, output = line.split(" -> ")
      wireValues[output] = gate
      if output.startswith("z"):
        maxZNum = max(maxZNum, int(output[1:]))
          
  binaryString = ""
  for digitPosition in range(maxZNum + 1):
    zWireName = f"z{digitPosition:02d}"
    digit = resolve(zWireName, wireValues)
    binaryString = f"{digit}{binaryString}"

  print(f"{binaryString=}")
  return int(binaryString, 2)

def main():
  with open(F) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    return go(lines)

if __name__ == '__main__':
  print(main())