__author__ = 'Tomasz Warkocki'

import csv

ALPHABET = set(['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'])

with open('/Users/warkocz/nr_final', 'a') as file:
    with open('/Users/warkocz/nr_sorted', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            seq = row[0]
            not_in_alphabet = set(seq) - ALPHABET
            if len(not_in_alphabet) == 0:
                file.write(row[0] + '\n')
