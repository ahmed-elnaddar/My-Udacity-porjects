import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

# list of valid months name
months = ['january', 'february', 'march', 'april', 'may', 'june']
# list of valid boolean inputs
boolean = ['yes', 'no']


def valid_input(lst, msg, err_msg = "Invalid input, please try again."):
    """
    Asks user for input and check if it in our "valid inputs list"
    
    Arguments:
        (iterable) lst - iterable of "valid inputs" to check our input
        (str) msg - message that we want to ask user
        (str) err_msg - error message to make user try again
       
    Returns:
        (str) inp - your valid input
    """
    while True:
        inp = input(msg)
        inp = inp.lower()
        if inp not in lst:
            print(err_msg)
            continue
        else:
            break
    return inp
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = valid_input(CITY_DATA.keys(),
                "Would you like to see data for Chicago, New York, or Washington? ")
    
    # Get user input for option
    options = ['day', 'month', 'none']
    option = valid_input(options,
                         "\nWould you like to filter the data by month, day, or not at all?\nType 'none' for no time filter.\n")
    
        
    # TO DO: get user input for month (all, january, february, ... , june)
    if option == 'none':
        month = "all"
        day = "all"
        
    elif option == 'month':
        # using the index of the months list to get the corresponding int
        month = valid_input(months,
                            "Which month - January, February, March, April, May, or June? ")
        day = "all"
        
    elif option == 'day':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        month = "all"
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = valid_input(days,
                          "Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ")
        


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month_name = months[df['month'].mode()[0] - 1]
    print("Most common month: %s" % common_month_name)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most common day: %s" % common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common hour: %s" % common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_satation = df['Start Station'].mode()[0]
    print("Most common start station: %s" % common_start_satation)

    # TO DO: display most commonly used end station
    common_end_satation = df['End Station'].mode()[0]
    print("Most common end station: %s" % common_end_satation)

    # TO DO: display most frequent combination of start station and end station trip
    common_comb = ('from "' + df['Start Station'] + '"' + " to " + '"' + df['End Station'] + '"').mode()[0]
    print("Most common end station: %s" %  common_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = pd.Timedelta(df['Trip Duration'].sum(), unit='s')
    print("Total travel time: %s" %  total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = pd.Timedelta(df['Trip Duration'].mean(), unit='s')
    print("Travel time average: %s" %  mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_type = df['User Type'].value_counts()
    print("Counts of user types:\n{}\n\n".format(count_type))
    
    col = df.columns
    
    if 'Gender' in col:
        # TO DO: Display counts of gender
        gender = df['Gender']
        print("Counts of user gender:\n{}\n\n".format(gender.value_counts()))
        
    if 'Birth Year' in col:
        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        oldest = int(max(birth_year))
        youngest = int(min(birth_year))
        common = int(birth_year.mode()[0])
        
        print("Earliest, most recent, and most common year of birth:\n\
Oldest birth year {}".format(oldest))
        print("Youngest birth year {}".format(youngest))
        print("Common birth year {}".format(common))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    function to display a row data from our dataset
    
    Arguments:
    (DataFrame) pd - dataset that we want to display data from.
    """
    start_time = time.time()

    i = 0
    pd.set_option('display.max_columns',200)

    while True:            
        raw = valid_input(boolean, "Would you like to see the raw data? ")
        if raw == 'no':
            break
        print(df[i:i+5])
        i += 5
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = valid_input(boolean, '\nWould you like to restart? Enter yes or no.\n')
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
