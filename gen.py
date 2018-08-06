from random import SystemRandom

def get_word(num_un):
  num = str(num_un)
  with open("eff_short_list") as f:
    for line in f:
      if num == line.split("\t")[0]:
        return line.split("\t")[1][:-1]

  with open("eff_list") as f:
    for line in f:
      if num == line.split("\t")[0]:
        return line.split("\t")[1][:-1]

  return None


def gen_random_num(digits=4):
  cryptogen = SystemRandom()
  num = [1 + cryptogen.randrange(6) for x in range(digits)]
  return int(''.join(map(str, num)))

def main():
  return ' '.join([get_word(gen_random_num()) for x in range(6)])

if __name__ == '__main__':
  print(main())
