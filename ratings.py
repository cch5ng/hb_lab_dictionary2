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

    while True:
        # Ask user for input
        # 1. See all ratings
        # 2. Add a restaurant rating
        # 3. Quit
        print 'Would you like to:'
        print '1) See all restaurant ratings'
        print '2) Add a new restaurant rating'
        print 'Q) Quit'
        main_choice = raw_input('> ')
        print '\n'

        if main_choice == '1':
            print_ratings(ratings)
        elif main_choice == '2':
            request_rating(ratings)
        elif main_choice == 'Q':
            break
        else:
            'Please enter 1, 2, or Q.'


def print_ratings(ratings):
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

            while not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
                print 'Please add a numerical rating between 1 and 5.'
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
