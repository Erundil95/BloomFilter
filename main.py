from pathlib import Path
import utils
import bloomfilter as bf

k = 25

path = Path(__file__) / "../sample_1.fa"
reads = utils.read_input(path)

bf = bf.BloomFilter(reads, k)


test = reads[150]
print(test)

print(bf.checkRead(test))