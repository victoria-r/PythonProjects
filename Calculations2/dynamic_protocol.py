"""Program that calculates the volumes needed for solution given user inputted values"""

# Get the final volume for the solution
FINAL_VOL = input('Please enter the final volume of the solution (mL): ')

# Get the NaCl concentrations
NACL_STOCK = input('Please enter the NaCl stock (mM): ')
NACL_FINAL = input('Please enter the NaCl final (mM): ')

# Get the MgCl2 concentrations
MGCL2_STOCK = input('Please enter the MgCl2 stock (mM): ')
MGCL2_FINAL = input('Please enter the MgCl2 final (mM): ')

# Calculate the volume needed to make the solution
NACL = (float(NACL_FINAL) * float(FINAL_VOL)) / (float(NACL_STOCK))
MGCL2 = (float(MGCL2_FINAL) * float(FINAL_VOL)) / (float(MGCL2_STOCK))

# Print the volumes needed for the solution
print('Add', NACL, 'ml NaCl')
print('Add', MGCL2, 'mL MgCl2')
print('Add water to a final volume of', float(FINAL_VOL), 'mL and mix')
