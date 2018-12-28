"""
    Main file for the application
"""
import datetime
import os
from collections import OrderedDict

# import classes
from log_util import LogUtil
from search_util import SearchUtil

MAIN_MENU = OrderedDict([
    ('a', 'Add new entry'),
    ('b', 'Search existing entries'),
    ('c', 'Quit the program')
])

SEARCH_MENU = OrderedDict([
    ('a', 'Exact Date'),
    ('b', 'Time spent (in minutes)'),
    ('c', 'Exact Search (will search title and notes)'),
    ('d', 'Regex Pattern'),
    ('e', 'Return to main menu')
])

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


class WorkLog:
    """ Provides the interface needed for a user to interact with the application """
    def __init__(self):
        self.tasks = LogUtil.load_tasks()
        self.prompt_user()

    def search_menu(self):
        clear_terminal()
        while True:
            print('Do you want to search by:')
            for key, value in SEARCH_MENU.items():
                print('{}) {}'.format(key, value))
            user_choice = self.get_user_input('Your choice: ').lower().strip()
            if user_choice == 'a':
                date = self.get_date_input()
                SearchUtil.search_tasks(
                    date, self.tasks, SearchUtil.search_exact_date)
            elif user_choice == 'b':
                time = self.get_user_input('Time in minutes: ')
                SearchUtil.search_tasks(
                    time, self.tasks, SearchUtil.search_by_minutes)
            elif user_choice == 'c':
                user_query = self.get_user_input('Enter your search query: ')
                SearchUtil.search_tasks(
                    user_query, self.tasks, SearchUtil.exact_search)
            elif user_choice == 'd':
                pattern = self.get_user_input('Enter your regex pattern: ')
                SearchUtil.search_tasks(pattern, self.tasks, SearchUtil.regex_search)
            elif user_choice == 'e':
                break
            else:
                print('Option not recognized, please try again')

    def gather_task_data(self):
        task_date = self.get_date_input()
        task_title = self.get_user_input('Task title: ')
        task_time = self.get_time_input()
        task_notes = self.get_user_input(
            'Notes (Optional, you can leave this empty): ')
        task = {
            'date': task_date,
            'title': task_title,
            'time': task_time,
            'notes': task_notes
        }
        # if task is saved successfully add it to the tasks list and notify user
        LogUtil.save_to_log(task)
        self.tasks.append(OrderedDict(
            [('date', task_date), ('title', task_title), ('time', task_time), ('notes', task_notes)]))
        input('The entry has been added! Press enter to return to the menu ')


    def get_time_input(self):
        waiting_for_valid_time = True
        while waiting_for_valid_time:
            minutes = self.get_user_input('Time spent (rounded in minutes): ').strip()
            try:
                time = int(minutes)
                waiting_for_valid_time = False
                return time
            except ValueError:
                input('Please enter numbers only! Press enter to try again ')


    def get_date_input(self):
        waiting_for_valid_date = True
        while waiting_for_valid_date:
            print('Date of the task')
            date_input = input('Please use DD/MM/YYYY: ').strip()
            date_list = [int(date) for date in date_input.split('/')]
            try:
                task_date = datetime.date(
                    date_list[2], date_list[1], date_list[0])
                waiting_for_valid_date = False
                return date_input
            except (ValueError, IndexError):
                print('Error: {} doesn\'t seem to be a valid date'.format(date_input))
                input('Press enter to try again ')

    def get_user_input(self, message):
        return input(message)

    def print_menu(self):
        print('='*15)
        print('WORK LOG')
        print('='*15)
        print('What would you like to do?')
        for key, value in MAIN_MENU.items():
            print('{}) {}'.format(key, value))

    def prompt_user(self):
        LogUtil.check_for_log()
        while True:
            self.print_menu()
            user_choice = self.get_user_input('Your choice: ').lower().strip()
            if user_choice == 'a':
                self.gather_task_data()
            elif user_choice == 'b':
                self.search_menu()
            elif user_choice == 'c':
                break
            else:
                print('Option not recognized, please try again.')

        print('User has ended the program.')


if __name__ == '__main__':
    log = WorkLog()
