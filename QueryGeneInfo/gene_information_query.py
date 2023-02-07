#!/usr/bin/env python3
# gene_information_query.py

"""Query the tissue expression for a given host (species) and gene name"""


import argparse
import re
import sys
from assignment5 import my_io
from assignment5 import config


def main():
    """Main Program"""
    args = get_cli_args()
    host_name = args.HOST
    gene_name = args.GENE
    if host_name is None:
        cli_host_name = "Homo_sapiens"
        cli_gene_name = "TGM1"
    else:
        cli_host_name = modify_host_name(host_name)
        cli_gene_name = gene_name
    gene_file_name = "/".join((config.get_unigene_directory(), cli_host_name,
                               cli_gene_name + "." +
                               config.get_unigene_extension()))
    tissue_list = get_gene_data(gene_file_name)
    print_output(cli_host_name, cli_gene_name, tissue_list)


def modify_host_name(host_name):
    """
    Takes 1 argument: a host (species) name
    Checks for the available conversions from common to scientific names
    Returns the scientific name
    Calls get_host_keywords to get mapped terms from assignment5.config.py
    If host inputted does not exist, calls _print_host_directories and exits
    """
    if host_name is None:
        host_name = "Homo_sapiens"
    else:
        host_name = host_name.lower()
    host_keywords = config.get_host_keywords()
    if host_name not in host_keywords.keys():
        _print_host_directories()
        sys.exit()
    else:
        return host_keywords.get(host_name)


def _print_host_directories():
    """
    Takes no arguments
    Helper function
    If user inputs a directory that does not exist, the function prints out
    the host directories that do exist
    Uses get_host_keywords to get the hosts (species) that do exist
    """
    host_keywords = config.get_host_keywords()
    scientific_name = host_keywords.values()
    common_name = host_keywords.keys()
    print('\nEither the Host Name you are searching for is not '
          'in the database')
    print('\nor If you are trying to use the scientific name please put '
          'the name in double quotes:\n')
    print('"Scientific name"\n')
    print('Here is a (non-case sensitive) list of available Hosts '
          'by scientific name:\n')
    scientific_name_list = tuple(enumerate(set(scientific_name), 1))
    for index, name in scientific_name_list:
        print("{:>2}.{}".format(index, name.capitalize()))
    print('\nHere is a (non-case sensitive) list of available Hosts '
          'by common name:\n')
    common_name_list = tuple(enumerate(set(common_name), 1))
    for index, name in common_name_list:
        print("{:>2}.{}".format(index, name.capitalize()))


def get_gene_data(gene_file_name):
    """
    Takes 1 argument: a gene file name
    Opens a file for the host (species) and gene, extracts the list of
    tissues in which the gene is expressed
    Returns a sorted list of the tissues
    """
    args = get_cli_args()
    host_name = args.HOST
    gene_name = args.GENE
    if host_name is None:
        cli_host_name = "Homo_sapiens"
        cli_gene_name = "TGM1"
    else:
        cli_host_name = modify_host_name(host_name)
        cli_gene_name = gene_name
    infile = gene_file_name
    if my_io.is_valid_gene_file_name(infile):
        fh_in = my_io.get_fh(infile, "r")
    else:
        print("Not found")
        print(f"Gene {cli_gene_name} does not exist for {cli_host_name}.")
        print("Exiting now...")
        sys.exit()
    lines = fh_in
    for line in lines:
        find_match = re.search(r'^EXPRESS\s+(\D+)', line)
        if find_match:
            tissue_match = find_match.group(1)
            tissue_match_list = list(tissue_match.split(sep='|'))
            tissue_list = []
            for tissue in tissue_match_list:
                tissue_list.append(tissue.strip())
            return sorted(tissue_list)
    return None


def print_output(cli_host_name, cli_gene_name, tissue_list):
    """
    Takes 3 arguments: host (species) name given at the cli, the gene name
    searched at the cli, and the list of tissues returned from get_gene_data
    Prints out the tissue expression data for the gene
    """
    infile = "/".join((config.get_unigene_directory(), cli_host_name,
                       cli_gene_name + "." +
                       config.get_unigene_extension()))
    gene_check = my_io.is_valid_gene_file_name(infile)
    if gene_check:
        print(f"\nFound Gene {cli_gene_name} for {cli_host_name}\n")
        tissues_count = len(tissue_list)
        print(f"In {cli_host_name}, There are {tissues_count} tissues that "
              f"{cli_gene_name} is expressed in:\n")
        for index, tissue in sorted(enumerate(tissue_list, 1)):
            print(f"{index:>2}.{tissue.capitalize()}")


def get_cli_args():
    """
    Get command line arguments using argparse
    Returns the instance of argparse arguments
    """
    parser = argparse.ArgumentParser(
        description='Give the Host and Gene name')
    parser.add_argument('-host', dest='HOST',
                        help='Name of Host', required=False)
    parser.add_argument('-gene', dest='GENE',
                        help='Name of Gene', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    main()
