

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Name of the city to analyze: ").lower()

        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please enter a valid city name: Chicago, New_York_City or Washington.")

    while True:
        month = input("Name of the month to filter by, or 'all' to apply no month filter: ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please enter a valid month or 'all'.")

    while True:
        day = input("Name of the day of the week to filter by, or 'all' to apply no day filter: ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("You must have made a mistake. Please enter a valid day or 'all'.")

    return city, month, day


# In[5]:

def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()  # Convert day names to lowercase
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df["month"] == month]
    # filter by day of the week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.lower()]  # Convert input day to lowercase

    return df


# In[6]:

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if not df.empty:
        # TO DO: display the most common month
        popular_month = df['month'].mode()[0]

        # TO DO: display the most common day of the week
        popular_day = df['day_of_week'].mode()[0]

        # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]

        print(f"The most common month is {popular_month}")
        print(f"The most common day is {popular_day}")
        print(f"The most common hour is {popular_hour}")
    else:
        print("No data available for the selected filters.")

    print("\nThis took %s seconds." % (time.time() - start_time))


# In[7]:

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    if not df.empty:
        # TO DO: display most commonly used start station
        popular_start_station = df['Start Station'].mode()[0]

        # TO DO: display most commonly used end station
        popular_end_station = df['End Station'].mode()[0]

        # TO DO: display most frequent combination of start station and end station trip
        start_end_station = df['Start Station'] + " to " + df['End Station']
        popular_start_end_station = start_end_station.mode()[0]

        print(f"The most commonly used start station is {popular_start_station}")
        print(f"The most commonly used end station is {popular_end_station}")
        print(f"The most frequent combination of start station and end station trip is {popular_start_end_station}")
    else:
        print("No data available for the selected filters.")

    print("\nThis took %s seconds." % (time.time() - start_time))

# In[8]:

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print(f"The total travel time is {total_travel_time} seconds")
    print(f"The mean travel time is {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))

# In[9]:

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Check if 'Birth Year' column exists in the dataframe
    if 'Birth Year' in df.columns:
        # Display counts of user types
        count_of_user_types = df['User Type'].value_counts()

        # Display counts of gender
        counts_of_gender = df['Gender'].value_counts()

        # Display earliest, most recent, and most common year of birth
        if not df['Birth Year'].isnull().all():
            earliest_birth_year = int(df["Birth Year"].min())
            latest_birth_year = int(df["Birth Year"].max())
            common_birth_year = int(df["Birth Year"].mode()[0])

            print(f"The counts of user types are:\n{count_of_user_types}")
            print(f"The counts of gender are:\n{counts_of_gender}")
            print(f"The earliest, most recent, and most common year of birth are:\n{earliest_birth_year}, {latest_birth_year}, {common_birth_year}")
        else:
            print("Birth Year data is not available.")
    else:
        print("Birth Year column is not present in the dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))

def display_raw_data(df):
    """
    Display raw data from a DataFrame in chunks of five rows.

    Parameters:
    df (pd.DataFrame): The DataFrame to display raw data from.
    """
    i = 0
    raw = input("Do you want to see the raw data? Enter 'yes' or 'no': ").lower()

    pd.set_option('display.max_columns', 200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])  # Subset the DataFrame to display the next five rows
            raw = input("Do you want to see the next five rows? Enter 'yes' or 'no': ").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no': ").lower()


# In[ ]:

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

# In[ ]:
