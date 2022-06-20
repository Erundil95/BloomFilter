from Bio import SeqIO
import math
from bitarray import bitarray

class BloomFilter(object):

    def __init__(self, input):
        '''class contructor
            
            p = 0.5 -> false positive probability fixed to 0.5 for semplicity's sake
            
            n : int
                number of items to insert in the filter
            k : int
                number of hash functions to use'''

        self.p = 0.5
        self.n = len(input)
        self.size = int(-(self.n * math.log(p))/(math.log(2)**2))
        self.k = self.calculate_k(self.size, self.n)
        self.bitArray = bitarray(self.n)
        self.bitArray.setall(0)


    def calculate_k(self, m, n):
        '''calculate optimal number of hases to use based on false positives probability
            and number of total items in the filter'''

        return (m/n) * math.log(2)

    def additem(self, item):
        '''adds an item to the bloom filter'''

        k_range = range(self.k)
        A = []

        for h in k_range:

    def checkitem(self, item):
        '''checks if an item is present in the bloom filter'''
        

        

