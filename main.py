from pathlib import Path
import utils
import bloomfilter as bf

k = 25

path = Path(__file__) / "../sample_1.fa"
reads = utils.read_input(path)

bf = bf.BloomFilter(reads, k)

#Add random picker of r to search for
#Add output onto text file with K parameter (idk which one she means tho)
#Just put both and a bunch of other stuff as well ez
test = reads[150]
print(test)

print(bf.checkRead(test))