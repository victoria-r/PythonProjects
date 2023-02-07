#!/usr/bin/env python3.9
# chr21_gene_names.py

"""
This program asks the user to enetr a gene symbol and it prints the
description for that gene based on data from the chr21_gene.txt file.
An error message will show if the symbol is not found in the table.
This program will ask the user for genes until "quit" is given.
"""

import argparse
from assignment4 import my_io


def main():
    """Main Program"""
    args = get_cli_args()
    infile = args.infile
    fh_in = my_io.get_fh(infile, "r")
    desc_output = get_description_using_dict(fh_in)
    user_input(desc_output)


def get_description_using_dict(fh_in):
    """
    Takes 1 argument: a filehandle to chr21_genes.txt
    Stores the categores and descriptions of genes in a dictionary
    """
    desc_output = {}
    lines = fh_in.readlines()[1:]
    for line in lines:
        gene = line.strip().split('\t')[0].lower()
        description = line.strip().split('\t')[1].lower()
        desc_output[gene] = description
    return desc_output


def user_input(desc_output):
    """
    Takes 1 argument: Dictionary of categories and descriptions of genes
    Asks user for a gene name and prompts to use "quit" to exit
    """
    while True:
        gene = input("Enter gene name of interest. Type quit to exit:").lower()
        if gene in desc_output:
            print(f"{gene} found! Here is the description: ")
            print(f"{desc_output[gene]}")
        elif gene == 'quit':
            print("Thanks for querying the data.")
            break
        else:
            print("Not a valid gene name.")


def get_cli_args():
    """
    Get the command line arguments using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(
        description='Open chr21_genes.txt and ask user for a gene name')
    parser.add_argument('-i', '--infile', dest='infile', type=str,
                        help='Path to the file to open', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
