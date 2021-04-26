# Lyst Cron Test

## Specification
There are a set of tasks, each running at least daily, which are scheduled using some simple values in a text file.

The scheduler config:
```
30 1 /bin/run_me_daily
45 * /bin/run_me_hourly
* * /bin/run_me_every_minute
* 19 /bin/run_me_sixty_times
```

The first field is the minute past the hour, the second field is the hour of the day and the third is the command to run. For both cases * means that it should run for all values of that field. In the above example run_me_daily has been set to run at 1:30am every day and run_me_hourly at 45 minutes past the hour every hour. The fields are whitespace separated and each entry is on a separate line.

The task is to write a command line program that takes a single argument. This argument is the simulated 'current time' in the format HH:MM. The program should accept config lines in the form above to **STDIN** and output the soonest time at which each of the commands will fire and whether it is today or tomorrow. In the case when the task should fire at the simulated 'current time', then that is the time the program should output, not the next one.

For example, `python app.py 16:10 < config` will output:
```
1:30 tomorrow - /bin/run_me_daily 
16:45 today - /bin/run_me_hourly
16:10 today - /bin/run_me_every_minute 
19:00 today - /bin/run_me_sixty_times
```
## Running The Program
### From the zip file
* Unzip the file
* `cd` into `Lyst` if you're not already in the root of the project
* Depending on the version of Python you have, use the command `python`, `python3` or `py` to run the `app.py` script:
    * For example, `python app.py 16:10 < config`
    * You can enter any time between 00:00 and 23:59
### From GitHub
* Clone the repo
* `cd` into `Cron-Test` if you're not already in the root of the project
* Depending on the version of Python you have, use the command `python`, `python3` or `py` to run the `app.py` script:
    * For example, `python app.py 16:10 < config`
    * You can enter any time between 00:00 and 23:59

## If I Had More Time
* Create more consistency when printing the hour (e.g. depending on user input, the program will output 09:45 or 9:45)
* Improve error handling + remove any unnecessary print statements
* Refactor: put lines 97 - 107 in its own function
* Unit test each function