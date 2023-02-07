# my_io.py

This is a Python Module that will call the function get_fh as a file handle for reading and writing files. This can be implemented by calling my_io.get_fh in the program. This program runs as an imported custom python module that takes care of file handling for the program that it is used in. 

# __init__.py

This is a blank python program for directory structure usage. This is a blank program that will allow for this specific directory structure: <br />

assignment5 <br />
├── assignment5 <br />
│   ├── __init__.py <br />
│   ├── config.py <br />
│   └── my_io.py <br />
├── gene_information_query.py <br />
└── tests <br />
    ├── __init__.py <br />
    └── unit <br />
        ├── __init__.py <br />
        ├── test_config.py <br />
        └── test_my_io.py <br />

# config.py

This program holds the absolute path to the Unigene data and returns the value, which makes it easier to change the variable for use in functions. The program will also return a dictionary of hosts that will be used for mapping. 

# gene_infromation_query.py

This program takes a user inputted host (species) and gene name, then return the tissue expression for the given species and gene.  

## Getting Started

### Dependencies

* Python3.9
* IDE - such as Pycharm
* data from Unigene database 

### Information on Unigene data

The data contains information from six different types of mammals. This data will be used to find a way to query the tissue expression for a given gene and species, "on demand". 

## Author 

Victoria R. Liebsch

## Date Created - All programs

27 November 2021
    
