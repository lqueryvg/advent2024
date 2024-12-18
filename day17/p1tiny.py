import sys

def run1(a):
  b = a % 8
  b = b ^ 1
  c = a >> b
  b = b ^ 0b0101
  b = b ^ c
  b = b % 8
  return b

def main(a):
  out = []
  while a > 0:
    out.append(run1(a))
    a = a >> 3
  return ",".join([str(x) for x in out])

if __name__ == '__main__':
  print(main(int(sys.argv[1])))
