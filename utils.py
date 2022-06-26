from Bio import SeqIO
import sys

def read_input(path):
    '''Relative read of fasta file within project'''

    reads = []      
    with path.open() as f:
        for record in SeqIO.parse(f, 'fasta'):
            reads.append(str(record.seq))
    return reads

def splice(read, k):
    '''splice strings into k-mers'''

    if(not type(read) == list):
        print("input must be a list of strings")
        return None

    kmer = []
    for elem in read:
        for i in range(0, len(elem) - (k - 1)):
            kmer.append(elem[i : i + k])
    return kmer