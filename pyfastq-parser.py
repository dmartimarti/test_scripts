#!/usr/bin/python3

from Bio import SeqIO
import random 
import argparse

# pyfastq-parser release information
__version__ = '0.0.1'
_verdata = 'Oct 2014'
_devflag = True

#########################################################################> MAIN

# Program Header
print('\n=-= pyfastq-parser =-= v' + __version__ + ' =-= ' +
      _verdata + ' =-= by DLS team =-=')
if(_devflag): 
    print('\n>>> WARNING! THIS IS JUST A DEVELOPMENT SUBRELEASE.' + 
          ' USE IT AT YOUR OWN RISK!')  


# Flags

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="name of the input file")
parser.add_argument("-s", "--seqs", help="number of seqs per file",
						type = int)
parser.add_argument("-n", "-nout", help="number of output files",
						type = int)
args = parser.parse_args()

# Random selection of sequences in a fastq
original_fastq_list = []

for record in SeqIO.parse(args.input,
					"fastq"):
        record.format("fastq")
        original_fastq_list.append(record.format("fastq"))

output_number = 1

while (output_number - 1) < args.nout:
	my_randoms = random.sample(xrange(230), args.seqs)
	w = open('rand_output_' + str(output_number) + '.fastq', "w")
	for i in my_randoms:
		w.write(str(original_fastq_list[i]))
	output_number = output_number + 1


# TO DO:
# - chose file
# - output also some simple statistical values (average nt count, std, 
#	distribution?)
