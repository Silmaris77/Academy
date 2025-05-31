#!/usr/bin/env python3
"""
Simple test for time utilities
"""

import sys
import os
sys.path.append('.')

def simple_time_test():
    """Simple test of time functions"""
    print("Testing time utilities...")
    
    try:
        from utils.time_utils import calculate_relative_time, get_current_timestamp
        
        # Test current timestamp
        current = get_current_timestamp()
        print(f"Current timestamp: {current}")
        
        # Test relative time
        test_cases = [
            "2024-01-01 12:00:00",
            "2025-05-30 12:00:00", 
            current
        ]
        
        for timestamp in test_cases:
            relative = calculate_relative_time(timestamp)
            print(f"{timestamp} -> {relative}")
        
        print("Time utilities test passed!")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    simple_time_test()
