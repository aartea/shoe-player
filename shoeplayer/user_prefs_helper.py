'''
Program Title: log_in_helper.py
Author: Aaron A
Program Description: Convert CSV objects to JSON readable format.


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
