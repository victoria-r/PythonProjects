#!/usr/bin/env python3.9
# intersection.py

"""
This program finds all gene symbols that appear both in the chr21_genes.txt
file and in the HUGO_genes.txt file.
These gene symbols are printed to an output file, intersection_output.txt, in
alphabetical order.
This will also print on the terminal how many common gene symbols were found.
"""

import argparse
from assignment4 import my_io


def main():
    """Main Program"""
    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    fh_in = my_io.get_fh(infile1, "r")
    fh_in2 = my_io.get_fh(infile2, "r")
    fh_out = my_io.get_fh("OUTPUT/intersection_output.txt", "w")
    list_genes, list_genes2 = gene_lists(fh_in, fh_in2)
    unique_names, unique_names2 = find_unique_names(list_genes, list_genes2)
    common_names = find_common_names(unique_names, unique_names2, fh_out)
    print_results(infile1, infile2, unique_names, unique_names2, common_names)


def gene_lists(fh_in, fh_in2):
    """
    Takes 2 arguments: filehandle for chr21_genes.txt and HUGO_genes.txt
    Creates 2 lists of genes from 2 files
    """
    list_genes = []
    list_genes2 = []
    lines = fh_in.readlines()[1:]
    lines2 = fh_in2.readlines()[1:]
    for line in lines:
        gene = line.replace('\n', "").split('\t')[0]
        list_genes.append(gene)
    for line in lines2:
        gene2 = line.replace('\n', "").split('\t')[0]
        list_genes2.append(gene2)
    return list_genes, list_genes2


def find_unique_names(list_genes, list_genes2):
    """
    Takes 2 arguments: the lists made from both input files
    Creates unique gene name lists from lists made from input files
    """
    unique_names = list(set(list_genes))
    unique_names2 = list(set(list_genes2))
    return unique_names, unique_names2


def find_common_names(unique_names, unique_names2, fh_out):
    """
    Takes 3 arguments: both unique gene names from both input files
    and a filehandle
    Finds all the common gene symbols between the 2 input files
    """
    intersection = set(unique_names).intersection(set(unique_names2))
    common_names = sorted(list(intersection))
    for element in common_names:
        fh_out.write("%s\n" % element)
    return common_names


def print_results(infile1, infile2, unique_names, unique_names2, common_names):
    """
    Takes 5 arguments: both input files, both unique name list from files,
    intersection list of unique name lists
    Prints results of how many common gene symbols were found
    """
    print(f"\nNumber of unique gene names in {infile1}: {len(unique_names)}\n")
    print(f"Number of unique gene names in {infile2}: {len(unique_names2)}\n")
    print(f"Number of common gene symbols found: {len(common_names)}\n")
    print(f"Output stored in OUTPUT/intersection_output.txt")


def get_cli_args():
    """
    Get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(
        description='Provide two gene list (ignore header), find intersection')
    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, help='Gene list 1 to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, help='Gene list 2 to open', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
