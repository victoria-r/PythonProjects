# my_ip.py

This is a Python Module that will call the function get_fh as a file handle for reading and writing files. This can be implemented by calling my_io.get_fh in the ptogram. This program runs as an imported custom python module that takes care of file handling for the program that it is used in. 

# __init__.py

This is a blank python program for directory structure usage. This is a blank program that will allow for this specific directory structure: <br />
assignment4 <br />
├── assignment4 <br />
|   |── __init__.py  # Do this at the terminal:  touch assignment4/__init__.py <br />
|   └── my_io.py <br />
├── HUGO_genes.txt <br />
├── OUTPUT # your output will go here (you can manually make this) <br />
│   ├── categories.txt <br />
│   └── intersection_output.txt <br />
├── categories.py <br />
├── chr21_gene_names.py <br />
├── chr21_genes.txt <br />
├── chr21_genes_categories.txt <br />
└── intersection.py <br />
└── tests <br />
    ├── __init__.py <br />
    └── unit <br />
        ├── __init__.py <br />
        └── test_my_io.py  # make sure to write this test, see solution to assignment 3 <br />


# chr21_genes_categories.txt

This file stores the meanings of each category in ch21_genes.txt in tab separated fields. <br />
Ex: <br />
1.1     Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase). <br />
1.2     Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs). <br />

# chr21_gene_names.py

This is a python program that asks the user for a gene symbol and then prints the description for that gene based on data from the chr21_genes.txt file. This program gives an error message if the entered symbol is not found in the table. The program will continue to ask the user for genes until "quit" or "exit" is given. 

# categories.py

This program counts how many genes are in each categories from ch21_genes.txt. Then it prints the results of the counts from each category in ch21_gene.txt arranged in ascending order to an output file (OUTPUT/categories.txt). 

# intersection.py

This program finds the gebe symbols that appear both in the chr21_genes.txt and HUGO_genes.txt file. These gene symbols print in alphabetical order to a file (OUTPUT/intersection_output.txt). This program also prints to the terminal how many common gene symbols were found.

## Getting Started

### Dependencies

* Python3.9
* IDE - such as Pycharm
* Source files - HUGO_genes.txt, chr21_genes.txt

### Information on Source files

chr21_genes.txt <br />

* This file lists genes from the human chromosome 21, in their order along the chromosome, as described in Hattori et al. (Nature 405, 311-319) (Links to an external site.). For each gene, the file gives the gene symbol, description and category. The fields are separated by tabs. You will need to get the the meaning of each category. You can find these meanings in the original paper (Links to an external site.), under the "Gene categories" section.

HUGO_genes.txt <br />

* This file lists all human genes having official symbol approved by the HUGO gene nomenclature committee (Links to an external site.) (some have probably changed by now). For each gene, the file gives its symbol and description, separated by a TAB character.

## Author

Victoria R. Liebsch

## Date Created - All programs

31 October 2021
