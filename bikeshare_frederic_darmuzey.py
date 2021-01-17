import time
import pandas as pd
import numpy as np

# our datasets

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# lists of accepted month and day values

dataset_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all', 'nomonth']
dataset_days_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all', 'noday']


def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). Use a while loop to handle invalid inputs

    city=input(
        '\nPlease enter the name of one of these cities to see their related data >> Chicago, New York City or Washington:\n') # ask for user input
       
    while city.lower() not in CITY_DATA:   # loop that we activate if user input is not in city data
        print('\nThere\'s no data for the city you chose! We only have data for Chicago, New York City or Washington.')
        city=input('\nPlease enter the name of one of these cities to see their related data:\n')
    
    if city.lower() in CITY_DATA: # conditional statement: if user input is in city data, print the message below
        print('\nGreat! You chose to see data from ' + city + '.')
        
    # get user to choose month, week or both

    time_input= ['month', 'day', 'both']   # list of possible user time inputs.
    
    time_data=input(
        '\nPlease enter month if you want to see monthly data, day if you want to see daily data or both if you want both monthly and daily data.\n')
    
    while time_data.lower() not in time_input:   # loop that we activate if user input is not in time_input list.
        print('\nYou did not select a valid option.')
        time_data=input('\nPlease enter month, day or both depending on the bikeshare time data you want to access for ' + city+':\n')
        
    if time_data.lower() in time_input: # conditional statement: if user input is in time_input, print one of the messages below
        if time_data.lower() == 'both':
            print("\nGreat! You chose to see both monthly and daily data. Let's go for it!\n")
        
            # get user input for month (all, january, february, ... , june)

            month = input(
                "\nPlease enter the month name (January-June) you would like to analyze or enter 'all' to analyze the data from January to June:\n")
            while month.lower() not in dataset_months:
                print('\nThis is not a recognized month value.')
                month = input("\nEnter the correct month to analyze (from January until June) or enter 'all' to analyze everything:\n")

            # get user input for day of week (all, monday, tuesday, ... sunday)
       
            day = input(
                "\nPlease enter the name of the day of the week (Sunday-Saturday) you want to analyze or enter 'all' to analyze the data from Sunday to Saturday:\n")
            while day.lower() not in dataset_days_week:
                print('\nThis is not a recognized day of the week.')
                day = input(
                    "\nEnter the correct day to analyze (between Sunday until Saturday) or enter 'all' to analyze everything:\n")
            
            print(
                "\nYou chose to see bikeshare data for " + day + " and " + month + " in " + city + " out of all available days and months. Let's roll it out!!\n")
            
        elif time_data.lower() == 'month':  
            print('\nExcellent! You chose to see bikeshare data of ' + city + ' by ' + time_data + ". Let's go for it!\n")
        
            # get user input for month (all, january, february, ... , june)
            
            month = input(
                "\nPlease enter the month name (January-June) you would like to analyze or enter 'all' to analyze the data from January to June:\n")
            while month.lower() not in dataset_months:
                print('\nThis is not a recognized month value.')
                month = input("\nEnter the correct month to analyze (from January until June) or enter 'all' to analyze everything:\n")
            
            day = dataset_days_week[8] 
        
            print(
                "\nYou chose to see bikeshare data for " + month + " in " + city + " out of all available months. Let's roll it out!!\n")
        
        else:
            print('\nExcellent! You chose to see bikeshare data of ' + city + ' by ' + time_data + ". Let's go for it!\n")
        
            # get user input for day of week (all, monday, tuesday, ... sunday)

            day = input(
                 "\nPlease enter the name of the day of the week (Sunday-Saturday) you want to analyze or enter 'all' to analyze the data from Sunday to Saturday:\n")
            while day.lower() not in dataset_days_week:
                print('\nThis is not a recognized day of the week.')
                day = input(
                    "\nEnter the correct day to analyze (between Sunday until Saturday) or enter 'all' to analyze everything:\n")
        
            month = dataset_months[7]
            
            print(
            "\nYou chose to see bikeshare data for " + day + " in " + city + " out of all available days. Let's roll it out!!\n")


    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter or "nomonth" for only day filtering
        (str) day - name of the day of week to filter by, or "all" to apply no day filter or "noday" for only month filtering
    
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day or just day or just month
    """
    try:
        # load data file into a dataframe
        
        df = pd.read_csv(CITY_DATA[city])
        
        # convert the Start Time column to datetime
        
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
        
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()

        # filter by month if applicable
        
        if(month != 'nomonth' and month != 'all'):  # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1

            # filter by month to create the new dataframe
            
            df = df[df['month'] == month]
            
        elif month == 'nomonth':    
            
            # drop the month column
            
            df = df.drop(['month'], axis=1)
        
        else: 
             df = df
        
        
        # filter by day of week if applicable
        
        if(day != 'noday' and day != 'all'):  # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
            
        elif day == 'noday':
            
            # drop the day column
            
            df = df.drop(['day_of_week'], axis=1)
            
        else:
            df = df
            
        return df
    
    except ValueError as e:
        print(e.args)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    try: 

        # display the most common month
        
        if 'month' not in df:  # warn the user they chose not to see any monthly data if applicable
            raise Exception("You chose not to select any data related to months.")
        
        print('\nThe most frequent month is ', df['month'].value_counts().idxmax())

    except Exception as e:
        print(e)
    
    try:
        
        # display the most common day of week
        
        if 'day_of_week' not in df:  # warn the user they chose not to see any daily data if applicable
             raise Exception("\nYou chose not to select any data related to days.")
         
        print('\nThe most frequent day is ', df['day_of_week'].value_counts().idxmax())
         
    except Exception as e:
        print(e)
    
    try:

        # extract hour from the Start Time column to create an hour column
        
        df['hour'] = df['Start Time'].dt.hour

        # find the most common hour (from 0 to 23)
       
        popular_hour = df.mode()['hour'][0]
        
        # display the most common start hour
        
        print('\nThe most frequent start hour is ', popular_hour)
        
    except ValueError as e:
        print(e.args)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    try:
        
        # display most commonly used start station
    
        print('\nThe most commonly used start station is ', df.mode()['Start Station'][0])

        # display most commonly used end station
        
        print('\nThe most commonly used end station is ', df.mode()['End Station'][0])
        
        # display most frequent combination of start station and end station trip

        print(
            '\nThe most common combinations of stations are ', df.groupby(['Start Station', 'End Station']).size().idxmax())

    except Exception as e:
        pass
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    try:
        
        # display total travel time
        
        print('\nThe total travel time is ', sum(df['Trip Duration']))

        # display mean travel time
        
        print('\nThe mean travel time is ', df.loc[:, "Trip Duration"].mean())
    
    except (Exception, ValueError) as e:
        print(e.args)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    try:
        
        # Display counts of user types
        
        if 'User Type' not in df: # warn user there is no information about user type if applicable
            raise Exception("No User Type data")
        
        print('\nType of users:', df['User Type'].value_counts())
        
    except Exception as e:
        print(e)   
     
    try:
           
        # Display counts of gender
        
        if 'Gender' not in df: # warn user there is no information about gender if applicable
            raise Exception("\nNo Gender data")
        
        print('\nUsers split by gender:', df['Gender'].value_counts())
    
    except Exception as e:
        print(e)   
    
    try:
        
        # Display earliest, most recent, and most common year of birth
        
        print('\nThe earlier Birth Year is ', int(df['Birth Year'].min()))
        print('\nThe most recent Birth Year is ', int(df['Birth Year'].max()))
        print('\nThe most common Birth Year is ', int(df.mode()['Birth Year'][0]))
    
    except Exception:
        print("\nUnable to calculate birth data. Birth column seems to be missing.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_first_rows(df):
    
    """
        Displays filtered data - 10 first rows depending on user input.
        
        Args:
            (str) df - pandas DataFrame with the filtered data from the load_data function.
    """
    
    print('\nDisplaying 10 first data rows...\n')
    start_time = time.time()
    
    display=True
    user_answer=['yes','no']
    
    while display:
        display = input('\nWould you like to print the 10 first rows of the dataframe? Enter yes or no.\n')
        while display.lower() not in user_answer:
            display = input(
                '\nPlease enter a valid answer. Would you like to print 10 rows? Enter yes or no.\n')
        if display.lower() != 'yes':
            break
        else:
            print(df.head(10))
            break
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_first_rows(df)
        
        restart_input=['yes','no']
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() not in restart_input:
            restart = input("\nPlease enter a correct input: 'yes' for restart, 'no' to end the program.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
    