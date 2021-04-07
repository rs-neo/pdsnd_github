from mypackage import *

def main():
    while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)            
            # External functions for statistical analytics           
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            # External function, diplay 5 records at a time
            raw_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
            while restart not in ['yes','no']:
                restart = input('\nWould you like to restart? Enter yes or no. ').lower().strip()
            if restart == 'no':
                quit()
        
if __name__ == "__main__":
    main()