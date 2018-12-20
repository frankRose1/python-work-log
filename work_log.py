"""
    Main file for the application
"""
import datetime
from collections import OrderedDict

from log_util import LogUtil
from search_utils import search_tasks, search_exact_date, search_by_minutes

class WorkLog:
    def __init__(self):
        self.tasks = LogUtil.load_tasks()
        self.prompt_user()


    def search_menu(self):
        waiting_for_input = True
        while waiting_for_input:
            print('Do you want to search by:')
            print('a) Exact Date')
            print('b) Time spent(in minutes)')
            print('c) Range of dates')
            print('d) Exact Search')
            print('e) Regex Pattern')
            print('f) Return to main menu')
            user_choice = self.get_user_choice()
            if user_choice.lower() == 'a':
                date = self.get_date_input()
                search_tasks(date, self.tasks, search_exact_date)
            elif user_choice.lower() == 'b':
                time = input('Time in minutes: ')
                search_tasks(time, self.tasks, search_by_minutes)
            elif user_choice.lower() == 'c':
                print('you chose c')
            elif user_choice.lower() == 'd':
                print('you chose d')
            elif user_choice.lower() == 'e':
                print('you chose e')
            elif user_choice.lower() == 'f':
                waiting_for_input = False
            else:
                print('Command not recognized, please try again')


    def gather_task_data(self):
        task_date = self.get_date_input()
        task_title = input('Title of the task: ')
        task_time = input('Time spent (rounded in minutes): ')
        task_notes = input('Notes (Optional, you can leave this empty): ')
        task = {
            'date': task_date,
            'title': task_title,
            'time': task_time,
            'notes': task_notes
        }
        # if task is saved successfully add it to the tasks list and notify user
        LogUtil.save_to_log(task)
        self.tasks.append(OrderedDict([('date', task_date), ('title', task_title), ('time', task_time), ('notes', task_notes)]))
        input('The entry has been added. Press enter to return to the menu ')


    def get_date_input(self):
        waiting_for_valid_date = True
        while waiting_for_valid_date:
            print('Date of the task')
            date_input = input('Please use DD/MM/YYYY: ')
            date_list = [int(date) for date in date_input.split('/')]
            try:
                task_date = datetime.date(date_list[2], date_list[1], date_list[0])
                waiting_for_valid_date = False
                return date_input
            except ValueError:
                print('Error: {} doesn\'t seem to be a valid date'.format(date_input))
                input('Press enter to try again ')


    def get_user_choice(self):
        return input('Your choice: ')


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
            user_choice = self.get_user_choice()
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
    print(log.tasks)
