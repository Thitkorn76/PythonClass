#  This program demostractes two functions that
#  have local variables with the same name.

def main():
# Call the texas fundtion 
    taxas()

# Call the california function
    californai()

# Defintiion of the taxas function. It creates
# a local varible named birds.
def taxas():
    birds = 5000
    print('tecas has', birds, 'birsd.')

# Definition if the california function. It also
# creates a local varible named birds.
def californai():
    birds = 8000
    print('california has', birds, 'birds.')

# Call the main fucntion
main()
    