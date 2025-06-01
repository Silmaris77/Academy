#!/usr/bin/env python3
"""
Time utility functions for ZenDegenAcademy
Provides Polish relative time calculation and timestamp handling
"""

from datetime import datetime
import re


def get_current_timestamp():
    """
    Get current timestamp in ISO format
    
    Returns:
        str: Current timestamp in 'YYYY-MM-DD HH:MM:SS' format
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def calculate_relative_time(timestamp_str):
    """
    Calculate relative time in Polish from a timestamp string
    
    Args:
        timestamp_str (str): Timestamp in 'YYYY-MM-DD HH:MM:SS' format
        
    Returns:
        str: Polish relative time string (e.g., "2 godziny temu", "1 dzień temu")
    """
    if not timestamp_str:
        return "niedawno"
    
    try:
        # Parse timestamp
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        
        # Calculate time difference
        diff = now - timestamp
        total_seconds = int(diff.total_seconds())
        
        # Handle future timestamps (shouldn't happen, but just in case)
        if total_seconds < 0:
            return "niedawno"
        
        # Less than 1 minute
        if total_seconds < 60:
            return "przed chwilą"
        
        # Minutes
        minutes = total_seconds // 60
        if minutes < 60:
            if minutes == 1:
                return "1 minutę temu"
            elif minutes < 5:
                return f"{minutes} minuty temu"
            else:
                return f"{minutes} minut temu"
        
        # Hours
        hours = minutes // 60
        if hours < 24:
            if hours == 1:
                return "1 godzinę temu"
            elif hours < 5:
                return f"{hours} godziny temu"
            else:
                return f"{hours} godzin temu"
        
        # Days
        days = hours // 24
        if days < 30:
            if days == 1:
                return "1 dzień temu"
            else:
                return f"{days} dni temu"
        
        # Months
        months = days // 30
        if months < 12:
            if months == 1:
                return "1 miesiąc temu"
            elif months < 5:
                return f"{months} miesiące temu"
            else:
                return f"{months} miesięcy temu"
        
        # Years
        years = months // 12
        if years == 1:
            return "1 rok temu"
        elif years < 5:
            return f"{years} lata temu"
        else:
            return f"{years} lat temu"
            
    except (ValueError, TypeError) as e:
        # If timestamp parsing fails, return fallback
        return "niedawno"


def format_timestamp_display(timestamp_str):
    """
    Format timestamp for display in Polish format
    
    Args:
        timestamp_str (str): Timestamp in 'YYYY-MM-DD HH:MM:SS' format
        
    Returns:
        str: Formatted date string (e.g., "7 grudnia 2024, 15:30")
    """
    if not timestamp_str:
        return "Nieznana data"
    
    try:
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        
        # Polish month names
        months = [
            "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
            "lipca", "sierpnia", "września", "października", "listopada", "grudnia"
        ]
        
        day = timestamp.day
        month = months[timestamp.month - 1]
        year = timestamp.year
        hour = timestamp.hour
        minute = timestamp.minute
        
        return f"{day} {month} {year}, {hour:02d}:{minute:02d}"
        
    except (ValueError, TypeError):
        return "Nieznana data"


def is_recent_timestamp(timestamp_str, hours=1):
    """
    Check if timestamp is recent (within specified hours)
    
    Args:
        timestamp_str (str): Timestamp in 'YYYY-MM-DD HH:MM:SS' format
        hours (int): Number of hours to consider as "recent"
        
    Returns:
        bool: True if timestamp is recent, False otherwise
    """
    if not timestamp_str:
        return False
    
    try:
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        
        diff = now - timestamp
        return diff.total_seconds() <= (hours * 3600)
        
    except (ValueError, TypeError):
        return False


def get_time_of_day():
    """
    Get current time of day in Polish
    
    Returns:
        str: Time of day ("rano", "po południu", "wieczorem", "w nocy")
    """
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "rano"
    elif 12 <= current_hour < 18:
        return "po południu"
    elif 18 <= current_hour < 22:
        return "wieczorem"
    else:
        return "w nocy"
