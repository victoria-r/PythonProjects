#!/usr/bin/env python3
# sliding_window.py
import sys


def sliding_window(k, string):
    """
    Take 2 arguments: k_mer size and a string
    Returns a list of all k-mers in the string using the sliding window algorithm
    """
    kmers = []
    end = len(string) - k + 1
    for start in range(0, end):
        kmers.append(string[start:start + k])
    return kmers


def gc_content(dna):
    """
    Takes 1 argument: a single string
    Returns the GC content (as a fraction) of the string
    """
    dna = dna.lower()    # Make the sequence lowercase for consistency
    gc = 0    # Count the number of g's and c's
    for nucleotide in dna: 
        if nucleotide in ['g', 'c']:
            gc += 1
    return gc/len(dna)
    

if __name__ == '__main__':

    # Check to make sure there are at least two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: kmer size and a DNA string")

    # Get parameters from command line options
    k = int(sys.argv[1])
    string = sys.argv[2]
    # Iterate over function to get each kmer GC content seperately 
    for dna in sliding_window(k, string):
        result = gc_content(dna)
       
        # Print kmer and GC content to 2 decimal places
        print("{}\t{:.2f}".format(dna, result))
    
        
