#!/usr/bin/env python3
"""
Debug script for testing the "Idź do misji" button functionality
"""

import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.mission_components import render_mission_summary_widget
from utils.mission_manager import mission_manager

def main():
    st.title("🔧 Debug: Mission Button Test")
    st.markdown("Testing the 'Idź do misji' button functionality")
    
    # Initialize session state
    if 'username' not in st.session_state:
        st.session_state.username = 'testuser'
    if 'current_lesson' not in st.session_state:
        st.session_state.current_lesson = None
    if 'lesson_step' not in st.session_state:
        st.session_state.lesson_step = None
    if 'show_missions_tab' not in st.session_state:
        st.session_state.show_missions_tab = False
    if 'page' not in st.session_state:
        st.session_state.page = 'dashboard'
    
    st.markdown("### Current Session State:")
    st.json({
        'username': st.session_state.username,
        'current_lesson': st.session_state.current_lesson,
        'lesson_step': st.session_state.lesson_step,
        'show_missions_tab': st.session_state.show_missions_tab,
        'page': st.session_state.page
    })
    
    st.markdown("---")
    
    # Test mission data availability
    st.markdown("### Mission Data Check:")
    try:
        summary = mission_manager.get_lesson_mission_summary('testuser', 'B1C1L1')
        st.success(f"✅ Mission data loaded successfully!")
        st.json(summary)
    except Exception as e:
        st.error(f"❌ Error loading mission data: {str(e)}")
        return
    
    st.markdown("---")
    
    # Test the mission summary widget
    st.markdown("### Mission Summary Widget Test:")
    try:
        render_mission_summary_widget('testuser', 'B1C1L1')
        st.success("✅ Mission summary widget rendered successfully!")
    except Exception as e:
        st.error(f"❌ Error rendering mission summary widget: {str(e)}")
        st.exception(e)
    
    st.markdown("---")
    
    # Button test
    st.markdown("### Manual Button Test:")
    if st.button("🎯 Test Button", key="test_button"):
        st.session_state.current_lesson = 'B1C1L1'
        st.session_state.lesson_step = 'summary'
        st.session_state.show_missions_tab = True
        st.rerun()
    
    # Show session state after button click
    if st.session_state.current_lesson:
        st.success(f"✅ Button clicked! Session state updated:")
        st.json({
            'current_lesson': st.session_state.current_lesson,
            'lesson_step': st.session_state.lesson_step,
            'show_missions_tab': st.session_state.show_missions_tab
        })
    
    st.markdown("---")
    
    # Navigation test
    st.markdown("### Navigation Test:")
    if st.button("Navigate to Lesson Page", key="nav_test"):
        st.session_state.page = 'lesson'
        st.rerun()

if __name__ == "__main__":
    main()
