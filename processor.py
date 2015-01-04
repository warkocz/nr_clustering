__author__ = 'Tomasz Warkocki'

import itertools

S_C = 0.9

def similarity(seq_1, seq_2):
    if len(seq_1) <= len(seq_2):
        shorter_seq = seq_1
        longer_seq = seq_2
    else:
        shorter_seq = seq_2
        longer_seq = seq_1

    shorter_seq_len = len(shorter_seq)
    longer_seq_len = len(longer_seq)
    delta = longer_seq_len - shorter_seq_len

    hamming_distances = []
    for x in xrange(delta + 1):
        distance = hamming1(shorter_seq, longer_seq[x:x+shorter_seq_len])
        hamming_distances.append(distance)
        if x%100 == 0:
            print str(x) + "/" + str(delta + 1)

    return float(shorter_seq_len - min(hamming_distances))/shorter_seq_len

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def hamming1(str1, str2):
  return sum(itertools.imap(str.__ne__, str1, str2))

def append_to_file(index, sequence):
    with open("/Users/warkocz/nr_clusters/nr_" + str(index), 'a') as file:
        file.write(sequence + '\n')


clusters = []

with open('/Users/warkocz/nr_final', 'rb') as file:
    for seq in file:
        seq = seq.strip()
        new_cluster = True
        for cluster_seq in clusters:
            similarity_score = similarity(seq, cluster_seq)
            print "Similarity: " + str(similarity_score)
            if similarity_score > S_C:
                print 'Existing cluster'
                new_cluster = False
                append_to_file(clusters.index(cluster_seq), seq)
                break
        if new_cluster:
            print 'New cluster'
            clusters.append(seq)
            append_to_file(clusters.index(seq), seq)

        print "Clusters count: " + str(len(clusters))
