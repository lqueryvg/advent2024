def run1(a): # 1 iteration, no shifting of A
  b = a % 8
  b = b ^ 1
  c = a >> b
  b = b ^ 0b0101
  b = b ^ c
  b = b % 8
  return b

"""
A is processed by the tiny program in 3 bit chunks from right to left (lowest bit first)
to produce the program output. But each output digit could be affected by 3 bits which
are up to 7 bits to the left of it (7 because a copy of A is shifted by the number
of bits stored in the lowest 3 bits of B which could be up to 7).
Therefore we have to reconstruct the program in reverse.
"""
def dfs(a, program, pi):
  if pi >= len(program):
    return a
  a = a << 3
  # try all possible 3 bit values to see which will give the next expected program digit
  # for each that does, recurse to the next expected digit trying to find the solution
  for i in range(0,8):
    if run1(a+i) == program[pi]:
      r = dfs((a+i), program, pi + 1)
      if r is not None:
        # solution found !
        return r
      # else try the next value

  # something went wrong and there is no solution !
  return None

def main():
  program = [int(x) for x in reversed("2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0".split(","))]
  return dfs(0, program, 0)

if __name__ == '__main__':
  print(main())