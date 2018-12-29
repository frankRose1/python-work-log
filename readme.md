# Python Work Log
Terminal application that allows a user to enter tasks which will then be saved as a row in a csv file.
Date, title, minutes, and optional notes can all be added to the csv. There are various search options and any matching task(s)
will be printed to the console.

## App Features
- Object oriented approach
- ```LogUtil``` class will check for the `log.csv` when the app launches and create it if it doesn't exist
- tasks are loaded from the file system when the app starts
- Can search by:
  - exact Date
  - time spent
  - exact title or notes
  - enter a regex pattern that will look for a match in either title or notes

## To Run
- clone this repo
- ```cd``` in to the root directory
- in your terminal type ```python work_log.py```
- Note: I removed the ```log.csv``` from the repo but the app will create it for you if it doesn't already exist

## Technologies Used
- Only the standard python library was used - No 3rd party packages
