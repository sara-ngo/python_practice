# Read file
file = 'lab9_input.txt'
list = []
count = 0
    
with open(file) as f:
    for name in f.readlines():
        count += 1
        list.append(name.strip())

# get min and max length of name in names[]
min_length = len(min(list, key=len))
max_length = len(max(list, key=len))

# promps the users length of a name
def get_length(min_length, max_length):
    while 1:
        input_length = int(input("What name length would you like? "))

        if input_length < min_length or input_length > max_length:
            print("Length must be between {} and {}".format(min_length, max_length))
            print()      
        else:
            return input_length


def print_names(length):
    # printing the names
    print("Name(s) with length {}".format(length))
    found = False
    for name in list:
        if len(name) == length:
            print(name)
            found = True
    if not found:
        print("None")
    print()



def add_name(file, list, min_length, max_length):
    name = input('Enter a name with length between {} and {}: '.format(min_length, max_length))
    print()
    with open(file, 'a') as f: # looping in append mode
        f.write(name.strip() + "\n")
        list.append(name)
        


def main():
    print("There are {} names in the class list".format(count))
    print()
    print('The shortest name has {} characters'.format(min_length))
    print()
    print('The longest name has {} characters'.format(max_length))
    print()

    add_name(file, list, min_length, max_length)

    while 1:
        length = get_length(min_length, max_length)
        print_names(length)
        cont = input("Continue? y/n: ").lower()
        if cont != 'y':
            break
main()
