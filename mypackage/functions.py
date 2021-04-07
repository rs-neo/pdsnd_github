def get_month():
    """
    Asks user to specify a month to analyse.

    Returns:
        (str) month - name of the month to filter by
    """    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('\nWhich Month? {}?\n'.format(', '.join(months).title())).lower().strip()
        if month in months:
            break
    return month

def get_day():
    """
    Asks user to specify a day to analyse.

    Returns:
        (str) day - name of the day to filter by
    """    
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input('\nWhich day of the week? {}?\n'.format(', '.join(days).title())).lower().strip()
        if day in days:
            break
    return day


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """  
    month = "all"
    day = "all"
              
    while True:
        try:
            city = input('\n Which City\'s data would you like to analyse?\n Please type either Chicago, New York City or Washington:  ').lower().strip()
            if city in ['chicago', 'new york city','washington']:
                print('\nYou have picked {} for data analysis.\n'.format(city.capitalize()))
                break
        except:
            quit_system = input('Would you like to exit the program? Type \'Yes\' or \'No\' ').lower().strip()
            if quit_system == 'yes':
                quit()    
    while True:
        try:
            filters = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter.\n').lower().strip()
            if filters == 'none':
                break    
            elif filters == 'month':
                month = get_month()
                break
            elif filters == 'day':
                day = get_day()
                break
            elif filters == 'both':
                month = get_month()
                day = get_day()
                break  
        except:
            quit_system = input('Would you like to exit the program? Type \'Yes\' or \'No\' ').lower().strip()
            if quit_system == 'yes':
                quit()
    
    return city,month,day