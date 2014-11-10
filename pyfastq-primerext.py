#!/usr/bin/python3

from Bio import SeqIO
import numpy
import random 
import argparse
import os
import glob

# pyfastq-primerext release information
__version__ = '0.0.1'
_verdata = 'Oct 2014'
_devflag = True

#########################################################################> MAIN

# Program Header
print('\n=-= pyfastq-primerext =-= v' + __version__ + ' =-= ' +
      _verdata + ' =-= by DLS team =-=')
if(_devflag): 
    print('\n>>> WARNING! THIS IS JUST A DEVELOPMENT SUBRELEASE.' + 
          ' USE IT AT YOUR OWN RISK!')  


# flags

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="name of the input file")
args = parser.parse_args()

# main loop

# list where objects are going to be added
v13 = []
v31 = []
v35 = []
v53 = []
v69 = []
v96 = []


for record in SeqIO.parse(args.input, "fastq"):
	record.format("fastq")
	sequence = record.seq.tostring()
	
	if (sequence.startswith('TCAGAGAGTTTGATCCTGGCTCAG')) or (sequence.startswith('AGAGTTTGATCCTGGCTCAG',4)):
		v13.append(record.format('fastq'))
	elif (sequence.startswith('TCAGATTACCGCGGCTGCTGG')) or (sequence.startswith('ATTACCGCGGCTGCTGG',4)): 
		v31.append(record.format('fastq'))
	elif (sequence.startswith('TCAGCCTACGGGAGGCAGCAG')) or (sequence.startswith('CCTACGGGAGGCAGCAG',4)):
		v35.append(record.format('fastq'))
	elif (sequence.startswith('TCAGCCGTCAATTCATTTAAGT')) or (sequence.startswith('CCGTCAATTCATTTAAGT',4)):
		v53.append(record.format('fastq'))
	elif (sequence.startswith('TCAGAACGCGAAGAACCTTAC')) or (sequence.startswith('AACGCGAAGAACCTTAC',4)):
		v69.append(record.format('fastq'))
	elif (sequence.startswith('TCAGTACGGCTACCTTGTTACGACT')) or (sequence.startswith('TACGGCTACCTTGTTACGACT',4)):
		v96.append(record.format('fastq'))
	else:
		pass

a = open('v13.fastq','wr')
for i in v13:
	a.write(str(i))
b = open('v31.fastq','wr')
for i in v31:
	b.write(str(i))
c = open('v35.fastq','wr')
for i in v35:
	c.write(str(i))
d = open('v53.fastq','wr')
for i in v53:
	d.write(str(i))
e = open('v69.fastq','wr')
for i in v69:
	e.write(str(i))
f = open('v96.fastq','wr')
for i in v96:
	f.write(str(i))




