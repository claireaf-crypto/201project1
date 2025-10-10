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
#--------Helper Functions for calculate gender/species distrubution----------Claire Fuller
#gender occurance grouping functions 
def group_species_island_by_sex(penguins): # group penguin by island and gender and species occurance
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
#--------Final call for calculate gender/species distrubution----------Claire Fuller
def calculate_gender_distribution(penguins):
    grouped = group_species_island_by_sex(penguins)
    percentages = calculate_percentage(grouped)
    return percentages

#--------Helper Functions size of penguin vs island----------Claire Fuller

def group_data_by_island(penguins):
    data = {}

    for penguin in penguins:
        island = penguin.get("island", "Unknown")

        # If the island isn't in the dictionary yet, create an entry for it
        if island not in data:
            data[island] = {"body_mass": [], "flipper_length": []}

        try: # had to ask chatgpt about tru and except erros because i forgot from 106
            body_mass = penguin.get("body_mass")
            flipper_length = penguin.get("flipper_length")

            if body_mass:
                data[island]["body_mass"].append(float(body_mass))
            if flipper_length:
                data[island]["flipper_length"].append(float(flipper_length))
        except ValueError:
            continue

    return data

#finding the averages for weight and flipper size
def compute_averages(grouped_data):
    averages = {}

    for island, values in grouped_data.items():
        avg_mass = safe_average(values["body_mass"])
        avg_flipper = safe_average(values["flipper_length"])

        averages[island] = {
            "avg_body_mass": avg_mass,
            "avg_flipper_length": avg_flipper
        }

    return averages

# make sure if there none is returns none
def safe_average(numbers):
    if not numbers:
        return None
    return round(sum(numbers) / len(numbers), 2)

#--------Final call for analyze size vs island----------Claire Fuller
def analyze_size_vs_island(penguins):

    grouped_data = group_data_by_island(penguins)
    averages = compute_averages(grouped_data)

    return averages

#call functions
#def main():