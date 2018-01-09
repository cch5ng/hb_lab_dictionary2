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

    request_rating(ratings)
    #ratings[new_restaurant] = new_rating

    sorted_restaurants = sorted(ratings.keys())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant, ratings[restaurant])


def request_rating(ratings):
    """Gets restaurant and rating from command line and updates existing dictionary
    of ratings.
    """

    while True:
        continue_choice = raw_input('Would you like to add a restaurant? (Y/N)')
        if continue_choice == 'Y':
            rest = raw_input('Please enter a restaurant: ')
            rating = raw_input('Please rate the restaurant: ')

            rest = rest[0].upper() + rest[1:]
            ratings[rest] = rating
        else:
            print '\n'
            break


if len(sys.argv) > 1:
    sort_rest_ratings(sys.argv[1])
else:
    sort_rest_ratings()
