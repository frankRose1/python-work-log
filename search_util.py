import re


class SearchUtil:
    """ Helper class that provides methods to search through the log.csv contents """

    @staticmethod
    def print_tasks(matching_tasks):
        """If any tasks matched a search, they will be printed to the terminal.

        Arguments:
            :matching_tasks: potential list of tasks that matched a user's search.
        """
        if len(matching_tasks) >= 1:
            for task in matching_tasks:
                print('-'*25)
                print('Date: {}'.format(task['date']))
                print('Title: {}'.format(task['title']))
                print('Time Spent: {} minutes'.format(task['time']))
                if len(task['notes']) > 0:
                    print('Notes: {}'.format(task['notes']))
                print('-'*25)
        else:
            print('Sorry, no tasks found.')

    @staticmethod
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

    @classmethod
    def search_exact_date(cls, date, tasks):
        """Search tasks by date. Looks for exact match

        Arguments:
            :date: format DD/MM/YYYY
            :tasks: list of tasks
        """
        matching_tasks = [task for task in tasks if task['date'] == date]
        cls.print_tasks(matching_tasks)

    @classmethod
    def search_by_minutes(cls, time, tasks):
        """Search tasks by time spent

        Arguments:
            :time: amount of time the task took in minutes
            :tasks: list of tasks
        """
        matching_tasks = [task for task in tasks if task['time'] == time]
        cls.print_tasks(matching_tasks)

    @classmethod
    def exact_search(cls, query, tasks):
        """Search tasks for an exact search in the notes or title

        Arguments:
            :query: string the user is attempting to search by
            :tasks: list of tasks
        """
        matching_tasks = [task for task in tasks if (
            task['title'] == query) or (task['notes'] == query)]
        cls.print_tasks(matching_tasks)

    @classmethod
    def regex_search(cls, pattern, tasks):
        """User provides a regex pattern that is used to search title and notes

        Arguments:
            :pattern: regex pattern provided by the user
            :tasks: list of tasks
        """
        raw_str_pattern = r''+pattern
        matching_tasks = [task for task in tasks if (
            re.search(raw_str_pattern, task['title'])) != None or
            (re.search(raw_str_pattern, task['notes'])) != None]
        cls.print_tasks(matching_tasks)
