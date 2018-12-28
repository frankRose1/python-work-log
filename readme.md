# Python Work Log

Terminal application that allows a user to enter tasks which will then be saved as a row in a csv file.
Date, title, minutes, and optional notes can all be added to the csv. There are various search options and any matching task(s)
will be printed to the console.

## App Features

- Object oriented approach
- `LogUtil` class will check for the `log.csv` when the app launches and create it if it doesn't exist
- tasks are loaded from the file system when the app starts
- Can search by:
  - exact Date
  - time spent
  - exact title or notes
  - enter a regex pattern that will look for a match in either title or notes
