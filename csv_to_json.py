import csv
import json

# This module is used to convert the CSV from Bakkesmod "dumpitems" command to JSON

# TODO: change how dict is converted so Key in Json data is ID number and not duplicated

def make_json(csv_filepath, json_filepath):

    # Initialize dict
    data = {}

    # Open CSV file and load into into csv.reader object
    with open(csv_filepath) as csvfile:
        csvreader = csv.reader(csvfile)


        # Iterate through rows
        for rows in csvreader:
            id_list = rows[0]
            type_list = rows[1]
            dbname_list = rows[2]
            name_list = rows[3]

            # id_list is ID number eg. "28"
            # type_list is type eg. "Skin"
            # dbname_list is Full name in RL database eg. "Product_TA ProductsDB.Products.Body_Torch"
            # name_list is display name, what the item is actually called in game eg. "X-Devil"

            key = rows[0]
            data[key] = rows



    with open(json_filepath, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))


        


    make_json("items.csv", "rl_items.json")