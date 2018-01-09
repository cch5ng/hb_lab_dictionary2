"""Restaurant rating lister."""
import sys
import random


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
        print '\nWould you like to:'
        print '1) See all restaurant ratings'
        print '2) Add a new restaurant rating'
        print '3) Update a random restaurant\'s rating'
        print 'Q) Quit'
        main_choice = raw_input('> ')
        print '\n'

        if main_choice == '1':
            print_ratings(ratings)
        elif main_choice == '2':
            request_rating(ratings)
        elif main_choice == '3':
            update_random_rating(ratings)
        elif main_choice.upper() == 'Q':
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
        if continue_choice.upper() == 'Y':
            rest = raw_input('Please enter a restaurant: ')
            rating = validate_rating('Please rate the restaurant: ')

            # while not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
            #     print 'Please add a numerical rating between 1 and 5.'
            #     rating = raw_input('Please rate the restaurant: ')

            rest = rest[0].upper() + rest[1:]
            ratings[rest] = rating
        else:
            print '\n'
            break


def update_random_rating(ratings):
    random_restaurant = random.choice(ratings.keys())
    print 'The rating for {} is {}.'.format(random_restaurant, ratings[random_restaurant])
    # new_rating = raw_input('What is your rating? ')
    new_rating = validate_rating('What is your rating? ')
    ratings[random_restaurant] = new_rating


def validate_rating(msg):
    """Prints msg and requests a rating between 1 and 5 to return."""

    rating = raw_input(msg)
    while not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
        print 'Please add a numerical rating between 1 and 5.'
        rating = raw_input(msg)

    return rating


if len(sys.argv) > 1:
    sort_rest_ratings(sys.argv[1])
else:
    sort_rest_ratings()
