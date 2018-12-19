"""
  Contains helper functions to search through the log.csv contents
"""
from log_utils import read_log


def print_task(task):
    """Prints a task to the console.

    Arguments:
        :task: OrderedDict of task details
    """
    print('Date: {}'.format(task['date']))
    print('Title: {}'.format(task['title']))
    print('Time Spent: {} minutes'.format(task['time']))
    if len(task['notes']) > 0:
        print('Notes: {}'.format(task['notes']))


def search_tasks(date, search_fn):
    """Checks that tasks were returned before attempting to search.

    Arguments:
        :date: date to be searched DD/MM/YYYY format
        :search_fn: function to be executed if tasks were returned from the log
    """
    tasks = read_log()
    if tasks != None and len(tasks) >= 1:
        search_fn(date, tasks)
    else:
        print('There were no tasks found, the work log may not exist or is empty.')


def search_exact_date(date, tasks):
    """Search dates for an exact match

    Arguments:
        :date: format DD/MM/YYYY
        :tasks: list of tasks
    """
    matching_tasks = [task for task in tasks if task['date'] == date]
    if len(matching_tasks) >= 1:
        for task in matching_tasks:
            print_task(task)
    else:
        print('Sorry, no tasks found for that date.')
