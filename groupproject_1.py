import csv
import os
import unittest

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

#Abbey Halabis Calculations: add my calculations


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



#-------------------------------------------UNIT TESTS--------------------
class TestPenguinFunctions(unittest.TestCase):
#Anna Kerhoulas tests:

#Abbey Halabis tests:

#Claire Fuller tests:
    def setUp(self):
        self.sample_penguins = [
            {"species": "Adelie", "island": "Torgersen", "sex": "male", "body_mass_g": 3700, "flipper_length_mm": 180},
            {"species": "Adelie", "island": "Torgersen", "sex": "female", "body_mass_g": 3400, "flipper_length_mm": 176},
            {"species": "Chinstrap", "island": "Dream", "sex": "male", "body_mass_g": 3800, "flipper_length_mm": 195},
            {"species": "Gentoo", "island": "Biscoe", "sex": "NA", "body_mass_g": None, "flipper_length_mm": None},
            {"species": "Adelie", "island": "Torgersen", "sex": None, "body_mass_g": 3600, "flipper_length_mm": 178},
        ]
    # -----------------gender distribution-----------------
    def test_gender_distribution_normal_mixed(self):
        result = calculate_gender_distribution(self.sample_penguins)
        adelie_torg = result["Adelie"]["Torgersen"]
        total_percent = sum(adelie_torg.values())
        self.assertAlmostEqual(total_percent, 100.0, delta=0.01) # asked chat gpt about assert almost equal and helped me do delta
        self.assertIn("male", adelie_torg)
        self.assertIn("female", adelie_torg)
        self.assertIn("NA", adelie_torg)

    def test_gender_distribution_single_species(self):
        penguins_single = [
            {"species": "Adelie", "island": "Torgersen", "sex": "female"},
            {"species": "Adelie", "island": "Torgersen", "sex": "male"}
        ]
        result = calculate_gender_distribution(penguins_single)
        adelie = result["Adelie"]["Torgersen"]
        self.assertAlmostEqual(adelie["male"], 50.0, delta=0.01) # same thing with delta
        self.assertAlmostEqual(adelie["female"], 50.0, delta=0.01)

    def test_gender_distribution_all_na(self):
        penguins_all_na = [
            {"species": "Adelie", "island": "Dream", "sex": None},
            {"species": "Adelie", "island": "Dream", "sex": "NA"}
        ]
        result = calculate_gender_distribution(penguins_all_na)
        adelie_dream = result["Adelie"]["Dream"]
        self.assertAlmostEqual(adelie_dream["NA"], 100.0, delta=0.01) # same thing with delta
        self.assertEqual(adelie_dream["male"], 0)
        self.assertEqual(adelie_dream["female"], 0)

    def test_gender_distribution_empty(self):
        result = calculate_gender_distribution([])
        self.assertEqual(result, {})

    # -----------------size vs island-----------------
    def test_size_vs_island_normal(self):
        result = analyze_size_vs_island(self.sample_penguins)
        self.assertIn("Torgersen", result)
        self.assertIn("Dream", result)
        self.assertIn("Biscoe", result)
        self.assertIsInstance(result["Torgersen"]["avg_body_mass_g"], float)
        self.assertIsInstance(result["Torgersen"]["avg_flipper_length_mm"], float)

    def test_size_vs_island_two_islands(self):
        penguins_islands = [
            {"island": "Dream", "body_mass_g": 4000, "flipper_length_mm": 200},
            {"island": "Biscoe", "body_mass_g": 5000, "flipper_length_mm": 210}
        ]
        result = analyze_size_vs_island(penguins_islands)
        self.assertEqual(result["Dream"]["avg_body_mass_g"], 4000)
        self.assertEqual(result["Biscoe"]["avg_flipper_length_mm"], 210)

    def test_size_vs_island_missing_values(self):
        penguins_missing = [
            {"island": "Dream", "body_mass_g": None, "flipper_length_mm": None}
        ]
        result = analyze_size_vs_island(penguins_missing)
        self.assertIsNone(result["Dream"]["avg_body_mass_g"])
        self.assertIsNone(result["Dream"]["avg_flipper_length_mm"])

    def test_size_vs_island_empty(self):
        result = analyze_size_vs_island([])
        self.assertEqual(result, {})



#-------------------output/main-----------------------
#output call for everyone
def main():
    #universal
    penguin_data = load_penguins("penguins.csv")



#Anna Kerhouslas output:

#Abbey Halabis output:

#Claire Fuller output

    #define function calls
    averages = analyze_size_vs_island(penguin_data)
    gender_dist = calculate_gender_distribution(penguin_data)

#size v island output

    print("Average Body Mass & Flipper Length by Island:")
    for island, values in averages.items():
        avg_mass = values["avg_body_mass_g"]
        avg_flipper = values["avg_flipper_length_mm"]
        print(f"{island}:")
        print(f"- Avg Body Mass (g): {avg_mass if avg_mass is not None else 'N/A'}")
        print(f"- Avg Flipper Length (mm): {avg_flipper if avg_flipper is not None else 'N/A'}")

#gender distribution output

    print("\nGender Distribution by Island:")
    for species, islands in gender_dist.items():
        print(f"{species}:")
        for island, genders in islands.items():
            gender_str = ", ".join([f"{g}: {round(p, 2)}%" for g, p in genders.items()])
            print(f"- {island}: {gender_str}")
#stuff i had for debugging
    #size_results = analyze_size_vs_island(penguins=penguin_data)
    #print(size_results)
    
    #gender_distribution = calculate_gender_distribution(penguins=penguin_data)
    #print(gender_distribution)

    print("All Done!")

if __name__ == "__main__":
    main()
    unittest.main(exit=False)