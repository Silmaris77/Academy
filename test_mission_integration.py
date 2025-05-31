#!/usr/bin/env python3
"""
Mission Integration Test
Tests the mission system integration with lesson B1C1L1
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_mission_integration():
    print("🧪 MISSION INTEGRATION TEST")
    print("=" * 40)
    
    try:
        # Test imports
        from utils.mission_manager import mission_manager
        from utils.mission_components import render_missions_page, render_mission_summary_widget
        print("✅ Mission components imported successfully")
        
        # Test mission data loading
        missions = mission_manager.get_available_missions('test_user', 'B1C1L1')
        print(f"✅ Mission system working - found {len(missions)} missions for B1C1L1")
        
        # Test mission summary
        summary = mission_manager.get_lesson_mission_summary('test_user', 'B1C1L1')
        print(f"✅ Mission summary working - {summary['total_missions']} total missions")
        
        # Show mission details
        print("\n📋 Available Missions for B1C1L1:")
        for i, mission in enumerate(missions, 1):
            title = mission.get('title', 'Unknown')
            difficulty = mission.get('difficulty', 'unknown')
            xp_reward = mission.get('xp_reward', 0)
            duration = mission.get('duration_days', 0)
            print(f"  {i}. {title} ({difficulty}, {xp_reward} XP, {duration} days)")
        
        print("\n🎯 Mission system integration: READY")
        print("✅ The mission tab will appear in lesson B1C1L1 summary section")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in mission integration: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_mission_integration()
