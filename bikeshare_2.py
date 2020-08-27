import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

MONTHS = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6
}

DAYS = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_validator("Please choose one of the followings cities: Chicago, New York City, Washington \ncity: ", "city")
    filter_choice = input_validator("Please choose a time filter: month, day or none for no time filter \nfilter: ", "filter")

    if filter_choice == "month":
        # get user input for month (january, february, ... , june)  
        month = input_validator("Please choose a month: January, February, March, April, May, June \nmonth: ", "month")
        day = None
    elif filter_choice == "day":
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input_validator("Please choose a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday \nday: ", "day")
        month = None
    else:
        month = None
        day = None

    print('-'*40)
    return city, month, day


def input_validator(input_str, type):
    while True:
        input_value = input(input_str)
        try:
            if type == "month":
                result = validate_month(input_value)
            if type == "day":
                result = validate_day(input_value)
            if type == "filter":
                result = validate_filter_choice(input_value)
            if type == "city":
                result = validate_city(input_value)
            if not result:
                raise Exception("Please type one of the values above")
        except Exception as error:
            print(error)
            continue
        break
    return input_value

def validate_city(city):
    cities = ['chicago', 'new york city', 'washington']
    return True if city.lower() in cities else False

def validate_filter_choice(filter_choice):
    filter_options = ['month', 'day', 'none']
    return True if filter_choice.lower() in filter_options else False

def validate_month(month):
    month_options = ['january', 'february', 'march', 'april', 'may', 'june']
    return True if month.lower() in month_options else False

def validate_day(day):
    day_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return True if day.lower() in day_options else False

def load_data(city, month=None, day=None):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    """
    Return Data Frame if no filters applied
    """
    if month == None and day == None:
        return df
    
    if month != None:
        df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df = df[df['month'] == 4]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def str_to_bold(str):
    return "\033[1m{}\033[0m".format(str)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
