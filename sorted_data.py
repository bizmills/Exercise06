# from sys import argv

# filename = argv[1]
# input_file = open(filename)
input_file = open("scores.txt")

#builds dictionary
restaurant_ratings = {}

for line in input_file:
    line = line.rstrip()
    restaurant_data = line.split(':')
    rest_name = restaurant_data[0]
    rating = restaurant_data[1]
    restaurant_ratings[rest_name] = rating

# sorts into alphabetized tuples
sorted_rest = (sorted(restaurant_ratings.items()))

#loops through tuples and prints report.
for i in range(len(sorted_rest)):
    print "Restaurant '%s' is rated at %s." % (sorted_rest[i][0], sorted_rest[i][1])


