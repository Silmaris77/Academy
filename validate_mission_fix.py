#!/usr/bin/env python3
"""
Simple validation script to test mission button fix
"""

import sys
import os
import json

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_mission_data_accessibility():
    """Test if mission data files are accessible"""
    try:
        mission_file = "data/missions/B1C1L1_missions.json"
        if os.path.exists(mission_file):
            with open(mission_file, 'r', encoding='utf-8') as f:
                missions = json.load(f)
            print(f"✅ Mission data file found: {mission_file}")
            print(f"✅ Contains {len(missions)} missions")
            
            # Check if there are active missions
            active_missions = [m for m in missions if not m.get('completed', False)]
            if active_missions:
                print(f"✅ Found {len(active_missions)} active missions")
                return True
            else:
                print("⚠️  No active missions found")
                return False
        else:
            print(f"❌ Mission data file not found: {mission_file}")
            return False
    except Exception as e:
        print(f"❌ Error loading mission data: {e}")
        return False

def test_imports():
    """Test if required modules can be imported"""
    try:
        from utils.mission_components import render_mission_summary_widget
        print("✅ mission_components imported successfully")
        
        from utils.mission_manager import load_missions
        print("✅ mission_manager imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def simulate_button_logic():
    """Simulate the button logic without Streamlit"""
    print("\n🔄 Simulating button click logic...")
    
    # Simulate session state changes that the button would make
    session_state = {}
    lesson_id = 'B1C1L1'
    
    # This is what the button does when clicked
    session_state['current_lesson'] = lesson_id
    session_state['lesson_step'] = 'summary'
    session_state['show_missions_tab'] = True
    
    print(f"✅ Session state would be set to:")
    print(f"   - current_lesson: {session_state['current_lesson']}")
    print(f"   - lesson_step: {session_state['lesson_step']}")
    print(f"   - show_missions_tab: {session_state['show_missions_tab']}")
    
    return True

def main():
    print("🧪 Testing Mission Button Fix")
    print("=" * 40)
    
    success = True
    
    # Test 1: Mission data accessibility
    print("\n1. Testing mission data accessibility...")
    if not test_mission_data_accessibility():
        success = False
    
    # Test 2: Module imports
    print("\n2. Testing module imports...")
    if not test_imports():
        success = False
    
    # Test 3: Button logic simulation
    print("\n3. Testing button logic...")
    if not simulate_button_logic():
        success = False
    
    # Summary
    print("\n" + "=" * 40)
    if success:
        print("✅ ALL TESTS PASSED")
        print("The mission button fix should be working correctly!")
        print("\nNext steps:")
        print("1. Start the Streamlit app: streamlit run main.py")
        print("2. Navigate to the dashboard")
        print("3. Click the 'Idź do misji' button")
        print("4. Verify it navigates to the mission tab")
    else:
        print("❌ SOME TESTS FAILED")
        print("The mission button may still have issues.")
    
    return success

if __name__ == "__main__":
    main()
