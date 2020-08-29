import time
import pandas as pd
from datetime import timedelta

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
    # get user input for city (chicago, new york city, washington)
    city = input_validator("Please choose one of the followings cities: Chicago, New York City, Washington \ncity: ", "city").lower()
    filter_choice = input_validator("Please choose a time filter: month, day or none for no time filter \nfilter: ", "filter")

    if filter_choice == "month":
        # get user input for month (january, february, ... , june)  
        month = input_validator("Please choose a month: January, February, March, April, May, June \nmonth: ", "month").lower()
        day = None
    elif filter_choice == "day":
        # get user input for day of week (monday, tuesday, ... sunday)
        day = input_validator("Please choose a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday \nday: ", "day").lower()
        month = None
    else:
        month = None
        day = None

    print('-'*40)
    return city, month, day


def input_validator(input_str, type):
    """
    Validates user input based on the type of input (e.g. month, day, filter)

    Returns:
        (input_value) - user input value 
    """
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
            if type == "answer":
                result = validate_yes_no_answer(input_value)
            if not result:
                raise Exception("Please type one of the values above")
        except Exception as error:
            print(error)
            continue
        break
    return input_value

def validate_city(city):
    for key, value in CITY_DATA.items():
        if key == city.lower():
            return True
    return False

def validate_filter_choice(filter_choice):
    filter_options = ['month', 'day', 'none']
    return True if filter_choice.lower() in filter_options else False

def validate_month(month):
    for key, value in MONTHS.items():
        if key == month.lower():
            return True
    return False

def validate_day(day):
    for key, value in DAYS.items():
        if key == day.lower():
            return True
    return False

def validate_yes_no_answer(answer):
    answer_options = ['yes', 'no']
    return True if answer.lower() in answer_options else False


def get_dict_key(value, dict_list):
    for key, val in dict_list.items():
        if val == value:
            return key


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
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['week day'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    """
    Return Data Frame with month filter
    """
    if month != None:
        month_filter = df[df['month'] == MONTHS[month.lower()]]
        return month_filter
    elif day != None:
        day_filter = df[df['week day'] == DAYS[day.lower()]]
        return day_filter
    else:
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()

    # display the most common day of week
    most_common_week_day = df['week day'].value_counts().idxmax()

    # display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    most_common_hour = df['hour'].value_counts().idxmax()


    print("Most common month: {}".format(get_dict_key(most_common_month, MONTHS).title()))
    print("Most common week day: {}".format(get_dict_key(most_common_week_day, DAYS).title()))
    print("Most common hour: {} (24h format)".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()

    # display most frequent combination of start station and end station trip
    df['Start and End Station Combo'] = df['Start Station'].map(str) + ' - ' + df['End Station'].map(str)
    most_common_start_end_stations_combo = df['Start and End Station Combo'].value_counts().idxmax()

    print("Most common Start station: {}".format(most_common_start_station))
    print("Most common End station: {}".format(most_common_end_station))
    print("Most common Start - End Station Combination: {}".format(most_common_start_end_stations_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_seconds = df['Trip Duration'].sum()
    total_travel_time_hours_mins = timedelta(seconds=int(total_travel_time_seconds))
    # display mean travel time
    mean_travel_time_seconds = df['Trip Duration'].mean()
    mean_travel_time_hours_mins = timedelta(seconds=int(mean_travel_time_seconds))
    
    print("Total travel time: {} (h/m)".format(total_travel_time_hours_mins))
    print("Average travel time: {} (h/m)".format(mean_travel_time_hours_mins))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("User Type counts:\n{}".format(count_user_type))

    # Display counts of gender
    if "Gender" in df.columns:
        count_gender = df['Gender'].value_counts()
        print("\nUser Gender counts:\n{}".format(count_gender))
    else:
        print("Unable to get count for Gender")    


    if "Birth Year" in df.columns:
        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].value_counts().idxmax()

        print("\nEarliest birth year: {}, most recent birth year: {}, and most common birth year: {}".format(earliest_birth, most_recent_birth, most_common_birth))
    else:
        print("Unable to get results for Birth Year")    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_raw_data(df):
    """
    Asks the user whether s/he wants to see raw data. If yes, the script will print 5 rows each time the user types yes.
    """
    raw_data_answer = input_validator("\nWould you like to view raw data? Type yes or no. \n", "answer")
    if raw_data_answer.lower() != "yes":
        return df

    start_count = 0
    while True:
        end_count = start_count + 5
        print(df.iloc[start_count:end_count])
        more_raw_data_answer = input_validator("\nWould you like to view additional raw data? Type yes or no. \n", "answer")
        if more_raw_data_answer.lower() == "yes":
            start_count += 5
            continue
        break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print_raw_data(df)    

        restart = input_validator("\nWould you like to restart? Type yes or no.\n", "answer")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
