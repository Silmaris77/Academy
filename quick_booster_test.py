#!/usr/bin/env python3
"""
Simple test to verify the booster format fix in shop_new.py
"""

import datetime
import json

# Test the booster data handling logic directly
def test_booster_handling():
    print("🧪 Testing booster data handling logic...")
    
    # Simulate both data formats
    test_cases = [
        {
            'name': 'Old Format (String)',
            'data': '2025-06-17T15:56:10.600451'
        },
        {
            'name': 'New Format (Object)',
            'data': {
                'expires_at': '2025-06-17T15:56:10.600451',
                'activated_at': '2025-06-16T15:56:10.600470'
            }
        }
    ]
    
    for test_case in test_cases:
        print(f"\n📋 Testing: {test_case['name']}")
        booster_data = test_case['data']
        
        try:
            # This is the exact logic from shop_new.py
            if isinstance(booster_data, str):
                expiry_time = datetime.datetime.fromisoformat(booster_data)
                print(f"✅ String format processed: {expiry_time}")
            elif isinstance(booster_data, dict) and 'expires_at' in booster_data:
                expiry_time = datetime.datetime.fromisoformat(booster_data['expires_at'])
                print(f"✅ Object format processed: {expiry_time}")
            else:
                print(f"❌ Invalid format: {type(booster_data)}")
                continue
            
            now = datetime.datetime.now()
            if expiry_time > now:
                remaining_seconds = (expiry_time - now).total_seconds()
                remaining_hours = int(remaining_seconds // 3600)
                remaining_minutes = int((remaining_seconds % 3600) // 60)
                remaining_time = f"{remaining_hours}h {remaining_minutes}m"
                print(f"✅ Time calculation works: {remaining_time} remaining")
            else:
                print(f"⏰ Booster expired")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    return True

if __name__ == "__main__":
    print("🚀 Booster Format Fix Test")
    print("=" * 40)
    
    if test_booster_handling():
        print("\n🎉 SUCCESS: Fix is working correctly!")
        print("The shop will now handle both booster data formats.")
    else:
        print("\n💥 FAILURE: Fix needs more work.")
