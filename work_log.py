import csv


def search_menu():
    waiting_for_input = True
    while waiting_for_input:
        print('Do you want to search by:')
        print('a) Exact Date')
        print('b) Range of dates')
        print('c) Exact Search')
        print('d) Regex Pattern')
        print('e) Return to menu')

# TODO log the task to a csv
def log_task():
    print('Date of the task')
    task_date = input('Please use DD/MM/YYYY: ')
    task_title = input('Title of the task: ')
    task_time = input('Time spent (rounded in minutes): ')
    task_notes = input('Notes (Optional, you can leave this empty): ')
    task = {
        'date': task_date,
        'title': task_title,
        'time': task_time,
        'notes': task_notes
    }
    print(task)


def get_user_choice():
    return input('Your choice: ')


def print_menu():
    print('WORK LOG')
    print('What would you like to do?')
    print('a) Add new entry')
    print('b) Search existing entries')
    print('c) Quit the program')


def init():
    waiting_for_input = True
    while waiting_for_input:
        print_menu()
        user_choice = get_user_choice()
        if user_choice.lower() == 'a':
            log_task()
        elif user_choice.lower() == 'b':
            search_menu()
        elif user_choice.lower() == 'c':
            waiting_for_input = False
        else:
            print('Option not recognized, please try again.')

    print('User has ended the program.')


if __name__ == '__main__':
    init()
