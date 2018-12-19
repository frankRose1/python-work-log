import csv
import os


def save_to_log(task):
    """Saves the task to the log.csv file.

    Arguments:
        :task: Dict of task details
    """
    with open('log.csv', mode='a') as log_csv:
        fieldnames = ['date', 'title', 'time', 'notes']
        log_writer = csv.DictWriter(log_csv, fieldnames)
        log_writer.writerow(
            {'date': task['date'], 'title': task['title'], 'time': task['time'], 'notes': task['notes']})


def read_log():
    """Reads in the log's content and returs in as a list of OrderedDicts.
        If a "FileNotFound" Error is caught, it will return "None".
    """
    # try/except in case the file somehow is removed
    try:
        with open('log.csv', mode="r") as log_csv:
            log_content = []
            log_reader = csv.DictReader(log_csv)
            for row in log_reader:
                log_content.append(row)
            return log_content
    except FileNotFoundError:
        print('Error: "log.csv" file not found!')
        return None


def check_for_log():
    """When the app starts, check to see if the csv exists
        and if not, create it and write the headers
    """
    file_exists = os.path.isfile('log.csv')
    if not file_exists:
        with open('log.csv', mode='w') as csv_file:
            fieldnames = ['date', 'title', 'time', 'notes']
            log_writer = csv.DictWriter(csv_file, fieldnames)
            log_writer.writeheader()
