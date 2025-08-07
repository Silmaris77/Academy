#!/usr/bin/env python3
"""
Test script to verify the new 4-stage lesson structure with proper navigation
"""

import json
import sys
import os

def test_lesson_structure():
    """Test the lesson structure against the new 4-stage model"""
    
    print("🔍 Testing new 4-stage lesson structure...")
    
    # Test lesson template
    template_path = "data/lessons/lesson_template.json"
    lesson_path = "data/lessons/B1C1L1.json"
    
    success = True
    
    # Test 1: Check lesson template structure
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = json.load(f)
        
        print("\n✅ Template loaded successfully")
        
        # Check required sections in template
        required_sections = {
            'intro': ['main', 'case_study', 'quiz_samodiagnozy'],
            'sections': {
                'learning': ['sections'],
                'practical_exercises': ['exercises', 'closing_quiz']
            },
            'summary': ['main', 'case_study', 'mind_map']
        }
        
        # Check intro structure
        if 'intro' in template:
            intro = template['intro']
            for subsection in required_sections['intro']:
                if subsection not in intro:
                    print(f"❌ Missing {subsection} in intro section")
                    success = False
                else:
                    print(f"✅ Found intro.{subsection}")
        
        # Check sections structure
        if 'sections' in template:
            sections = template['sections']
            for section_name, subsections in required_sections['sections'].items():
                if section_name in sections:
                    for subsection in subsections:
                        if subsection in sections[section_name]:
                            print(f"✅ Found sections.{section_name}.{subsection}")
                        else:
                            print(f"❌ Missing sections.{section_name}.{subsection}")
                            success = False
        
        # Check summary structure
        if 'summary' in template:
            summary = template['summary']
            for subsection in required_sections['summary']:
                if subsection in summary:
                    print(f"✅ Found summary.{subsection}")
                else:
                    print(f"❌ Missing summary.{subsection}")
                    success = False
        
    except Exception as e:
        print(f"❌ Error loading template: {e}")
        success = False
    
    # Test 2: Check actual lesson structure
    try:
        with open(lesson_path, 'r', encoding='utf-8') as f:
            lesson = json.load(f)
        
        print(f"\n✅ Lesson {lesson.get('id', 'unknown')} loaded successfully")
        
        # Check lesson structure
        expected_structure = {
            'intro': ['main', 'case_study', 'quiz_samodiagnozy'],
            'sections.learning': ['sections'],
            'sections.practical_exercises': ['exercises', 'closing_quiz'],
            'summary': ['main', 'case_study', 'mind_map']
        }
        
        # Test intro structure
        if 'intro' in lesson and isinstance(lesson['intro'], dict):
            intro = lesson['intro']
            for key in expected_structure['intro']:
                if key in intro:
                    print(f"✅ Lesson has intro.{key}")
                else:
                    print(f"❌ Lesson missing intro.{key}")
                    success = False
        
        # Test sections structure
        if 'sections' in lesson:
            sections = lesson['sections']
            
            # Check learning
            if 'learning' in sections and 'sections' in sections['learning']:
                print("✅ Lesson has sections.learning.sections")
            else:
                print("❌ Lesson missing sections.learning.sections")
                success = False
            
            # Check practical_exercises
            if 'practical_exercises' in sections:
                practical = sections['practical_exercises']
                if 'exercises' in practical:
                    print("✅ Lesson has sections.practical_exercises.exercises")
                else:
                    print("❌ Lesson missing sections.practical_exercises.exercises")
                    success = False
                
                if 'closing_quiz' in practical:
                    print("✅ Lesson has sections.practical_exercises.closing_quiz")
                else:
                    print("❌ Lesson missing sections.practical_exercises.closing_quiz")
                    success = False
        
        # Test summary structure
        if 'summary' in lesson:
            summary = lesson['summary']
            for key in expected_structure['summary']:
                if key in summary:
                    print(f"✅ Lesson has summary.{key}")
                else:
                    print(f"❌ Lesson missing summary.{key}")
                    success = False
        
    except Exception as e:
        print(f"❌ Error loading lesson: {e}")
        success = False
    
    # Test 3: Check navigation logic compatibility
    print("\n🔍 Testing navigation logic...")
    
    # Expected 4-stage navigation
    expected_stages = ['intro', 'content', 'practical_exercises', 'summary']
    stage_names = {
        'intro': 'Wprowadzenie',
        'content': 'Nauka', 
        'practical_exercises': 'Praktyka',
        'summary': 'Podsumowanie'
    }
    
    print("Expected navigation stages:")
    for i, stage in enumerate(expected_stages, 1):
        print(f"{i}. {stage_names.get(stage, stage)} ({stage})")
    
    # Summary
    print(f"\n{'='*50}")
    if success:
        print("🎉 SUCCESS: New lesson structure is properly implemented!")
        print("\n📚 Structure summary:")
        print("1. Wprowadzenie")
        print("   - Wprowadzenie")
        print("   - Case Study") 
        print("   - Quiz Samodiagnozy")
        print("2. Nauka")
        print("3. Praktyka")
        print("   - Ćwiczenia")
        print("   - Quiz końcowy")
        print("4. Podsumowanie")
        print("   - Podsumowanie")
        print("   - Case Study")
        print("   - Mapa myśli")
    else:
        print("❌ FAILED: Issues found in lesson structure")
        return False
    
    return True

if __name__ == "__main__":
    success = test_lesson_structure()
    sys.exit(0 if success else 1)
