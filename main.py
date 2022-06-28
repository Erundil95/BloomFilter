from pathlib import Path
from random import randint
import utils
import bloomfilter as bf

k = 20

path = Path(__file__) / "../sample_1.fa"
reads = utils.read_input(path)

bf = bf.BloomFilter(reads, k)


x = randint(0, len(reads))
test = reads[x]

output = open('output.txt', "w")
output.write('K = ' + str(k) + '\n')
output.write('Read (r) randomly chosen from sample_1.fa: ' + '\n')
output.write(test + '\n')
output.write('Result: \n')
output.write(str(bf.checkRead(test)))
output.write('\n\n')

output.write('Read (r) for non-presence test in filter: ' + '\n')
#Given the random choosing of the test string, 
#this case test might rarely return a positive result
test_fail = 'AGT' + test[1:]
output.write(test_fail + '\n')
output.write('Result: \n')
output.write(str(bf.checkRead(test_fail)))

