# Technical Exercise

## Instructions

Write a program that reads data from a CSV file, transforms the data, and produces an output CSV file.  When finished, **please issue a pull request** with your program source code.

* Can use external libraries
* Can be coded in any language
* Does not have to be syntactically correct
* We will not run this code
* We are focusing more on how you approach solving this problem
* You have ~45 minutes to solve the following exercise

## Program Input: Faculty Appointments CSV

Please use the provided [input CSV file](input.csv) of faculty appointments

All rows have the following columns:

* employee_id
* name
* department_id
* title_code
* step
* appointment_period: begin and end date separated by pipe “|” character.  Date format is YYYY-MM-DD.

Rows *may* have up to 4 additional faculty appointments appended to the end for a total of 5 appointments.  A single faculty appointment consists of the following columns:

* department_id
* title_code
* step
* appointment period

## Program Output

[Example output CSV file](output.csv)

Output CSV file requirements:

* A CSV that includes only active appointments (i.e.: when appointment_period is current).
* Only the following columns should be included, in order:
  * employee_id
  * name
  * department_id
  * title_code
  * step
  * appt_begin_date
  * appt_end_date

* Should list one faculty appointment per row.  All subsequent faculty appointments should be listed on separate rows with all other data repeated.
* appt_begin_date and appt_end_date should be extracted from the ‘appointment_period’ column of the faculty appointments CSV.
* All output dates should have the format MM/DD/YYYY
* Output should be a valid CSV file.

## Optional (if time allows):

Optional requirements:

* Change the program to take in a title_code parameter.  This parameter acts as a filter on the output file: only appointments with a matching title code should be output.
* Add a test

Optional output CSV file:

* When given a title_code input parameter of "1200", return the following [CSV file](output-1200.csv)
