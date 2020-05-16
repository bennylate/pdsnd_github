#Import libraries
import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv' }

 
#Begin function definitions
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print()

#TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#Get a city name from the user, return something to the user showing the selection and break if they enter something other than the city names

    city_input = input('Please choose the city in which you\'re interested.\nChicago \nNew York City \nWashington D.C.\n')
    
    while True:
        if city_input == 'chicago':
            print('\nSweet home, Chicago\n')
            break
        elif city_input == 'new york':
            print('\nNew York, New York\n')
            break
        elif city_input == 'washington':
            print('\nOur Capitol it is\n')
            break
        else:
            print('\nI didn\'t recognize your choice, please try again\n')
            continue
# Note, .lower here makes sure the input is translated into a case agnostic format as CITY_DATA             
    city = city_input.lower()

# TO DO: get user input for month (all, january, february, ... , june)
# Creating a dictionary so the user can enter the month name and then we translate to the integer as that's what will be in the dataset

    month_input = input('\nWhich month would you like to use as a filter? January, February, March, April, May, June, or All?\n')  
    month_dict = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'all':7}
    while month_input.lower() in month_dict.keys():
        print('\nYou\'ve chosen:',month_input.lower())
        break
        if month_input.lower() not in month_dict.keys():
            print('\nI didn\'t catch that.  Please try again')
            continue
    month = month_dict[month_input.lower()]
            
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
# Using a dictionary like month_input and the user input is checked against the keys for the integer to match in the date/time breakout from the data upload

    day_input = input('If you would like a particular day of week please choose from the following \nSunday \nMonday \nTuesday \nWednesday \nThursday \nFriday \nSaturday \nAll\n')
    day_dict = {'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':7, 'all':8}
    while day_input.lower() in day_dict.keys():
        print('\nYou\'ve chosen:',day_input.lower())
        break
        if day_input.lower() not in day_dict.keys():
            print('I didn\'t catch that.  Please try again')
            continue
    day = day_dict[day_input.lower()]
    
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
 
# Using pandas accessor to find month, day, hour from the Start Time column in the source data
    print("A moment please while I find the data....\n")
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month: ',popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most popular day: ",popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most popular hour: \n",popular_hour)
    
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most common place to start: ",common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most common place to end:",common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_combo = (df['Start Station']+"||"+df['End Station']).mode()[0]
    print("The most frequently used station combination: ",str(common_combo.split("||")))

    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time was:",str(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The average travel time was:",str(mean_time))

    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print("These are the user types requested: ",user_type)

    # TO DO: Display counts of gender
    gender = df["Gender"].value_counts()
    print("These are the genders requested: ",gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    early_year = df["Birth Year"].min()
    print("The earliest year of birth for this filtered set is: ", int(early_year))
    
    recent_year = df["Birth Year"].max()
    print("The most recent year of birth for this set is: ",int(recent_year))
    
    common_year = df["Birth Year"].mode()
    print("The most common year of birth is: ",int(common_year))
    print('-'*40)

def show_data(df):
    'Shows raw data, five lines at a time, continues til the user stops'
# Using current_line to establish place in data and iterate by 5
    start = 0
    end = 5
    sd_input = input('\nWould you like to see 5 lines of the raw data? Y or N, please.\n')
    sd_input = sd_input.lower()
    if sd_input.lower() == 'y':
        while True:
            print(df.iloc[start:end])
            start += 5
            end += 5
            sec_input = input('\nWould you like 5 more rows?\n')
            sec_input = sec_input.lower()
            if sec_input == 'n' or sec_input == 'no':
                break
 
    print('-'*40)                
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Please enter Yes or No.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    