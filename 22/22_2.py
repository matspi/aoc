from itertools import islice
from joblib import Parallel, delayed
from joblib_progress import joblib_progress

with open("22/22_input.txt", "r") as f:
  input=[int(l.strip()) for l in f.readlines()]


def mix(s, n):
  return s^n

def prune(s):
  return s%16777216

def step1(s):
  return prune(mix(s, s*64))

def step2(s):
  return prune(mix(s, s//32))

def step3(s):
  return prune(mix(s, s*2048))

def evolve(s):
  return step3(step2(step1(s)))

def get_price(s):
  return s%10

def get_price_series(s):
  prices=[]
  for _ in range(2000):
    prices.append(get_price(s))
    s=evolve(s)

  return prices

def get_change_series(s):
  changes=[]
  for p,n in zip(s, s[1:]):
    changes.append(n-p)
  
  return changes


def get_data(s):
  prices = get_price_series(s)
  changes = get_change_series(prices)

  return prices, changes

def window(s):
  it=iter(s)
  result=tuple(islice(it, 4))
  if len(result)==4:
    yield result
  for i in it:
    result=result[1:] + (i,)
    yield result

def get_sequences(s):
  seqs=set()
  for w in window(s):
    seqs.add((w))

  return seqs

def buy_after_seq(prices, changes, seq):
  lseq=list(seq)
  for i in range(len(changes) - len(seq) + 1):
    if changes[i:i+len(seq)] == lseq:
      return prices[i+len(seq)]
  return 0


def get_seq_with_price(s):
  prices=get_price_series(s)
  changes=get_change_series(prices)#
  seqs_with_price={}
  for seq in get_sequences(changes):
    if seq not in seqs_with_price:
      seqs_with_price[seq] = 0
    seqs_with_price[seq] += buy_after_seq(prices, changes, seq)

  return seqs_with_price

with joblib_progress("Calculating square...", total=len(input)):
  seq_with_prices = Parallel(n_jobs=8)(delayed(get_seq_with_price)(s) for s in input)

all_seqs = {}

for s in seq_with_prices:
  for k,v in s.items():
    if k not in all_seqs:
      all_seqs[k] = v
    else:
      all_seqs[k] += v
  


print(max(all_seqs.values()))