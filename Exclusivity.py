# take in the number
n = input().strip()

# Split the input string into a list of integers
coordinates = list(map(int, n.split()))

# Use a set to track seen coordinates and maintain order
seen = set()
unique_coordinates = []

for i in coordinates:
    if i not in seen:
        unique_coordinates.append(i)
        seen.add(i)

# Print the refined list
print(" ".join(map(str, unique_coordinates)))
#Author: voloshka_3 / vasilek3
#Name: Exclusivity
#Level: very easy
