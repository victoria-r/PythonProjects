# sliding_window.py

This file contains 2 functions:

1: sliding_window which takes 2 arguments, k (a k-mer size) and a string, and returns a list of all k-mers in the given string, using the sliding window algorithm.

2: gc_content which takes a single string and returns it's GC content (as a fraction between 0 and 1, where 0 represents no G or C bases and 1 represents only G and C bases).

This file also takes in two command line arguments: a k-mer size and a string. On each line, it should then print out a k-mer followed by a tab, followed by the GC content of that k-mer, rounded to two decimal places.

# sliding_window_fatsa.py

This file modifies the script sliding_window.py and uses the same functions but, instead of taking a k-mer size and a string, it takes a k_mer size and a fasta file. It also will run separately fo reach header, printing the header name on one line, and then each k-mer from that fasta entry followed by a tab, followed by the GC content of that k-mer, rounded to two decimal places. Tested with the dengue.fasta file.

## Getting Started

### Dependencies

* Python3
* dengue.fasta - download: wget -O dengue.fasta 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NC_001477.1&rettype=fasta' (Links to an external site.)

## Author

Victoria R. Liebsch

## Date Created

23 January 2022

