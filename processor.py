__author__ = 'Tomasz Warkocki'

import itertools

S_C = 0.9

def similarity(sequence, query):
    sequence_len = len(sequence)
    query_len = len(query)
    delta = sequence_len - query_len

    hamming_distances = []
    for x in xrange(delta + 1):
        distance = hamming_distance(query, sequence[x:x+query_len])
        hamming_distances.append(distance)
        if x%100 == 0:
            print str(x) + "/" + str(delta + 1)

    return float(query_len - min(hamming_distances))/query_len

def hamming_distance(str1, str2):
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
            similarity_score = similarity(cluster_seq, seq)
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
