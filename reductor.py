__author__ = 'Tomasz Warkocki'

from Bio import SeqIO

with open('/Users/warkocz/nr_reduced', 'a') as file:
    for seq_record in SeqIO.parse('/Users/warkocz/Documents/Big Data/nr', 'fasta'):
        file.write(str(seq_record.seq) + ',' + str(len(str(seq_record.seq))) + '\n')
