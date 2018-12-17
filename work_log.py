import csv


def get_user_choice():
    return input('Your choice: ')


def print_menu():
    print('Choose an option from the menu')
    print('1 --> Do something')
    print('2 --> Do something else')
    print('Q --> Quit the program')


def init():
    waiting_for_input = True
    while waiting_for_input:
        print_menu()
        user_choice = get_user_choice()
        if user_choice == '1':
            print('doing something')
        elif user_choice == '2':
            print('doing something else')
        elif user_choice.upper() == 'Q':
            waiting_for_input = False
        else:
            print('Option not recognized, please try again.')

    print('User has ended the program.')


if __name__ == '__main__':
    init()
