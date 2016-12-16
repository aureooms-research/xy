from itertools import chain
from itertools import product
from itertools import combinations

def nonemptysubsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s) + 1))

def minima ( t ) :

  """
      Clarkson's algorithm.
      O(nm) where m is the size of the minima set.

  """

  # O(n^2)
  # return filter(lambda x : not any(map(lambda y : y < x, t)), t)

  m = []
  c = list(t)

  while c :

    x = c[-1]

    if any( map( lambda y : y < x , m ) ):

      c.pop()
      continue

    i = -1

    for j in range(len(c)-1):
      y = c[j]

      if y < x :
        x = y
        i = j

    c[i],c[-1]=c[-1],c[i]
    c.pop()

    m.append(x)

  return m


class Poset (object):

  def __init__(self, elements):
    self.elements = frozenset(elements)

  def __len__(self):
    return len(self.elements)

  def e(self):
    M = {frozenset(): 1}
    for i in range(len(self)):
      N = {}
      for s in M:
        t = self.elements - s
        for p in minima(t):
          x = s | {p}
          if x in N:
            N[x] += M[s]
          else:
            N[x] = M[s]
      M = N

    return next(iter(M.values()))

  def w(self):
    n = len(self)
    M = [{frozenset(): 1}] + [{} for i in range(n)]
    for i in range(n):
      for s in M[i]:
        t = self.elements - s
        for p in nonemptysubsets(minima(t)):
          x = s | frozenset(p)
          j = len(x)
          if x in M[j]:
            M[j][x] += M[i][s]
          else:
            M[j][x] = M[i][s]

    return next(iter(M[n].values()))


class AntichainPoset (Poset):

  class Element (object):
    def __init__(self):
      pass

    def __lt__(self,other):
      return False

  def __init__(self,n):
     super().__init__(AntichainPoset.Element() for i in range(n))

class ChainPoset (Poset):

  class Element (object):
    def __init__(self, i):
      self.i = i

    def __lt__(self,other):
      return self.i < other.i

  def __init__(self,n):
     super().__init__(map(ChainPoset.Element, range(n)))


class SquarePoset (Poset):

  class Element (object):
    def __init__(self, i):
      self.i = i

    def __lt__(self,other):
      x, y = self.i, other.i
      return x[0]<=y[0] and x[1]<=y[1] and x[0]+x[1] < y[0]+y[1]

  def __init__(self,n):
     super().__init__(map(SquarePoset.Element, product(range(n),repeat=2)))

class HalfSquarePoset (Poset):

  class Element (object):
    def __init__(self, i):
      self.i = i

    def __lt__(self,other):
      x, y = self.i, other.i
      return x[0]<=y[0] and x[1]<=y[1] and x[0]+x[1] < y[0]+y[1]

  def __init__(self,n):
     super().__init__(map(HalfSquarePoset.Element, combinations(reversed(range(n+1)),2)))

if __name__ == '__main__' :

  import sys

  count, poset, *_ = sys.argv[1:]

  posets = {
      "square" : SquarePoset ,
      "halfsquare" : HalfSquarePoset ,
      "antichain" : AntichainPoset ,
      "chain" : ChainPoset ,
  }

  MyPoset = posets[poset]

  if count == 'e' :
    for i in range(1,100):
      print(i, MyPoset(i).e())

  if count == 'w' :
    for i in range(1,100):
      print(i, MyPoset(i).w())
