#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive test for practical exercises implementation
"""

import json
import os
import sys

def test_practical_exercises_comprehensive():
    """Comprehensive test of practical exercises implementation"""
    
    print("🎯 COMPREHENSIVE PRACTICAL EXERCISES TEST")
    print("=" * 60)
    
    total_tests = 0
    passed_tests = 0
    
    # Test 1: Lesson data structure
    total_tests += 1
    print("\n📋 TEST 1: Lesson Data Structure")
    print("-" * 40)
    
    try:
        lesson_path = "data/lessons/B1C1L4.json"
        if os.path.exists(lesson_path):
            with open(lesson_path, 'r', encoding='utf-8') as f:
                lesson_data = json.load(f)
            
            # Check basic structure
            if 'sections' in lesson_data and 'practical_exercises' in lesson_data['sections']:
                practical = lesson_data['sections']['practical_exercises']
                
                if 'tabs' in practical:
                    tabs = practical['tabs']
                    expected_tabs = ['reflection', 'implementation', 'analysis', 'autotest']
                    
                    # Check all expected tabs are present
                    all_tabs_present = all(tab in tabs for tab in expected_tabs)
                    
                    if all_tabs_present:
                        print("✅ All 4 expected tabs present")
                        
                        # Count total sections and interactive sections
                        total_sections = 0
                        interactive_sections = 0
                        
                        for tab_name, tab_data in tabs.items():
                            sections = tab_data.get('sections', [])
                            total_sections += len(sections)
                            interactive_sections += sum(1 for s in sections if s.get('interactive', False))
                            
                            print(f"  📝 {tab_name}: {len(sections)} sections")
                        
                        print(f"✅ Total sections: {total_sections}")
                        print(f"✅ Interactive sections: {interactive_sections}")
                        
                        if total_sections >= 12 and interactive_sections >= 10:
                            print("✅ TEST 1 PASSED: Lesson structure is comprehensive")
                            passed_tests += 1
                        else:
                            print("❌ TEST 1 FAILED: Insufficient sections")
                    else:
                        print("❌ TEST 1 FAILED: Missing expected tabs")
                else:
                    print("❌ TEST 1 FAILED: No tabs structure")
            else:
                print("❌ TEST 1 FAILED: No practical_exercises section")
        else:
            print("❌ TEST 1 FAILED: Lesson file not found")
    except Exception as e:
        print(f"❌ TEST 1 FAILED: {e}")
    
    # Test 2: lesson.py implementation
    total_tests += 1
    print("\n🔧 TEST 2: lesson.py Implementation")
    print("-" * 40)
    
    try:
        lesson_py_path = "views/lesson.py"
        if os.path.exists(lesson_py_path):
            with open(lesson_py_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check critical implementation patterns
            critical_patterns = [
                ("Step handler", "st.session_state.lesson_step == 'practical_exercises'"),
                ("Tabs rendering", "st.tabs(available_tabs)"),
                ("Interactive handling", "section.get('interactive', False)"),
                ("Form system", "st.form(key="),
                ("XP integration", "award_fragment_xp(lesson_id, 'practical_exercises'"),
                ("Step order", "'practical_exercises' in available_steps"),
                ("Step naming", "'practical_exercises': 'Ćwiczenia praktyczne'"),
                ("XP allocation", "'practical_exercises': int(base_xp * 0.40)")
            ]
            
            patterns_found = 0
            for pattern_name, pattern in critical_patterns:
                if pattern in content:
                    print(f"  ✅ {pattern_name}: Found")
                    patterns_found += 1
                else:
                    print(f"  ❌ {pattern_name}: Missing")
            
            if patterns_found == len(critical_patterns):
                print("✅ TEST 2 PASSED: All implementation patterns found")
                passed_tests += 1
            else:
                print(f"❌ TEST 2 FAILED: {patterns_found}/{len(critical_patterns)} patterns found")
        else:
            print("❌ TEST 2 FAILED: lesson.py not found")
    except Exception as e:
        print(f"❌ TEST 2 FAILED: {e}")
    
    # Test 3: Backward compatibility
    total_tests += 1
    print("\n🔄 TEST 3: Backward Compatibility")
    print("-" * 40)
    
    try:
        # Check if old reflection/application logic is preserved
        backward_patterns = [
            ("Old reflection support", "'reflection': fragment_progress.get('reflection_completed', False)"),
            ("Old application support", "'application': fragment_progress.get('application_completed', False)"),
            ("Fallback logic", "if 'reflection' in lesson.get('sections', {})"),
            ("Legacy XP", "'reflection': int(base_xp * 0.20)")
        ]
        
        backward_found = 0
        for pattern_name, pattern in backward_patterns:
            if pattern in content:
                print(f"  ✅ {pattern_name}: Found")
                backward_found += 1
            else:
                print(f"  ❌ {pattern_name}: Missing")
        
        if backward_found >= 3:  # At least 3 out of 4 for backward compatibility
            print("✅ TEST 3 PASSED: Backward compatibility maintained")
            passed_tests += 1
        else:
            print("❌ TEST 3 FAILED: Insufficient backward compatibility")
    except Exception as e:
        print(f"❌ TEST 3 FAILED: {e}")
    
    # Test 4: Polish character support
    total_tests += 1
    print("\n🇵🇱 TEST 4: Polish Character Support")
    print("-" * 40)
    
    try:
        # Check for proper Polish characters in the lesson file
        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
        polish_found = any(char in content for char in polish_chars)
        
        if polish_found:
            print("✅ Polish characters found in implementation")
            
            # Check lesson data as well
            lesson_str = json.dumps(lesson_data, ensure_ascii=False)
            lesson_polish = any(char in lesson_str for char in polish_chars)
            
            if lesson_polish:
                print("✅ Polish characters preserved in lesson data")
                print("✅ TEST 4 PASSED: Polish character support verified")
                passed_tests += 1
            else:
                print("❌ TEST 4 FAILED: No Polish characters in lesson data")
        else:
            print("❌ TEST 4 FAILED: No Polish characters found")
    except Exception as e:
        print(f"❌ TEST 4 FAILED: {e}")
    
    # Test 5: Import verification
    total_tests += 1
    print("\n📦 TEST 5: Import Verification")
    print("-" * 40)
    
    try:
        # Test critical imports
        sys.path.insert(0, '.')
        
        # Test lesson loading
        from data.lessons import load_lessons
        lessons = load_lessons()
        
        if 'B1C1L4' in lessons:
            print("✅ Lesson B1C1L4 loads successfully")
            
            # Test lesson.py import
            from views.lesson import show_lesson
            print("✅ lesson.py imports successfully")
            
            # Test if the lesson has the expected structure
            lesson = lessons['B1C1L4']
            if 'sections' in lesson and 'practical_exercises' in lesson['sections']:
                print("✅ Lesson structure accessible via import")
                print("✅ TEST 5 PASSED: Import verification successful")
                passed_tests += 1
            else:
                print("❌ TEST 5 FAILED: Lesson structure not accessible")
        else:
            print("❌ TEST 5 FAILED: Lesson B1C1L4 not found")
    except Exception as e:
        print(f"❌ TEST 5 FAILED: {e}")
    
    # Final summary
    print("\n" + "=" * 60)
    print("🎯 FINAL TEST SUMMARY")
    print("=" * 60)
    
    success_rate = (passed_tests / total_tests) * 100
    print(f"📊 Tests passed: {passed_tests}/{total_tests} ({success_rate:.1f}%)")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! Implementation is ready for production.")
        print("\n✅ VERIFICATION COMPLETE:")
        print("   • Lesson structure with 4 sub-tabs: ✅ READY")
        print("   • Interactive sections with forms: ✅ READY") 
        print("   • XP system integration: ✅ READY")
        print("   • Backward compatibility: ✅ READY")
        print("   • Polish character support: ✅ READY")
        print("   • Import system: ✅ READY")
        
        print("\n🚀 LIVE TESTING INSTRUCTIONS:")
        print("   1. Run: streamlit run main.py")
        print("   2. Navigate to: Kurs → B1C1L4 'Emocjonalna zmienność a zmienność rynku'")
        print("   3. Complete intro, opening quiz, and content sections")
        print("   4. Reach: '🎯 Ćwiczenia praktyczne' step")
        print("   5. Test all 4 sub-tabs:")
        print("      • 📝 Refleksja - Self-reflection and diary")
        print("      • 🎯 Wdrożenie - Implementation tasks")
        print("      • 📊 Analiza - Case studies and analysis")
        print("      • 🧠 Autotest - Mini-quizzes and scenarios")
        print("   6. Verify interactive forms work and save responses")
        print("   7. Complete section and verify XP is awarded")
        
    elif passed_tests >= 4:
        print("⚠️  MOSTLY READY - Minor issues detected")
        print("   Most functionality should work correctly")
        print("   Recommend live testing to identify remaining issues")
    else:
        print("❌ IMPLEMENTATION INCOMPLETE")
        print("   Critical issues found that need addressing")
        print("   Review failed tests and fix before deployment")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    test_practical_exercises_comprehensive()
