#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL= "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)


def get_file_content(url):
    """Download the file over the internet and
    convert needed columns into sorted dictionary."""

    my_dict = {}
    with requests.get(url, stream=True) as r:
        lines = (line.decode('utf-8') for line in r.iter_lines())
        reader = csv.reader(lines)
        next(reader)
        for row in reader:
            my_dict[row[3]] = [row[0] + " " + row[1]]
    return dict(sorted(my_dict.items()))


def get_same_or_newer(start_date, data):
    """Go through all the data and find the employees that started on the given date,
    or the closest one. Do not include dates after today."""

    my_date_employees = {}
    for key in data:
        name = data[key]
        date = datetime.datetime.strptime(key, '%Y-%m-%d')
        if date >= start_date and date <= datetime.datetime.today():
            my_date_employees[date] = name
        
    return my_date_employees


def list_newer(start_date, data):
    employees = get_same_or_newer(start_date, data)
    for key in employees:
        print("Started on {}: {}".format(key.strftime("%b %d, %Y"), employees[key]))


def main():
    data = get_file_content(FILE_URL)
    start_date = get_start_date()
    list_newer(start_date, data)


if __name__ == "__main__":
    main()