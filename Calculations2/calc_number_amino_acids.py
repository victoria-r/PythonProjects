"""Program that calculates the the molecular weight of a user inputted gene"""

# Get the gene name and print it back
GENE_NAME = input('Please enter a name for the DNA sequence: ')
print('Your sequence name is:', GENE_NAME)

# Get the number of nucleotides in the gene coding sequence
NUCLEOTIDES = input('Please enter the length of the sequence: ')


# Calculate if the number of given nucleotides is divisible by 3
if (int(NUCLEOTIDES)) % 3 == 0:

    # Calculate the number of amino acids in the gene coding sequence
    AMINO_ACIDS = (int(NUCLEOTIDES) / 3)

    # Print the number of given nucleotides and calculated amino acid length
    print('The length of the DNA sequence is:', NUCLEOTIDES)
    print('The length of the decoded protein is:', AMINO_ACIDS)

    # Calculate the molecular weight of the amino acids in kilodaltons
    DALTONS = 110
    WEIGHT_GENE = (int(AMINO_ACIDS) * DALTONS)
    KILO_DALTONS = (WEIGHT_GENE / 1000)

    # Print the molecular weight of the amino acids in kilodaltons
    print('The average molecular weight of the protein sequence is:', KILO_DALTONS, 'kilodaltons')


# If the number of given nucleotides in not divisible by 3 print ERROR message
else:
    print('Error: the DNA sequence is not a multiple of 3')
