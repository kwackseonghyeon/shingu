import sys
sys.argv = list 
class OddMagicSquare:
  def __init__(self, n):
    if 0 == n % 2: n += 1
    
    self.numbers = [0 for i in xrange(n * n)]
    self.n = n
    self.currentIdx = self.getFirstIdx()
    self.currentValue = 0
    
  def getFirstIdx(self):
    return self.n / 2 * self.n + self.n - 1
    
  def hasNext(self):
    if((self.n * self.n) == self.currentValue): return False
    return True

  def next(self):
    if(self.currentIdx == self.n - 1):
      self.currentIdx -= 1
    else:
      self.currentIdx -= (self.n - 1)

      if(self.currentIdx < 0):
        self.currentIdx += (self.n * self.n)
      elif(self.currentIdx % self.n == 0):
        self.currentIdx -= self.n
    
    
    if(0 != self.numbers[self.currentIdx]):
      self.currentIdx += (self.n - 2)
      
  def mark(self):
    self.currentValue += 1
    self.numbers[self.currentIdx] = self.currentValue
    
  def run(self):
    while(self.hasNext()):
      self.mark()
      self.next()
    
  def printTable(self):
    for i in xrange(self.n):
      print '\t'.join([`n` for n in self.numbers[i * self.n : i * self.n + self.n]])

if __name__ == "__main__":
  import sys
  
m = OddMagicSquare(int(sys.argv[1]))
m.run()
m.printTable()
