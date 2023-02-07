#!/usr/bin/env python3.9

# headers_to_file.py

# Use regular expressions = import re
import re

# Set the file path and open to the Drosophila genome
dmel_genome_path = open('/home/victoria/dmel-all-chromosome-r6.17.fasta')

# The name of the file that will be written
filename = "dmel_headers.txt" 

# Initialize a header counter
header_count = 0  

# Open the file, pass the 'w' parameter
with open(filename, 'w') as out:
    for line in dmel_genome_path:
        # Check to see if the line is a header line (starts with >)
        if re.match('^>', line):
            # Set headers equal to line if the line starts with >
            header = line
            # Increment the header count by one
            header_count += 1
            # If the line count is less than 51
            if header_count < 51:
                # Write headers to file
                out.write(header)

# Print to know that fasta file is being read
print("Reading Drosophila genome...")

# Close fasta file
dmel_genome_path.close()

