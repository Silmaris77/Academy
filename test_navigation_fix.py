#!/usr/bin/env python3
"""
Test nawigacji dla strony implementacji
"""

import sys
import os

# Dodaj ścieżkę głównego katalogu
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_navigation_implementation():
    """Test czy nawigacja do implementacji działa"""
    print("🎯 TESTING IMPLEMENTATION NAVIGATION")
    print("=" * 40)
    
    try:
        # Test importów
        print("1. Testing imports...")
        from utils.session import init_session_state
        from views.implementation import show_implementation
        from utils.components import navigation_menu
        print("   ✅ All imports successful")
        
        # Test valid pages
        print("2. Testing session state...")
        import streamlit as st
        
        # Mock session state
        class MockSessionState:
            def __init__(self):
                self.data = {}
            
            def __contains__(self, key):
                return key in self.data
            
            def __getitem__(self, key):
                return self.data[key]
            
            def __setitem__(self, key, value):
                self.data[key] = value
                
            def get(self, key, default=None):
                return self.data.get(key, default)
        
        # Replace st.session_state for testing
        original_session_state = st.session_state
        st.session_state = MockSessionState()
        
        # Test init_session_state
        init_session_state()
        assert "page" in st.session_state
        print("   ✅ Session state initialized")
        
        # Test setting implementation page
        st.session_state.page = "implementation"
        init_session_state()  # Should not reset to dashboard
        assert st.session_state.page == "implementation"
        print("   ✅ Implementation page stays set")
        
        # Restore original session state
        st.session_state = original_session_state
        
        print("3. Testing implementation view...")
        # Test that show_implementation function exists and is callable
        assert callable(show_implementation)
        print("   ✅ Implementation view is callable")
        
        print("\n🎉 ALL TESTS PASSED!")
        print("Navigation to Implementation page should now work correctly.")
        
        return True
        
    except Exception as e:
        print(f"❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_navigation_implementation()
    sys.exit(0 if success else 1)
