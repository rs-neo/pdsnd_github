import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']  == month]
     
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']  == day.capitalize()]    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    s = df['month'].value_counts()
    print('Most popular month       : {}, with a Count of:{}'.format(months[s.index[0]-1].title(),s[s.index[0]]))
    # display the most common day of week
    s = df['day_of_week'].value_counts()
    print('Most popular Day of Week : {}, with a Count of:{}'.format(s.index[0],s[s.index[0]]))
    # display the most common start hour
    s = df['hour'].value_counts()
    print('Most popular Hour        : {}, with a Count of:{}'.format(s.index[0],s[s.index[0]]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    s = df['Start Station'].value_counts()
    print('Most popular station :\n{}, with a Count of : {}'.format(s.index[0],s[s.index[0]]))
    # display most commonly used end station
    s = df['End Station'].value_counts()
    print('Most popular end station :\n{}, with a Count of : {}'.format(s.index[0],s[s.index[0]]))
    # display most frequent combination of start station and end station trip
    s = df.groupby(['Start Station','End Station']).size().reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).head(1)
    print('Most Popular Trip:\n{} to {}, with a Count of : {}'.format(s['Start Station'].values[0],s['End Station'].values[0],s['count'].values[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    s = df['Trip Duration'].sum()
    print(f"Total duration : {s}\nCount : {df['Trip Duration'].count()}\nAverage duration : {df['Trip Duration'].mean()}")
    # display mean travel time
    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nUser Type Stats:')
    try:
       s = df['User Type'].value_counts().rename_axis('Types').reset_index(name='Count')
       usertype = s['Types'].values.tolist()
       usertype_count = s['Count'].values.tolist()
       for x in range(len(usertype)):
           print('{} : {}'.format(usertype[x],usertype_count[x]))
        
    except:
        print('Sorry, Not available for this city')
    
    # Display counts of gender
    print('\nGender stats:')
    try:
        s = df['Gender'].value_counts().rename_axis('Gender').reset_index(name='Count')
        gender = s['Gender'].values.tolist()
        gender_count = s['Count'].values.tolist()
        for x in range(len(gender)):
            print('{} : {}'.format(gender[x],gender_count[x]))
        
    except:
        print('Sorry, Not available for this city')

    # Display earliest, most recent, and most common year of birth
    print('\nBirth year stats:')
    try:
        e_year = int(df['Birth Year'].min())
        r_year = int(df['Birth Year'].max())
        c_year = int(df['Birth Year'].mean())
        print('Earliest Year of birth : {}\nMost recent Year of birth : {}\nAverage Year of birth : {}'.format(e_year, r_year, c_year))
    except:
        print('Sorry, Not available for this city')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Displays records (5) at a time."""
    
    # Display 5 raw records at a time, until user quits or end-of-file reached
    # Get rid of data we have generated
    df = df.drop(['month','day_of_week','hour'],axis=1)
    data_dict = df.to_dict('records')
    view_more = 'yes'
    count = 0
    end_count = len(data_dict)
    print('\n')
    while view_more == 'yes':
        # check for end-of-records
        count += 5
        if end_count < count:
            count = end_count
        for x in range(count-5,count):
            print(json.dumps(data_dict[x], default = str,  indent=4))
        #Check if user want to see 5 more records    
        view_more = input('\nWould you like would like to see 5 more rows of the data? Type \'Yes\' or \'No\'').lower().strip()
        while view_more not in ['yes','no']:
            view_more = input('\nWould you like would like to see 5 more rows of the data? Type \'Yes\' or \'No\'').lower().strip()
        if view_more == 'no':
            break
        #if view_more != 'yes':
        #    break
    
    print('-'*40)