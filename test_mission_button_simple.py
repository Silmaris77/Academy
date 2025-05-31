#!/usr/bin/env python3
"""
Simple test to verify mission button functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.mission_components import render_mission_summary_widget
from utils.mission_manager import mission_manager

# Test basic functionality
print("🔧 Testing Mission Button Functionality")
print("=" * 50)

# Test 1: Check if mission_manager can load data
print("\n1. Testing mission data loading...")
try:
    summary = mission_manager.get_lesson_mission_summary('testuser', 'B1C1L1')
    print(f"✅ Mission data loaded successfully!")
    print(f"   - Summary keys: {list(summary.keys())}")
    print(f"   - Completed missions: {summary.get('completed', 0)}")
    print(f"   - Total missions: {summary.get('total', 0)}")
except Exception as e:
    print(f"❌ Error loading mission data: {str(e)}")
    import traceback
    traceback.print_exc()

# Test 2: Check username parameter issue
print("\n2. Testing username parameter...")
test_username = 'testuser'
print(f"   - Testing with username: '{test_username}'")

# Test 3: Check if mission files exist
print("\n3. Checking mission files...")
mission_file = "data/missions/B1C1L1_missions.json"
if os.path.exists(mission_file):
    print(f"✅ Mission file exists: {mission_file}")
    import json
    with open(mission_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"   - Mission data structure: {list(data.keys())}")
else:
    print(f"❌ Mission file not found: {mission_file}")

print("\n" + "=" * 50)
print("Test completed!")
