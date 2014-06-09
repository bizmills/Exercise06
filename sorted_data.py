# from sys import argv

# filename = argv[1]
# input_file = open(filename)
input_file = open("scores.txt")

restaurant_ratings = {}

for line in input_file:
    line = line.rstrip()
    restaurant_data = line.split(':')
    rest_name = restaurant_data[0]
    rating = restaurant_data[1]
    restaurant_ratings[rest_name] = rating
print restaurant_ratings