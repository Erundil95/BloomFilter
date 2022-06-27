from Bio import SeqIO
import math
import mmh3
import utils
from bitarray import bitarray

class BloomFilter(object):

    def __init__(self, input, k):
        '''class contructor
            input : list
                kmer input to insert into bloom filter
            p = 0.5
                false positive probability fixed to 0.5 for semplicity's sake
            n : int
                number of items to insert in the filter
            k : int
                k parameter for k-mers splicing
            num_hashes : int
                number of hash functions to use
            size : int
                size of bit array calcualted from p and n
            bitArray : bitarray
                Hash bit array set to 0 '''

        self.kmer = utils.splice(input, k)
        #removing possible duplicates
        self.kmer = list(dict.fromkeys(self.kmer))

        self.k = k
        self.p = 0.01
        self.n = len(self.kmer)
        self.size = int(-(self.n * math.log(self.p))/(math.log(2)**2))

        self.num_hases = int(self.calculate_hashes(self.size, self.n))
        if(self.num_hases == 0):
            self.num_hases = 1

        self.bitArray = bitarray(self.size)
        self.bitArray.setall(0)

        for item in self.kmer:
            #fill in bloom filter with input kmers
            self.additem(item)



    def calculate_hashes(self, m, n):
        '''calculate optimal number of hases to use based on false positives probability
            and number of total items in the filter'''

        return (m/n) * math.log(2)

    def additem(self, item):
        '''adds an item to the bloom filter'''

        k_range = range(self.num_hases)

        for i in k_range:
            # calculate K different hashes for item,
            # % by size to fit into bitarray
            
            h = mmh3.hash(item, i) % self.size
            self.bitArray[h] = True

    def checkitem(self, item):
        '''checks if an item is present in the bloom filter
            if one hash isn't found in the filter return false'''
        
        for i in range(self.num_hases):
            x = mmh3.hash(item, i) % self.size
            
            if self.bitArray[x] == False:
                return False
        return True

    def checkRead(self, input):
        '''checks if all of the kmers from input read are present
            in the filter, returns False otherwise'''

        if(len(input) < self.k):
            print("Read length cannot be < K")
            return False

        read = []
        read.append(input)

        kmer = utils.splice(read, self.k)
        for item in kmer:
            if (self.checkitem(item) == False):
                return False
        return True




        
        


