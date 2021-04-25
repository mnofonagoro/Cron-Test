import sys
import os


def main():
    # Loops through every line in config.txt, and splits them into minute, hour and command    
    for schedule in sys.stdin:
        schedule_minute, schedule_hour, schedule_command = schedule.rstrip("\n").split(" ")
        
        if "run_me_daily" in schedule_command:
            return run_me_daily(schedule_minute, schedule_hour, schedule_command)
        
        elif "run_me_hourly" in schedule_command:
            return run_me_hourly(schedule_minute, schedule_command)
        
        elif "run_me_every_minute" in schedule_command:
            return run_me_every_minute(schedule_command)
        
        elif "run_me_sixty_times" in schedule_command:
            return run_me_sixty_times(schedule_hour, schedule_command)
        
        else:
            print("There is a line in this file that has a different command")
            os._exit(0)


def run_me_daily(schedule_minute, schedule_hour, schedule_command):
    # In this function, schedule_hour will always equal 1 (or 01)
    if schedule_minute == input_minute and schedule_hour.zfill(2) == input_hour.zfill(2):
        print("1:30 today - {}".format(schedule_command))
        
    elif int(input_minute) <= 29 and schedule_hour.zfill(2) == input_hour.zfill(2):
        print("1:30 today - {}".format(schedule_command))
        
    elif int(input_minute) >= 31 and schedule_hour.zfill(2) == input_hour.zfill(2):
        print("1:30 tomorrow - {}".format(schedule_command))
    
    elif int(schedule_hour) > int(input_hour):
        print("1:30 today - {}".format(schedule_command))
    
    elif int(schedule_hour) < int(input_hour):
        print("1:30 tomorrow - {}".format(schedule_command))
    
    else:
        print("There has been an error")
        
    return main()


def run_me_hourly(schedule_minute, schedule_command):
    # Here, schedule_minute will always equal 45
    if int(input_minute) <= int(schedule_minute):
        print("{}:45 today - {}".format(input_hour, schedule_command))
    
    elif int(input_minute) > int(schedule_minute):
        next_input_hour = int(input_hour) + 1
        if next_input_hour > 23:
            print("00:45 tomorrow - {}".format(schedule_command))
        else:
            print("{}:45 today - {}".format(next_input_hour, schedule_command))
    
    else:
        print("There has been an error")
    
    return main()


def run_me_every_minute(schedule_command):
    # Will always print put the current time
    print("{}:{} today - {}".format(input_hour, input_minute, schedule_command))
    
    return main()


def run_me_sixty_times(schedule_hour, schedule_command):
    # Schedule_hour will always be 19
    if int(schedule_hour) == int(input_hour):
        print("19:{} today - {}".format(input_minute, schedule_command))
    
    elif int(schedule_hour) > int(input_hour):
        print("19:00 today - {}".format(schedule_command))
    
    elif int(schedule_hour) < int(input_hour):
        print("19:00 tomorrow - {}".format(schedule_command))
    
    else:
        print("There has been an error")
    
    return main()


if __name__ == '__main__':
    # sys.argv are the command line arguments 
    # sys.argv[0] is the file name, so sys.argv[1] is the HH:MM input
    input_time = sys.argv[1]
    try:
        # Splitting time into hours and minutes, and catching input errors
        input_hour, input_minute = input_time.split(":")
        if int(input_hour) > 23:
            print("Hour value {} is out of range. Please enter a value between 00 and 23".format(input_hour))
        elif int(input_minute) > 59:
            print("Minute value {} is out of range. Please enter a value between 00 and 59".format(input_minute))
        elif len(input_minute) != 2:
            print("Please make sure that your minute value is 2 digits long, e.g. 00, 01, 02, etc.")
        else:
            main()
            print("Finished!")
    except ValueError:
        print("Please input the correct HH:MM format, e.g. 16:10")
        
    except Exception as e:
        print(e)
