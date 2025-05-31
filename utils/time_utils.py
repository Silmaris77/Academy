from datetime import datetime, timedelta
from typing import Optional

def calculate_relative_time(timestamp: str, current_time: Optional[datetime] = None) -> str:
    """
    Calculate relative time from a timestamp string.
    
    Args:
        timestamp: Timestamp string in format 'YYYY-MM-DD HH:MM:SS' or ISO format
        current_time: Current time to compare against (defaults to now)
    
    Returns:
        String describing relative time (e.g., "2 godziny temu", "1 dzień temu")
    """
    if current_time is None:
        current_time = datetime.now()
    
    try:
        # Parse the timestamp string
        if 'T' in timestamp:
            # ISO format
            target_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        else:
            # Standard format 'YYYY-MM-DD HH:MM:SS'
            target_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        
        # Calculate time difference
        time_diff = current_time - target_time
        
        # Return appropriate relative time string in Polish
        if time_diff.total_seconds() < 60:
            return "przed chwilą"
        elif time_diff.total_seconds() < 3600:  # Less than 1 hour
            minutes = int(time_diff.total_seconds() // 60)
            if minutes == 1:
                return "1 minutę temu"
            elif minutes < 5:
                return f"{minutes} minuty temu"
            else:
                return f"{minutes} minut temu"
        elif time_diff.total_seconds() < 86400:  # Less than 1 day
            hours = int(time_diff.total_seconds() // 3600)
            if hours == 1:
                return "1 godzinę temu"
            elif hours < 5:
                return f"{hours} godziny temu"
            else:
                return f"{hours} godzin temu"
        elif time_diff.days == 1:
            return "1 dzień temu"
        elif time_diff.days < 7:
            return f"{time_diff.days} dni temu"
        elif time_diff.days < 30:
            weeks = time_diff.days // 7
            if weeks == 1:
                return "1 tydzień temu"
            else:
                return f"{weeks} tygodni temu"
        elif time_diff.days < 365:
            months = time_diff.days // 30
            if months == 1:
                return "1 miesiąc temu"
            else:
                return f"{months} miesięcy temu"
        else:
            years = time_diff.days // 365
            if years == 1:
                return "1 rok temu"
            else:
                return f"{years} lat temu"
    
    except (ValueError, TypeError) as e:
        # If parsing fails, return a default string
        return "nieznany czas"

def get_current_timestamp() -> str:
    """
    Get current timestamp in the standard format used by the app.
    
    Returns:
        Current timestamp string in format 'YYYY-MM-DD HH:MM:SS'
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_current_iso_timestamp() -> str:
    """
    Get current timestamp in ISO format.
    
    Returns:
        Current timestamp string in ISO format
    """
    return datetime.now().isoformat()
