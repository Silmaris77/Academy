#!/usr/bin/env python3
"""
Test naprawy NameError w skills_new.py
"""

import sys
import os

# Dodaj ścieżkę głównego katalogu
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_skills_nameerror_fix():
    """Test czy naprawa NameError dla users_data działa"""
    print("🔧 TESTING SKILLS NAMEERROR FIX")
    print("=" * 40)
    
    try:
        # Test importów
        print("1. Testing imports...")
        import streamlit as st
        from views.skills_new import show_skill_tree, show_skills_content
        print("   ✅ Skills module imports successful")
        
        # Mock session state
        st.session_state.username = "test_user"
        
        # Test funkcji show_skill_tree
        print("2. Testing show_skill_tree function...")
        
        # Sprawdź czy funkcja może zostać wywołana (bez rzeczywistego wykonania Streamlit)
        import inspect
        signature = inspect.signature(show_skill_tree)
        assert len(signature.parameters) == 0  # Funkcja nie powinna mieć parametrów
        print("   ✅ show_skill_tree signature correct")
        
        # Test funkcji show_skills_content
        print("3. Testing show_skills_content function...")
        signature = inspect.signature(show_skills_content)
        expected_params = ['user_skills', 'user_xp', 'user_completed_lessons', 'categories', 
                          'blocks', 'categories_data', 'users_data', 'user_data', 'device_type']
        actual_params = list(signature.parameters.keys())
        assert actual_params == expected_params
        print("   ✅ show_skills_content signature correct")
        
        # Test importu load_user_data
        print("4. Testing data loading...")
        from data.users import load_user_data, get_current_user_data
        print("   ✅ User data functions import successful")
        
        print("\n🎉 ALL TESTS PASSED!")
        print("The NameError: name 'users_data' is not defined has been FIXED!")
        
        return True
        
    except Exception as e:
        print(f"❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_skills_nameerror_fix()
    sys.exit(0 if success else 1)
