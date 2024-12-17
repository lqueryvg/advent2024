f = 'input.txt'

global a, b, c
global program, output
global ip # instruction pointer

lines = []

def getComboOperand():
  """
  Combo operands 0 through 3 represent literal values 0 through 3.
  Combo operand 4 represents the value of register A.
  Combo operand 5 represents the value of register B.
  Combo operand 6 represents the value of register C.
  Combo operand 7 is reserved and will not appear in valid programs.
  """
  global ip, program
  op = program[ip]
  ip += 1
  # print(f"{op=}")
  if op <= 3:
    return op
  elif op == 4:
    return a
  elif op == 5:
    return b
  elif op == 6:
    return c
  elif op == 7:
    # return 7
    raise Exception("Reserved 7 operand not expected")

  raise Exception("Unexpected operand")

def printState():
  global ip, a, b, c, output
  print("-----")
  print(f"{ip=}, {a=}, {b=}, {c=}")
  print(",".join([str(x) for x in program]))
  print("  "*ip + "^")
  print(f"{output}")

  
def go():
  global ip, a, b, c, output
  ip = 0
  output = []
  # printState()
  while ip < len(program):
    opcode = program[ip]
    ip += 1
    if opcode == 0: # adv
      a = (a // 2**getComboOperand())
    elif opcode == 1: # bxl
      """
      calculates the bitwise XOR of register B and the instruction's literal operand,
      then stores the result in register B.
      """
      b = (b ^ program[ip])
      # b = (b ^ getOperand())
      ip += 1
    elif opcode == 2: # bst
      b = getComboOperand() % 8
    elif opcode == 3: # jnz
      """
      does nothing if the A register is 0. However, if the A register is not zero,
      it jumps by setting the instruction pointer to the value of its literal operand;
      if this instruction jumps,
      the instruction pointer is not increased by 2 after this instruction.
      """
      if a != 0:
        # ip = program[ip]
        ip = getComboOperand()
      else:
        ip += 1
    elif opcode == 4: # bxc
      """
      calculates the bitwise XOR of register B
      and register C, then stores the result in register B.
      (For legacy reasons, this instruction reads an operand but ignores it.)
      """
      b = b ^ c
      ip += 1
    elif opcode == 5: # out
      output.append(str(getComboOperand() % 8))
    elif opcode == 6: # bdv
      """
      works exactly like the adv instruction except that the result is stored in the B register.
      (The numerator is still read from the A register.)
      """
      b = (a // 2**getComboOperand())
    elif opcode == 7: # cdv
      """
      works exactly like the adv instruction except that the result is stored in the C register.
      (The numerator is still read from the A register.)
      """
      c = (a // 2**getComboOperand())
    else:
      raise Exception(f"Unexpected opcode {opcode}")

    # printState()

  # print(f"{output=}")
  return ",".join(output)

def main():
  global f
  global a, b, c, program
  with open(f) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    a = int(lines[0].split()[2])
    b = int(lines[1].split()[2])
    c = int(lines[2].split()[2])
    program = [int(x) for x in lines[4].split()[1].split(',')]

    return go()

if __name__ == '__main__':
  print(main())