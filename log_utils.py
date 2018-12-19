import csv
import os


def save_to_log(task):
    """Saves the task to the log.csv file
    """
    with open('log.csv', mode='a') as log_csv:
        fieldnames = ['date', 'title', 'time', 'notes']
        log_writer = csv.DictWriter(log_csv, fieldnames)
        log_writer.writerow(
            {'date': task['date'], 'title': task['title'], 'time': task['time'], 'notes': task['notes']})


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
