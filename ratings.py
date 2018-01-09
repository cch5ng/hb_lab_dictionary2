"""Restaurant rating lister."""
import sys


def sort_rest_ratings(file_name="scores.txt"):
    """Given a file of restaurants and ratings, prints ratings in alphabetical
    order
    """

    file = open(file_name)
    ratings = dict()
    for line in file:
        restaurant, rating = line.rstrip().split(":")
        ratings[restaurant] = rating

    sorted_restaurants = sorted(ratings.keys())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant, ratings[restaurant])

if len(sys.argv) > 1:
    sort_rest_ratings(sys.argv[1])
else:
    sort_rest_ratings()
