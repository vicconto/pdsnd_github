import time
import pandas as pd
import numpy as np

#Dictionary for all data sources belonging to their respective country
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#Function to filter through the dataset with the input of the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Creating empty city variable to store the city name and converting the input later into lower letters to be case insensitive
    city = ''
    while city not in CITY_DATA.keys():
        print("\nPlease enter your City:")
        print("\n1.Chicago 2. New York City 3. Washington")
        print("\nPlease enter the full Name ; The Case is irrelevant.")
        city = input().lower()
        
        if city not in CITY_DATA.keys():
            print("\nPlease revise your Input and try again")
    
    print(f"\You have chosen {city.title()}.")


    #Creating a 'Month' Dictionary and story the input in the 'month' variable
    
    MONTH_DATA = {'january': 1,'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter your Month (From January to June or All):")
        print("\nPlease enter the full Name ; The Case is irrelevant")
        month = input().lower()
        
        if month not in MONTH_DATA.keys():
            print("\nPlease revise your Input and try again.")
    print(f"\n You have chosen {month.title()}.")
    
    # TO DO: get user input for day of week (all, monday, tuesday, ...) 
    #The same Procedure like for the Month Variable
    DAY_LIST = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    while day not in DAY_LIST:
        print("Please enter your day (From Monday to Sunday or All):")
        print("Please enter the full day ; The Case is irrelevant.")
        day = input().lower()
        
        if day not in DAY_LIST:
            print("Please revise your Input and try again.")
                  
    print(f"\n You have chosen {day.title()}.")
      

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
    print("\n Loading Data…")
    #So basically I am extracting the time (month, day) and filtering though it to get the Int Numbers for the later Output
    df = pd.read_csv(CITY_DATA[city])
    #Sorting all Data in efficent Time Frames
    df['Start Time'] = pd.to_datetime(df['Start Time'])
       
    df['month'] = df ['Start Time'].dt.month
       
    df['day_of_week'] = df['Start Time'].dt.weekday_name
       
    if month != 'all':
       
       months_clear_list = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months_clear_list.index(month) + 1
       
       df = df[df['month'] == month]

   
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]

       

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print(f"Most Popular Month: {popular_month}")

# TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day: {popular_day}")

 # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {popular_hour}")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    
    # TO DO: display most commonly used start station
    start_stat = df['Start Station'].mode()
    print("Most Commonly Used Start Station:", start_stat[0])

    # TO DO: display most commonly used end station
    end_stat = df['End Station'].mode()
    print("Most Commonly Used End Station:", end_stat[0])

    # TO DO: display most frequent combination of start station and end station trip
    for i in df:
        start_end_station = df['Start Station'] + "=" + df['End Station']
        start_end_station = start_end_station.mode()[0].split("=")
    print('Most Frequent Combination Of Start Station And End Station Trip:',   (start_end_station)[0],'To',(start_end_station)[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    
    By using the divmod function I can print the travel time in hours, minutes and seconds """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_duration = df['Trip Duration'].sum()
    
    minutes, seconds = divmod(total_travel_duration, 60)
    hour, minutes = divmod(minutes, 60)
    print(f"\nTotal Trip Duration in hours, minutes and seconds: {hour}, {minutes} and {seconds}")

    # TO DO: display mean travel time
    mean_travel_duration = df['Trip Duration'].mean()
    mins, sec = divmod(mean_travel_duration, 60)
    print(f"\nMean Travel Duration: {mean_travel_duration}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Types of users: {user_types}")

    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print(f"\nTypes of users by gender: {gender_type}")
    except:
        print(f"\nThere is no information about gender.")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()
        print(f"\nEarliest Birth Year: {earliest_birth}")
        print(f"\nRecent Birth Year: {recent_birth}")  
        print(f"\nCommon Birth Year: {common_birth}")
    except:
        print("No date of birth available.")
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    """Displays 5 rows of raw data from the original file for the applied filter.
    """
    USER_RESPONSE = ['yes', 'no']
    raw_data = ''
    count = 0
    while raw_data not in USER_RESPONSE:
        print("\nDo you wish to view the raw data? Enter Yes or No.")
        raw_data = input().lower()
        #the raw data from the df is displayed if user requests it
        if raw_data == "yes":
            print(df.head())
        elif raw_data not in USER_RESPONSE:
            print("\nPlease revise again your input.")

    #while loop to continuesly ask if the user wants to draw new raw data
    while raw_data == 'yes':
        print("Would you like to view 5 rows more raw data?")
        count += 5
        raw_data = input().lower()
   
        if raw_data == "yes":
             print(df[count:count+5])
        elif raw_data != "yes":
             break

    print('-'*40)
    
#Main Function Calls all Information we calculated
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