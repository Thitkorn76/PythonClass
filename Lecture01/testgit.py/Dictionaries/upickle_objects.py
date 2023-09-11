import pickle

def main():
    end_of_file = False

    inptu_file = open('info.data', 'rb')

    while not end_of_file:
        try:

            person = pickle.load(inptu_file)

            display_data([person])

        except EOFError:


            end_of_file = True

    inptu_file.close()


def display_data(person):
    print('Name:', person['name'])
    print('Age:', person['age'])
    print('Weight:', person['weight'])
    print()

main()


