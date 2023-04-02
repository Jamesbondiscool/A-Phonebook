import json

def load_phonebook():
    try:
        with open('phonebook.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_phonebook(phonebook):
    with open('phonebook.json', 'w') as f:
        json.dump(phonebook, f)

def add_contact(phonebook):
    name = input('Enter contact name: ')
    number = input('Enter contact number: ')
    phonebook[name] = number
    save_phonebook(phonebook)
    print(f'{name} has been added to the phone book.')

def search_contact(phonebook):
    name = input('Enter contact name to search for: ')
    if name in phonebook:
        print(f'{name}: {phonebook[name]}')
    else:
        print(f'{name} not found in the phone book.')

def edit_contact(phonebook):
    name = input('Enter contact name to edit: ')
    if name in phonebook:
        new_number = input(f'Enter new number for {name}: ')
        phonebook[name] = new_number
        save_phonebook(phonebook)
        print(f'{name}\'s number has been updated.')
    else:
        print(f'{name} not found in the phone book.')

def delete_contact(phonebook):
    name = input('Enter contact name to delete: ')
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
        print(f'{name} has been deleted from the phone book.')
    else:
        print(f'{name} not found in the phone book.')

def display_phonebook(phonebook):
    print('Phone Book:')
    for name, number in phonebook.items():
        print(f'{name}: {number}')

def main():
    phonebook = load_phonebook()

    while True:
        print('\nWelcome to the Phone Book App!')
        print('1. Add Contact')
        print('2. Search Contact')
        print('3. Edit Contact')
        print('4. Delete Contact')
        print('5. Display Phone Book')
        print('6. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            edit_contact(phonebook)
        elif choice == '4':
            delete_contact(phonebook)
        elif choice == '5':
            display_phonebook(phonebook)
        elif choice == '6':
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()
