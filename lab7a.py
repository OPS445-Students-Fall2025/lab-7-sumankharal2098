#!/usr/bin/env python3
# Student ID: [seneca_id]
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum as a Time object"""
    sum_time = Time()
    
    # Add hours, minutes, seconds
    sum_time.second = t1.second + t2.second
    sum_time.minute = t1.minute + t2.minute
    sum_time.hour   = t1.hour + t2.hour

    # Normalize seconds to minutes
    sum_time.minute += sum_time.second // 60
    sum_time.second = sum_time.second % 60

    # Normalize minutes to hours
    sum_time.hour += sum_time.minute // 60
    sum_time.minute = sum_time.minute % 60

    # If you want to stay within 24 hours (optional)
    sum_time.hour = sum_time.hour % 24

    return sum_time

