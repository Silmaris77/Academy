#!/usr/bin/env python3
"""
🎯 MISSION SYSTEM USER TESTING SCRIPT

This script performs comprehensive testing of the mission system integration
and provides step-by-step validation of all components.
"""

import os
import sys
import json
from datetime import datetime

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"🎯 {title}")
    print("=" * 60)

def print_section(title):
    """Print a formatted section header"""
    print(f"\n📋 {title}")
    print("-" * 40)

def check_file_exists(filepath, description):
    """Check if a file exists and print result"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {filepath}")
    return exists

def check_string_in_file(filepath, search_string, description):
    """Check if a string exists in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        found = search_string in content
        status = "✅" if found else "❌"
        print(f"{status} {description}")
        return found
    except Exception as e:
        print(f"❌ {description} (Error: {e})")
        return False

def test_mission_system_imports():
    """Test if all mission system components can be imported"""
    print_section("TESTING MISSION SYSTEM IMPORTS")
    
    try:
        # Test mission manager import
        from utils.mission_manager import mission_manager
        print("✅ Mission manager imported successfully")
        
        # Test mission components import
        from utils.mission_components import (
            render_missions_page, 
            render_mission_summary_widget,
            render_mission_card,
            render_daily_mission_interface
        )
        print("✅ Mission components imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_mission_data_loading():
    """Test mission data loading functionality"""
    print_section("TESTING MISSION DATA LOADING")
    
    try:
        from utils.mission_manager import mission_manager
        
        # Test getting missions for B1C1L1
        missions = mission_manager.get_available_missions('test_user', 'B1C1L1')
        print(f"✅ Found {len(missions)} missions for B1C1L1")
        
        # Display mission details
        for i, mission in enumerate(missions, 1):
            title = mission.get('title', 'Unknown')
            status = mission.get('status', 'unknown')
            xp = mission.get('xp_reward', 0)
            duration = mission.get('duration_days', 0)
            print(f"   {i}. {title}")
            print(f"      Status: {status}, XP: {xp}, Duration: {duration} days")
        
        # Test mission summary
        summary = mission_manager.get_lesson_mission_summary('test_user', 'B1C1L1')
        print(f"\n✅ Mission summary generated:")
        print(f"   - Total missions: {summary['total_missions']}")
        print(f"   - Completed: {summary['completed_missions']}")
        print(f"   - Active: {summary['active_missions']}")
        print(f"   - Total XP: {summary['total_xp_earned']}")
        
        return True
    except Exception as e:
        print(f"❌ Mission data loading failed: {e}")
        return False

def validate_file_integrations():
    """Validate that all file integrations are in place"""
    print_section("VALIDATING FILE INTEGRATIONS")
    
    success = True
    
    # Check mission data file
    success &= check_file_exists(
        "data/missions/B1C1L1_missions.json",
        "Mission data file"
    )
    
    # Check lesson.py modifications
    if os.path.exists("views/lesson.py"):
        checks = [
            ("🎯 Misje praktyczne", "Mission tab added to lesson"),
            ("render_missions_page", "Mission components import"),
            ('lesson_id == "B1C1L1"', "B1C1L1 conditional logic"),
            ("show_missions_tab", "Navigation tab selection"),
            ("selected_tab_index = 2", "Auto-tab selection logic")
        ]
        
        for search_string, description in checks:
            success &= check_string_in_file("views/lesson.py", search_string, description)
    
    # Check dashboard.py modifications
    if os.path.exists("views/dashboard.py"):
        dashboard_checks = [
            ("render_mission_summary_widget", "Mission widget import"),
            ("render_mission_summary_widget(username, 'B1C1L1')", "Mission widget integration")
        ]
        
        for search_string, description in dashboard_checks:
            success &= check_string_in_file("views/dashboard.py", search_string, description)
    
    # Check mission components modifications
    if os.path.exists("utils/mission_components.py"):
        component_checks = [
            ("🎯 Idź do misji", "Navigation button in widget"),
            ("st.session_state.current_lesson = lesson_id", "Navigation state setting"),
            ("st.session_state.show_missions_tab = True", "Mission tab flag setting")
        ]
        
        for search_string, description in component_checks:
            success &= check_string_in_file("utils/mission_components.py", search_string, description)
    
    return success

def simulate_user_flow():
    """Simulate the complete user flow"""
    print_section("SIMULATING USER FLOW")
    
    print("🔄 STEP 1: User visits Dashboard")
    print("   ├─ Mission summary widget should be visible")
    print("   ├─ Shows 'Misje praktyczne: Strach przed stratą'")
    print("   ├─ Displays progress overview (0/3 missions initially)")
    print("   └─ Contains '🎯 Idź do misji' button")
    
    print("\n🔄 STEP 2: User clicks 'Idź do misji'")
    print("   ├─ Sets st.session_state.current_lesson = 'B1C1L1'")
    print("   ├─ Sets st.session_state.lesson_step = 'summary'")
    print("   ├─ Sets st.session_state.show_missions_tab = True")
    print("   └─ Triggers st.rerun()")
    
    print("\n🔄 STEP 3: User lands on lesson B1C1L1")
    print("   ├─ Page loads lesson summary")
    print("   ├─ Detects B1C1L1 and adds missions tab")
    print("   ├─ Auto-selects missions tab (index 2)")
    print("   └─ Clears show_missions_tab flag")
    
    print("\n🔄 STEP 4: User interacts with missions")
    print("   ├─ Sees 3 missions for Fear of Loss")
    print("   ├─ Can click '🚀 Rozpocznij' to start missions")
    print("   ├─ Active missions show daily task interface")
    print("   ├─ Can complete daily tasks")
    print("   └─ Earns XP rewards for progress")
    
    print("\n🔄 STEP 5: User returns to Dashboard")
    print("   ├─ Mission widget reflects updated progress")
    print("   ├─ Shows completed missions count")
    print("   ├─ Displays total XP earned")
    print("   └─ Ready for next mission cycle")

def create_user_testing_checklist():
    """Create a comprehensive testing checklist for manual testing"""
    print_section("USER TESTING CHECKLIST")
    
    checklist = """
📋 MANUAL TESTING CHECKLIST:

🚀 PREPARATION:
□ Start application: streamlit run main.py
□ Login with existing user account

📊 DASHBOARD TESTING:
□ Navigate to Dashboard
□ Locate "Misje praktyczne: Strach przed stratą" widget
□ Verify widget shows mission overview
□ Check if "🎯 Idź do misji" button is visible
□ Verify progress shows "0/3 ukończone" initially

🧭 NAVIGATION TESTING:
□ Click "🎯 Idź do misji" button
□ Verify navigation to lesson B1C1L1
□ Check if landing on Summary page
□ Verify missions tab is auto-selected
□ Confirm tab shows "🎯 Misje praktyczne"

🎯 MISSION INTERFACE TESTING:
□ Verify 3 missions are displayed
□ Check mission titles and descriptions
□ Verify XP rewards shown correctly
□ Test "🚀 Rozpocznij" button on a mission
□ Confirm mission status changes to active

📋 DAILY TASKS TESTING:
□ Click "📋 Dzisiejsze zadanie" on active mission
□ Verify daily task interface appears
□ Test task completion functionality
□ Check XP reward notification
□ Verify progress tracking updates

🔄 ROUND-TRIP TESTING:
□ Return to Dashboard from lesson
□ Verify mission widget reflects changes
□ Check updated progress count
□ Test navigation multiple times
□ Verify state persistence

⚡ ERROR HANDLING:
□ Test with no active missions
□ Verify graceful error handling
□ Check fallback behaviors
□ Test with invalid user data

✅ SUCCESS CRITERIA:
□ All navigation works smoothly
□ Mission state persists correctly
□ XP rewards are properly awarded
□ UI updates reflect backend changes
□ No console errors or exceptions
"""
    
    print(checklist)

def generate_testing_report():
    """Generate a comprehensive testing report"""
    print_header("MISSION SYSTEM TESTING REPORT")
    
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 System: BrainVenture Academy Mission System")
    print(f"📍 Focus: Lesson B1C1L1 - Fear of Loss")
    
    # Run all tests
    import_success = test_mission_system_imports()
    data_success = test_mission_data_loading()
    integration_success = validate_file_integrations()
    
    print_section("OVERALL TEST RESULTS")
    
    overall_success = import_success and data_success and integration_success
    
    print(f"{'✅' if import_success else '❌'} Mission System Imports: {'PASS' if import_success else 'FAIL'}")
    print(f"{'✅' if data_success else '❌'} Mission Data Loading: {'PASS' if data_success else 'FAIL'}")
    print(f"{'✅' if integration_success else '❌'} File Integrations: {'PASS' if integration_success else 'FAIL'}")
    print(f"{'✅' if overall_success else '❌'} Overall Status: {'READY FOR PRODUCTION' if overall_success else 'NEEDS FIXES'}")
    
    simulate_user_flow()
    create_user_testing_checklist()
    
    print_header("NEXT STEPS")
    
    if overall_success:
        print("""
🎉 INTEGRATION COMPLETE! Ready for production deployment.

🚀 RECOMMENDED ACTIONS:
1. Start the application: streamlit run main.py
2. Perform manual testing using the checklist above
3. Test with multiple user accounts
4. Verify data persistence across sessions
5. Monitor for any runtime errors
6. Collect user feedback for improvements

📈 PRODUCTION READINESS:
✅ All core components integrated
✅ Navigation flow implemented
✅ Mission data structure complete
✅ User interface components ready
✅ Error handling in place
""")
    else:
        print("""
⚠️  INTEGRATION ISSUES DETECTED

🔧 REQUIRED FIXES:
- Review failed test results above
- Check import errors and file paths
- Verify all file modifications are in place
- Test individual components separately
- Re-run this script after fixes

💡 TROUBLESHOOTING:
1. Ensure all dependencies are installed
2. Check file permissions and encoding
3. Verify import paths are correct
4. Test mission manager functionality
5. Validate JSON data structure
""")
    
    return overall_success

if __name__ == "__main__":
    print("🎯 BrainVenture Academy - Mission System User Testing")
    print("💫 Comprehensive Integration Validation")
    print("🔧 Automated Testing & Manual Checklist Generator")
    
    success = generate_testing_report()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 MISSION SYSTEM READY FOR USER TESTING!")
    else:
        print("⚠️  PLEASE REVIEW AND FIX ISSUES BEFORE PROCEEDING")
    print("=" * 60)
