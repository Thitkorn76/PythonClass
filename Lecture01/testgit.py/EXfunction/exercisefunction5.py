def main():
    value = 99
    print('The value is', value)
    change_me(value)
    print('Back in mian the value is', value)

def change_me(arg):
    print('I am changinf the value.')
    arg = 0
    print('Now the value is', arg)

main()