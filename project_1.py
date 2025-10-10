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

#--------Helper Functions for calculate gender distrubution----------Claire Fuller

def group_island_by_sex(penguins): # group penguin by island and gender occurance
    count = {}
    for p in penguins:
        island = p.get("island", 'Unknown')
        sex = (p.get("sex") or "Unknown").capitalize() 
        if island not in count:
            count[island] = {"Male": 0, "Female": 0, "Unknown": 0}

        if sex not in count[island]:
            count[island][sex] = 0 #mkaing sure the key exsists for na vlaues am i supposed t put this as a test case???
            count[island][sex] += 1

    return count

 def ca                            

#hello
#split up the functions that me and my group are doing
