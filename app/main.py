from datetime import datetime, timedelta
import time
import sys

#check if value given is valid
def validation(input_secs):
    return (input_secs != "0" and input_secs.isalpha() == False and input_secs.isnumeric() == True and len(input_secs) < 3 and len(input_secs) >= 1)

#take the current time and decrement with the given amount of secs
def back_clock(now, input_secs):
    try:
        input_secs = int(input_secs)
        new_clock = now - timedelta(seconds=input_secs)
        print("Clock Time:", format_clock(new_clock))
        time.sleep(input_secs)
        back_clock(new_clock, input_secs)
    except KeyboardInterrupt:
        print("Clock stopping...")
        sys.exit()

#format out clock with time only, removing other paremeters       
def format_clock(new_clock):
    new_clock_time = new_clock.strftime("%H:%M:%S")
    return new_clock_time

if __name__ == "__main__":
    try:
        input_secs = input("Please input number of seconds per decrement(1-99s):")
        if validation(input_secs) == True:
            print("Press 'cltr+c' to exit program")
            now = datetime.now()
            back_clock(now, input_secs)
        else:
            print("Invalid input. Please Try again")
            sys.exit()
    except KeyboardInterrupt:
        print("\nClock stopping...")
        sys.exit()