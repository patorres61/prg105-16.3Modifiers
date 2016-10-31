# Phyllis Torres
# 16.2 Time Assignment
# Due 11/10/2016

print('16.3 Modifiers Assignment\n')
print('Phyllis Torres\n\n')

print('This program will use a function that takes a given number of seconds and adds it to a time object. ')
print('The function returns the modified time object.')
# create a time class
# noinspection PyClassHasNoInit
class Time:
    """Represents the time of day
    attributes: hour, minute, second
    """

# create function to convert time to an integer
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

# create function to convert time to seconds
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

# create function to increment the time by the incremental number and return modified time
def increment(time, inc):
    time += inc
    return time

# create time1 object and populate the hour, minute, and second fields
# this object will be evaluated to determine if it follows time2
time = Time()
time.hour = 12
time.minute = 59
time.second = 55

print ('\nThe time to be incremented is ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

# call function to convert time to seconds
time.seconds = time_to_int(time)

inc_sec = raw_input('\nEnter the number of seconds to increment the time object by: ')

print ('\nThe amount time will be incremented by is: ' + str(inc_sec) + ' seconds.')

# call function to increment the time by the incremental
inc_seconds = increment(time.seconds, int(inc_sec))

# call function to convert seconds back to time format
timeNew = int_to_time(inc_seconds)

if timeNew.hour > 12:
    timeNew.hour -= 12

print ('\nThe incremented time is ' + '%.2d:%.2d:%.2d' % (timeNew.hour, timeNew.minute, timeNew.second))