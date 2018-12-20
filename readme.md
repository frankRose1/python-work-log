# Python Work Log
Terminal application that allows a user to enter tasks which will then be saved as a row in a csv file.
Date, title, minutes, and optional notes can all be added to the csv. You can also search by exact date or exact minutes and the task(s)
will be printed to the console.

## App Features
* Object oriented approach
* ```LogUtil``` class will check for the ```log.csv``` when the app launches and create it if it doesn't exist
* tasks are loaded from the file system when the app starts
* Can search by:
  * exact Date
  * time spent