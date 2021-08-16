import csv
import json

# This module is used to convert the CSV from Bakkesmod "dumpitems" command to JSON

# TODO: change how dict is converted so Key in Json data is ID number and not duplicated
def make_json(csv_filepath, json_filepath):

    # Initialize list for json data
    data = []

    # TODO: currently, this func needs the CSV file to have a header to work.
    # program a way to automatically add this header into the file
    # Will probably have to create new csv file first, then move data to it



    # Open CSV file and load into into csv.reader object
    with open(csv_filepath) as csvfile:
        csvreader = csv.DictReader(csvfile)


        # Iterate through rows
        for row in csvreader:
            print(row)
            data.append(row)



    with open(json_filepath, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(data, indent=4)
        json_file.write(json_string)






make_json("items.csv", "rl_items.json")