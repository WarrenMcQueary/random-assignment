"""Input a text list of people, and a text list of assignments, each separated by newlines.  Output a new .txt file
where each person has an assignment randomly chosen, and the leftover assignments are shown at the bottom of the file.
"""

import random

# Import list of people and list of assignments as .txt files, turning each into a list.
people_file = open("people.txt", "r")
people_list = people_file.readlines()
assignments_file = open("assignments.txt", "r")
assignments_list = assignments_file.readlines()

# Convert instances of "\n" in people_list to "\t", and make all-caps.
for pp in range(len(people_list)):
    people_list[pp] = people_list[pp].replace("\n", ": ")
    people_list[pp] = people_list[pp].upper()

# Randomly give an assignment to each person, keeping track of leftovers.  Store these pairings in a variable.
# assignments_list becomes the list of leftovers throughout the for loop.
pairings = []
for pp in range(len(people_list)):
    random_assignment_index = random.randint(0, len(assignments_list)-1)
    pairings.append([people_list[pp], assignments_list[random_assignment_index]])
    assignments_list.pop(random_assignment_index)

# Export a new .txt file, including leftovers.
output_pairings_file = open("output_pairings.txt", "w")
for pairing in pairings:
    output_pairings_file.write(pairing[0])
    output_pairings_file.write(pairing[1])
    output_pairings_file.write("\n")
output_pairings_file.write("\n\nLEFTOVERS:\n")
for leftover in assignments_list:
    output_pairings_file.write(leftover)

# Close files.
people_file.close()
assignments_file.close()
output_pairings_file.close()
