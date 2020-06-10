import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities = ['chicago', 'new york city', 'washington']
    while True:
            city = input('Which of these cities do you want to explore : Chicago, New York City or Washington? \n> ').lower()
            if city in cities:
                print("We are happy to explore this city with you!")
                break           
            else:
                print('Sorry, We dont have data on this city or place!')
                continue
            
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month = input('Kindly select a month from january to june or "all" for no week filter \n> {} \n> '.format(months)).lower()
        if month in months:
            print('You have selected {}'.format(month))
            break
        else:
            print('No information on this month, Are you sure you selected a valid month?')
            continue
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    while True:
        day = input('Kindly select a day of the week or "all" for no day filter \n> {} \n>'.format(days)).lower()
        if day in days:
            print('You have selected {}'.format(day))
            break
        else:
            print('This is not a day of the week')
    
    return city, month, day
    print('-'*40)
    


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

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day:', most_common_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular start station: ', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular end station: ', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    best_combination = df[['Start Station', 'End Station']].mode()
    print('The most combination used start station and end station : {}'.format(best_combination))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total trip duration: ',total_time)

    # TO DO: display mean travel time
    mean_per_trip = df['Trip Duration'].mean()
    print('mean travel time is : ',mean_per_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('counts of user types : ',count_user_types)

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('Gender count : ',count_gender)
    except KeyError:
        print("This dataset doesn't have any gender column")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('the earliest birth year is: ',earliest)
        recent = df['Birth Year'].max()
        print('the most recent birth year is: ',recent)
        common = df['Birth Year'].mode()
        print('the most common birth year is: ',common)
    except KeyError:
        print("This dataset doesn't have any gender column")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Continuously asks user to specify if they want to see raw data, returns 5 lines of raw data for every "yes reply" 
    till user replies with no  
    """
    reply = ['yes', 'no']
    while True:
        user_reply = input('Would you like to see the raw data ? Kindly reply with a "yes" or "no" \n> ').lower()
        while user_reply == 'yes':
            df.iloc[4:]
        else:
            break
                  

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
