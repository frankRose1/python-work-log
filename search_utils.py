"""
    Contains helper functions to search through the log.csv contents
"""

def print_task(task):
    """Prints a task to the console.

    Arguments:
        :task: OrderedDict of task details
    """
    print('-'*25)
    print('Date: {}'.format(task['date']))
    print('Title: {}'.format(task['title']))
    print('Time Spent: {} minutes'.format(task['time']))
    if len(task['notes']) > 0:
        print('Notes: {}'.format(task['notes']))
    print('-'*25)


def search_tasks(search_query, tasks, search_fn):
    """Checks that tasks were returned before attempting to search.

    Arguments:
        :search_query: Searching by date, time, title etc.
        :tasks: tasks will either be a list, or in the case the file is not 
        found tasks will be none.
        :search_fn: function to be executed if tasks were returned from the log
    """
    if tasks != None and len(tasks) >= 1:
        search_fn(search_query, tasks)
    else:
        print('There were no tasks found, the work log may not exist or is empty.')


def search_exact_date(date, tasks):
    """Search tasks by date. Looks for exact match

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


def search_by_minutes(time, tasks):
    """Search tasks by time spent

    Arguments:
        :time: amount of time the task took in minutes
        :tasks: list of tasks
    """
    matching_tasks = [task for task in tasks if task['time'] == time]
    if len(matching_tasks) >= 1:
        for task in matching_tasks:
            print_task(task)
    else:
        print('Sorry, no tasks found with that time.')
