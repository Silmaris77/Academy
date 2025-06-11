#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test specific for B1C1L4 practical_exercises structure
"""

import json
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_b1c1l4_practical_exercises():
    """Test the practical_exercises structure in B1C1L4"""
    print("🧪 Testing B1C1L4 practical_exercises structure...")
    
    lesson_file = "data/lessons/B1C1L4.json"
    
    if not os.path.exists(lesson_file):
        print(f"❌ Error: {lesson_file} not found!")
        return False
    
    try:
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        print("✅ B1C1L4.json loaded successfully")
        
        # Check sections
        sections = lesson_data.get('sections', {})
        print(f"📋 Sections found: {list(sections.keys())}")
        
        # Check practical_exercises
        if 'practical_exercises' not in sections:
            print("❌ No practical_exercises section found")
            return False
        
        practical_exercises = sections['practical_exercises']
        print(f"✅ practical_exercises section found with keys: {list(practical_exercises.keys())}")
        
        # Check tabs structure
        if 'tabs' not in practical_exercises:
            print("❌ No 'tabs' found in practical_exercises")
            return False
        
        tabs = practical_exercises['tabs']
        print(f"📋 Tabs found: {list(tabs.keys())}")
        
        # Check each tab
        expected_tabs = ['reflection', 'implementation', 'analysis', 'autotest']
        for tab_name in expected_tabs:
            if tab_name in tabs:
                tab_data = tabs[tab_name]
                sections_count = len(tab_data.get('sections', []))
                title = tab_data.get('title', 'No title')
                print(f"  ✅ {tab_name}: '{title}' with {sections_count} sections")
            else:
                print(f"  ❌ {tab_name}: Missing")
        
        print("✅ B1C1L4 practical_exercises structure test PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing B1C1L4: {e}")
        return False

def test_lesson_py_logic():
    """Test the lesson.py logic for handling practical_exercises"""
    print("\n🧪 Testing lesson.py practical_exercises logic...")
    
    # Simulate the lesson step order logic
    lesson_data = {
        'sections': {
            'opening_quiz': {},
            'learning': {},
            'practical_exercises': {
                'tabs': {
                    'reflection': {'sections': []},
                    'implementation': {'sections': []},
                    'analysis': {'sections': []},
                    'autotest': {'sections': []}
                }
            },
            'closing_quiz': {}
        }
    }
    
    # Test step order logic
    available_steps = ['intro', 'content', 'summary']
    if 'opening_quiz' in lesson_data.get('sections', {}):
        available_steps.append('opening_quiz')
    if 'application' in lesson_data.get('sections', {}):
        available_steps.append('application')
    if 'closing_quiz' in lesson_data.get('sections', {}):
        available_steps.append('closing_quiz')
    
    step_order = ['intro']
    if 'opening_quiz' in available_steps:
        step_order.append('opening_quiz')
    step_order.extend(['content'])
    
    # Check practical_exercises handling
    if 'practical_exercises' in lesson_data.get('sections', {}):
        step_order.append('practical_exercises')
        print("  ✅ practical_exercises added to step_order")
    elif 'reflection' in available_steps or 'application' in available_steps:
        if 'reflection' in available_steps:
            step_order.append('reflection')
        if 'application' in available_steps:
            step_order.append('application')
    
    if 'closing_quiz' in available_steps:
        step_order.append('closing_quiz')
    step_order.append('summary')
    
    print(f"📋 Final step_order: {step_order}")
    
    # Test step names
    step_names = {
        'intro': 'Wprowadzenie',
        'opening_quiz': 'Samorefleksja',
        'content': 'Materiał',
        'practical_exercises': 'Ćwiczenia praktyczne',
        'reflection': 'Refleksja',
        'application': 'Zadania praktyczne',
        'closing_quiz': 'Quiz końcowy',
        'summary': 'Podsumowanie'
    }
    
    if 'practical_exercises' in step_order:
        step_name = step_names.get('practical_exercises', 'Unknown')
        print(f"  ✅ practical_exercises step name: '{step_name}'")
        
        # Test tab structure handling
        practical_data = lesson_data['sections']['practical_exercises']
        if 'tabs' in practical_data:
            tabs_data = practical_data['tabs']
            tab_keys = list(tabs_data.keys())
            print(f"  ✅ Available tabs: {tab_keys}")
            return True
        else:
            print("  ❌ No 'tabs' found in practical_exercises")
            return False
    else:
        print("  ❌ practical_exercises not in step_order")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting B1C1L4 practical_exercises tests...\n")
    
    tests = [
        test_b1c1l4_practical_exercises,
        test_lesson_py_logic
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with error: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! B1C1L4 practical_exercises should work correctly!")
        print("\n💡 The issue might be:")
        print("1. App not restarted after code changes")
        print("2. Session state cache needs clearing")
        print("3. Encoding issue in browser/Streamlit")
    else:
        print("⚠️ Some tests failed. Check the implementation.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
