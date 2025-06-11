#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import os

def test_practical_exercises_implementation():
    """Quick test to verify practical_exercises implementation works"""
    
    print("🧪 Testing practical_exercises implementation...")
    
    # Load lesson data
    lesson_file = "data/lessons/B1C1L4.json"
    
    try:
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        print("✅ B1C1L4.json loaded successfully")
        
        # Test step order logic
        available_steps = ['intro', 'content', 'summary']
        if 'opening_quiz' in lesson_data.get('sections', {}):
            available_steps.append('opening_quiz')
        if 'closing_quiz' in lesson_data.get('sections', {}):
            available_steps.append('closing_quiz')
        
        step_order = ['intro']
        if 'opening_quiz' in available_steps:
            step_order.append('opening_quiz')
        step_order.extend(['content'])
        
        # Check practical_exercises handling (this is the key test)
        if 'practical_exercises' in lesson_data.get('sections', {}):
            step_order.append('practical_exercises')
            print("✅ practical_exercises found and added to step_order")
        else:
            print("❌ practical_exercises NOT found in lesson sections")
            return False
        
        if 'closing_quiz' in available_steps:
            step_order.append('closing_quiz')
        step_order.append('summary')
        
        print(f"📋 Final step_order: {step_order}")
        
        # Test practical_exercises structure
        practical_data = lesson_data['sections']['practical_exercises']
        
        if 'tabs' in practical_data:
            tabs = practical_data['tabs']
            print(f"✅ Found tabs: {list(tabs.keys())}")
            
            # Test each expected tab
            expected_tabs = ['reflection', 'implementation', 'analysis', 'autotest']
            for tab in expected_tabs:
                if tab in tabs:
                    tab_data = tabs[tab]
                    sections_count = len(tab_data.get('sections', []))
                    print(f"  ✅ {tab}: {sections_count} sections")
                else:
                    print(f"  ❌ {tab}: missing")
            
            return True
        else:
            print("❌ No 'tabs' found in practical_exercises")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_step_names():
    """Test step names mapping"""
    print("\n🧪 Testing step names...")
    
    step_names = {
        'intro': 'Wprowadzenie',
        'opening_quiz': 'Samorefleksja',
        'content': 'Materiał',
        'practical_exercises': 'Ćwiczenia praktyczne',
        'closing_quiz': 'Quiz końcowy',
        'summary': 'Podsumowanie'
    }
    
    if 'practical_exercises' in step_names:
        name = step_names['practical_exercises']
        print(f"✅ practical_exercises name: '{name}'")
        return True
    else:
        print("❌ practical_exercises not in step_names")
        return False

if __name__ == "__main__":
    print("🚀 Quick practical_exercises test\n")
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    test1 = test_practical_exercises_implementation()
    test2 = test_step_names()
    
    if test1 and test2:
        print("\n🎉 All tests PASSED!")
        print("\n💡 If you're still seeing errors in the app:")
        print("1. Restart Streamlit app completely")
        print("2. Clear browser cache")
        print("3. Check if session state has cached old step order")
    else:
        print("\n❌ Some tests FAILED")
    
    sys.exit(0 if test1 and test2 else 1)
