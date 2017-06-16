'''
Program Title: user_prefs_helper.py
Author: Aaron A
Program Description: Convert CSV objects to JSON readable format.

This helper class will store user preferences.

A second helper class will be created to read the user preferences from
this class' generated csv as soon as the log-in and password has been
verified (see: log_in_helper.py)

'''
import csv
import json

csvfile = open('/home/aaron/Desktop/pcc/github/shoe-player/shoeplayer/prefs/user-pref.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("_id","username","playlist","artist","song","date-added","like?")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
