import csv
import os

#Reading CSV into a list of dicts
def load_penguins(filename):
    data = []
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path,filename)
    with open(file_path, mode = 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    #print (data)
    return data

#Anna Kerhouslas calculation 1


#--------Helper Functions for calculate gender distrubution----------

def group_island_by_sex(penguins):
    count = {}
    for p in penguins:
        island = p.get("island", 'Unknown')
        sex = p.get(sex", 
#hello
#split up the functions that me and my group are doing
