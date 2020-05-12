import time
import pandas as pd
import numpy as np

# Mapping of city filter to the appropriate file
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Valid month filters
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

# Valid day of week filters
DAYS_OF_WEEK = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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
    while True:
        city = input('\nEnter name of city to analyze (chicago, new york city, washington):\n').lower()
        if city in CITY_DATA.keys():
            break

        print("Invalid city")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('\nFilter by name of month, valid months are: january, feburary, march, april, may, june')
        month = input('Enter name of the month to filter by, or "all" to apply no month filter:\n').lower()
        if month in MONTHS:
            break;

        print("Invalid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('\nFilter by day of week, valid days are: sunday, monday, tuesday, wednesday, thursday, friday, saturday')
        day = input('Enter name of the day of week to filter by, or "all" to apply no day filter:\n').lower()
        if day in DAYS_OF_WEEK:
            break;

        print("Invalid day of week")

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
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    time_start = time.time()

    # TO DO: display the most common month
    print("Most common month:", MONTHS[df['month'].mode()[0]-1].title())

    # TO DO: display the most common day of week
    print("Most common day of week:", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("Most common start hour:", df['start_hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - time_start))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common start station:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most common end station:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + " / " + df['End Station']
    print("Most frequent combination of start station and end station trip:", df['start_end'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", int(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("Mean travel time:", int(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n", df['User Type'].value_counts().to_frame())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("\nCounts of user types:\n", df['Gender'].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("\nEarliest year of birth:", int(df['Birth Year'].min()))
        print("Recent year of birth:", int(df['Birth Year'].max()))
        print("Most common year of birth:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    row_index = 0

    # show all column names
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    while True:
        display = input('\nWould you like to see 10 lines of raw data? Enter yes or no.\n')
        if display.lower() != 'yes':
            break

        print(df.iloc[row_index:row_index+10])
        row_index += 10

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
