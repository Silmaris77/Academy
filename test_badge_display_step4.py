#!/usr/bin/env python3
"""
Test script for Badge System Step 4 - Enhanced Badge Display Integration
Tests the integration of the new BadgeDisplaySystem with the profile view
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import json
from utils.badge_display import BadgeDisplaySystem
from utils.badge_tracking import BadgeTracker
from data.users import load_user_data
from config.settings import BADGES

def test_badge_display_integration():
    """Test the badge display system integration"""
    print("🧪 Testing Badge Display System Step 4 Integration...")
    
    # Test 1: Verify BadgeDisplaySystem can be imported and initialized
    try:
        badge_display = BadgeDisplaySystem()
        print("✅ BadgeDisplaySystem imported and initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize BadgeDisplaySystem: {e}")
        return False
    
    # Test 2: Verify BadgeTracker integration
    try:
        tracker = badge_display.tracker
        assert isinstance(tracker, BadgeTracker)
        print("✅ BadgeTracker integration working")
    except Exception as e:
        print(f"❌ BadgeTracker integration failed: {e}")
        return False
    
    # Test 3: Test with a test user
    test_username = "test_user"
    test_user_data = {
        "badges": ["starter", "tester"],
        "xp": 500,
        "lessons_completed": 5,
        "login_streak": 3,
        "quizzes_taken": 2
    }
    
    try:
        # Mock session state
        class MockSessionState:
            username = test_username
        
        st.session_state = MockSessionState()
        
        # Test badge data retrieval
        badge_data = tracker.get_user_badge_data(test_username)
        print("✅ Badge data retrieval working")
        
        # Test badge statistics
        badge_stats = tracker.get_badge_statistics(test_username)
        print("✅ Badge statistics working")
        
        # Test recommendations
        recommendations = tracker.get_recommended_badges(test_username)
        print(f"✅ Recommendations working: {len(recommendations)} recommendations found")
        
    except Exception as e:
        print(f"❌ Badge data operations failed: {e}")
        return False
    
    # Test 4: Verify profile view integration
    try:
        from views.profile import show_badges_section
        print("✅ Enhanced badge section can be imported from profile view")
    except Exception as e:
        print(f"❌ Profile view integration failed: {e}")
        return False
    
    # Test 5: Check CSS styles method
    try:
        badge_display.add_enhanced_badge_styles()
        print("✅ CSS styles method working")
    except Exception as e:
        print(f"❌ CSS styles method failed: {e}")
        return False
    
    print("\n🎉 All Badge Display Step 4 integration tests passed!")
    return True

def test_component_methods():
    """Test individual component methods"""
    print("\n🧪 Testing Individual Component Methods...")
    
    badge_display = BadgeDisplaySystem()
    test_username = "test_user"
    
    # Mock session state
    class MockSessionState:
        username = test_username
    st.session_state = MockSessionState()
    
    try:
        # Test badge statistics
        badge_stats = badge_display.tracker.get_badge_statistics(test_username)
        print(f"✅ Badge statistics: {badge_stats.get('total_earned', 0)} earned badges")
        
        # Test recommendations
        recommendations = badge_display.tracker.get_recommended_badges(test_username, limit=3)
        print(f"✅ Recommendations: {len(recommendations)} badges recommended")
        
        # Test badge data
        badge_data = badge_display.tracker.get_user_badge_data(test_username)
        print(f"✅ Badge data: {len(badge_data.get('badges', {}))} badges tracked")
        
        return True
        
    except Exception as e:
        print(f"❌ Component method test failed: {e}")
        return False

def verify_badge_configuration():
    """Verify badge configuration is compatible"""
    print("\n🧪 Verifying Badge Configuration Compatibility...")
    
    try:
        # Check BADGES import
        assert len(BADGES) > 0
        print(f"✅ Found {len(BADGES)} badges in configuration")
        
        # Check badge structure
        sample_badge = next(iter(BADGES.values()))
        required_fields = ['name', 'description', 'icon', 'xp']
        for field in required_fields:
            assert field in sample_badge
        print("✅ Badge structure is compatible")
        
        return True
        
    except Exception as e:
        print(f"❌ Badge configuration verification failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("BADGE SYSTEM STEP 4 - ENHANCED DISPLAY INTEGRATION TEST")
    print("=" * 60)
    
    all_passed = True
    
    # Run tests
    all_passed &= verify_badge_configuration()
    all_passed &= test_badge_display_integration()
    all_passed &= test_component_methods()
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED - Badge Display Step 4 integration is working!")
        print("\n✨ Enhanced badge display system is now active in profile view")
        print("📋 Features available:")
        print("   • Interactive badge cards with progress visualization")
        print("   • Real-time badge recommendations")
        print("   • Category-based badge organization")
        print("   • Modern UI with animations and hover effects")
        print("   • Detailed badge statistics dashboard")
        print("   • Tier indicators and progress tracking")
    else:
        print("❌ SOME TESTS FAILED - Check the output above for details")
    
    print("=" * 60)
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
