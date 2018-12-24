"""
    Main file for the application
"""
import datetime
import os
from collections import OrderedDict

# import classes
from log_util import LogUtil
from search_util import SearchUtil


class WorkLog:
    def __init__(self):
        self.tasks = LogUtil.load_tasks()
        self.prompt_user()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def search_menu(self):
        self.clear_screen()
        waiting_for_input = True
        while waiting_for_input:
            print('Do you want to search by:')
            print('a) Exact Date')
            print('b) Time spent(in minutes)')
            print('c) Exact Search (will search title and notes)')
            print('d) Range of dates')
            print('e) Regex Pattern')
            print('f) Return to main menu')
            user_choice = self.get_user_input('Your choice: ')
            if user_choice.lower() == 'a':
                date = self.get_date_input()
                SearchUtil.search_tasks(
                    date, self.tasks, SearchUtil.search_exact_date)
            elif user_choice.lower() == 'b':
                time = self.get_user_input('Time in minutes: ')
                SearchUtil.search_tasks(
                    time, self.tasks, SearchUtil.search_by_minutes)
            elif user_choice.lower() == 'c':
                user_query = self.get_user_input('Enter your search query: ')
                SearchUtil.search_tasks(
                    user_query, self.tasks, SearchUtil.exact_search)
            elif user_choice.lower() == 'd':
                print('you chose d')
            elif user_choice.lower() == 'e':
                pattern = self.get_user_input('Enter your regex pattern: ')
                SearchUtil.search_tasks(pattern, self.tasks, SearchUtil.regex_search)
            elif user_choice.lower() == 'f':
                waiting_for_input = False
            else:
                print('Command not recognized, please try again')

    def gather_task_data(self):
        task_date = self.get_date_input()
        task_title = get_user_input('Title of the task: ')
        task_time = get_user_input('Time spent (rounded in minutes): ')
        task_notes = get_user_input(
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
        input('The entry has been added. Press enter to return to the menu ')

    def get_date_input(self):
        waiting_for_valid_date = True
        while waiting_for_valid_date:
            print('Date of the task')
            date_input = input('Please use DD/MM/YYYY: ')
            date_list = [int(date) for date in date_input.split('/')]
            try:
                task_date = datetime.date(
                    date_list[2], date_list[1], date_list[0])
                waiting_for_valid_date = False
                return date_input
            except ValueError:
                print('Error: {} doesn\'t seem to be a valid date'.format(date_input))
                input('Press enter to try again ')

    def get_user_input(self, message):
        return input(message)

    def print_menu(self):
        print('WORK LOG')
        print('What would you like to do?')
        print('a) Add new entry')
        print('b) Search existing entries')
        print('c) Quit the program')

    def prompt_user(self):
        LogUtil.check_for_log()
        waiting_for_input = True
        while waiting_for_input:
            self.print_menu()
            user_choice = self.get_user_input('Your choice: ')
            if user_choice.lower() == 'a':
                self.gather_task_data()
            elif user_choice.lower() == 'b':
                self.search_menu()
            elif user_choice.lower() == 'c':
                waiting_for_input = False
            else:
                print('Option not recognized, please try again.')

        print('User has ended the program.')


if __name__ == '__main__':
    log = WorkLog()
