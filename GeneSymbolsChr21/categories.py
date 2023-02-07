#!/usr/bin/env python3.9
# categories.py

"""
This program counts how many genes are in each category from ch21_genes.txt
The count results will be outputted to categories.txt in ascending order
"""

import argparse
from assignment4 import my_io


def main():
    """ Main Program"""

    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    fh_in = my_io.get_fh(infile1, "r")
    fh_in2 = my_io.get_fh(infile2, "r")
    fh_out = my_io.get_fh("OUTPUT/categories.txt", "w")
    counts = get_occur_using_dict(fh_in)
    discript = get_discript_using_dict(fh_in2)
    print_results_to_file(counts, discript, fh_out)


def get_occur_using_dict(fh_in):
    """
    Takes 1 argument: a file handle to chr21_genes.txt
    Stores the categories in a dictionary and sorts from ascending order
    """
    counts = {}
    lines = fh_in.readlines()[1:]
    for line in lines:
        categories = line.replace('\n', "").split('\t')[2]
        counts[categories] = counts.get(categories, 0) + 1
        sort_dict = sorted(counts.items())
    return dict(sort_dict)


def get_discript_using_dict(fh_in2):
    """
    Takes 1 argument: a file handle to chr21_genes_categories.txt
    Stores the categories in the file into a dictionary
    """
    discript = {}
    lines = fh_in2.readlines()
    for line in lines:
        categories = line.replace('\n', "").split('\t')[0]
        disc_info = line.replace('\n', "").split('\t')[1]
        discript[categories] = disc_info
    return discript


def print_results_to_file(counts, discript, fh_out):
    """
    Takes 3 arguments: the count dict, discript dict, and the output filehandle
    Prints out the results to an output file in ascending order format
    """
    fh_out.write("Category\tOccurrence\tDescription\n")
    for key1, val1 in counts.items():
        for key2, val2 in discript.items():
            if key1 == key2:
                fh_out.write(f"{key1}\t{val1}\t{val2}\n")


def get_cli_args():
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(
        description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1', '--infile1', dest='infile1', type=str,
                        help='Path to the gene description file to open',
                        required=True)
    parser.add_argument('-i2', '--infile2', dest='infile2', type=str,
                        help='Path to the gene category to open',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
