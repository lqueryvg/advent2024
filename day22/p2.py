f = 'input-tiny.txt'
f = 'input-example2.txt'
f = 'input.txt'
# ITERATIONS = 10
ITERATIONS = 2000

def evolveSecret(num):
  num = ((num * 64) ^ num) % 16777216
  num = ((num // 32) ^ num) % 16777216
  num = ((num * 2048) ^ num) % 16777216
  return num

def go(secrets):
  sequenceTotals: dict[str, int] = {}
  maxSequenceTotal = 0

  for isecret in secrets:
    buyerSequences: set[str] = set()
    secret = isecret
    price = secret % 10
    previousPrice = price
    deltas = []
    for _i in range(0, ITERATIONS):
      secret = evolveSecret(secret)
      price = secret % 10
      delta = price - previousPrice
      deltas.append(delta)
      if len(deltas) < 4: continue

      sequenceString = ",".join(map(str,deltas[-4:]))
      if sequenceString in buyerSequences:
        continue

      buyerSequences.add(sequenceString)

      newSequencePrice = sequenceTotals.get(sequenceString, 0) + price
      sequenceTotals[sequenceString] = newSequencePrice
      maxSequenceTotal = max(newSequencePrice, maxSequenceTotal)
  
  return maxSequenceTotal

def main():
  global f, lines
  with open(f) as f:
    lines = f.readlines()
    secrets = [int(line.strip()) for line in lines]
    return go(secrets)

if __name__ == '__main__':
  print(main())