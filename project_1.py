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
#--------Helper Functions for calculating gender/species distrubution----------Claire Fuller
#gender occurance grouping functions 
def group_species_island_by_sex(penguins): # group penguin by island and gender and species occurance
    counts = {}
    for p in penguins:
        species = p.get("species", "NA")
        island = p.get("island", 'NA')
        sex = (p.get("sex") or "NA") 

        if species not in counts:
            counts[species] = {}
        
        if island not in counts[species]:
            counts[species][island] = {"male": 0, "female": 0, "NA": 0}

        if sex not in counts[species][island]:
            counts[species][island][sex] = 0 #making sure the key exsists for na vlaues am i supposed t put this as a test case???
        
        counts[species][island][sex] += 1

    return counts

#convert the genders into percentages
def calculate_percentage(counts_dict):
    percentages = {}

    for species, island_data in counts_dict.items():
        percentages[species] = {}

        for island, counts in island_data.items():
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
# Returns the percentage of male/femail/na for each species on each island
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
            data[island] = {"body_mass_g": [], "flipper_length_mm": []}

        try: # had to ask chatgpt about tru and except erros because i forgot from 106
            body_mass_g = penguin.get("body_mass_g")
            flipper_length_mm = penguin.get("flipper_length_mm")

            if body_mass_g:
                data[island]["body_mass_g"].append(float(body_mass_g))
            if flipper_length_mm:
                data[island]["flipper_length_mm"].append(float(flipper_length_mm))
        except ValueError:
            continue

    return data

#finding the averages for weight and flipper size
def compute_averages(grouped_data):
    averages = {}

    for island, values in grouped_data.items():
        avg_mass = safe_average(values["body_mass_g"])
        avg_flipper = safe_average(values["flipper_length_mm"])

        averages[island] = {
            "avg_body_mass_g": avg_mass,
            "avg_flipper_length_mm": avg_flipper
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
#please write four test cases
#per function. Two must test general/usual cases and two test edge cases.
#For the project 1 test cases, please use a sample of your chosen csv dataset (ensure to use data that has
#  NA/null values)
#  rather than re-reading/reusing your entire csv file.

#output call
def main():
    print("Debugginhg file directly.")

    penguin_data = load_penguins("penguins.csv")

    size_results = analyze_size_vs_island(penguins=penguin_data)
    print(size_results)
    
    gender_distribution = calculate_gender_distribution(penguins=penguin_data)
    print(gender_distribution)

    print("Done")


if __name__ == "__main__":
    main()
