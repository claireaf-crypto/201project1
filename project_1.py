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

#Anna Kerhouslas calculations:

#Abbey Halabis Calculations:


#Claire Fuller Calculations:
#--------Helper Functions for calculate gender distrubution----------Claire Fuller
#gender occurance grouping functions 
def group_island_by_sex(penguins): # group penguin by island and gender and species occurance
    counts = {}
    for p in penguins:
        species = p.get("species", "Unknown")
        island = p.get("island", 'Unknown')
        sex = (p.get("sex") or "Unknown").capitalize() 

        if species not in counts:
            counts[species] = {}
        
        if island not in counts:
            counts[island] = {"Male": 0, "Female": 0, "Unknown": 0}

        if sex not in counts[island]:
            counts[island][sex] = 0 #mkaing sure the key exsists for na vlaues am i supposed t put this as a test case???
        counts[species][island][sex] += 1

    return counts

#convert the genders into percentages
def calculate_percentage(counts_dict):
    percentages = {}

    for species, island_data in counts_dict.items():
        percentages[species] = {}

        for island, counts in counts_dict.items():
            total = sum(counts.values())

            if total == 0:
                island_percentages = {}
                for gender in counts:
                    island_percentages[gender] = 0
                percentages[island] = island_percentages
                continue
    
        island_percentages = {}
        for gender, count in counts.items():
            percent = (count / total ) * 100
            island_percentages[gender] = percent

        percentages[species][island] = island_percentages
    

    return percentages

def 




#split up the functions that me and my group are doing

#call functions
#def main():