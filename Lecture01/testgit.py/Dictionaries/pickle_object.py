import pickle


def main():
    agian = 'y'

    output_file = open('info.dat', 'wb')

    while agian.lower() == 'y':

        save_data(output_file)

        agian = input('Enter more data? (y/n): ')

    output_file.close()

def save_data(file):

    person = {}

    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['Weight'] = float(input('Weight: '))

    pickle.dump(person, file)

main()
