#!/usr/bin/env python3
"""
Test badge system and find issues
"""

import sys
import traceback

print("🔍 Debugowanie systemu odznak...")

try:
    # Test 1: Import badge display system
    print("1. Testowanie importu BadgeDisplaySystem...")
    from utils.badge_display import BadgeDisplaySystem
    print("✅ BadgeDisplaySystem zaimportowany")
    
    # Test 2: Initialize system
    print("2. Inicjalizacja systemu...")
    badge_display = BadgeDisplaySystem()
    print("✅ System zainicjalizowany")
    
    # Test 3: Check BadgeTracker
    print("3. Sprawdzanie BadgeTracker...")
    tracker = badge_display.tracker
    print(f"✅ BadgeTracker: {type(tracker)}")
    
    # Test 4: Mock session state and test user data
    print("4. Testowanie danych użytkownika...")
    
    class MockSessionState:
        username = "test_user"
    
    # Mock streamlit session state
    import streamlit as st
    st.session_state = MockSessionState()
    
    # Test badge data retrieval
    try:
        badge_data = tracker.get_user_badge_data("test_user")
        print(f"✅ Dane odznak pobrane: {len(badge_data.get('badges', {}))} odznak")
    except Exception as e:
        print(f"❌ Błąd pobierania danych odznak: {e}")
        traceback.print_exc()
    
    # Test badge statistics
    try:
        badge_stats = tracker.get_badge_statistics("test_user")
        print(f"✅ Statystyki odznak: {badge_stats.get('total_earned', 0)} zdobytych")
    except Exception as e:
        print(f"❌ Błąd statystyk odznak: {e}")
        traceback.print_exc()
    
    # Test recommendations
    try:
        recommendations = tracker.get_recommended_badges("test_user")
        print(f"✅ Rekomendacje: {len(recommendations)} sugestii")
    except Exception as e:
        print(f"❌ Błąd rekomendacji: {e}")
        traceback.print_exc()
    
    print("\n5. Test renderowania...")
    try:
        badge_display.add_enhanced_badge_styles()
        print("✅ Style CSS dodane")
        
        # This would normally render, but we can't test full rendering without streamlit app
        print("✅ System gotowy do renderowania")
        
    except Exception as e:
        print(f"❌ Błąd renderowania: {e}")
        traceback.print_exc()

except ImportError as e:
    print(f"❌ Błąd importu: {e}")
    traceback.print_exc()
except Exception as e:
    print(f"❌ Nieoczekiwany błąd: {e}")
    traceback.print_exc()

print("\n🏁 Test zakończony")
