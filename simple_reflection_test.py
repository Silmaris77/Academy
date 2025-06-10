#!/usr/bin/env python3
"""
Simple test of self-reflection quiz data and logic
"""

import json
import os

def test_quiz_logic():
    """Test the self-reflection quiz logic"""
    print("🧪 TESTING SELF-REFLECTION QUIZ LOGIC")
    print("=" * 50)
    
    # Load lesson data
    lesson_path = "data/lessons/B1C1L4.json"
    if not os.path.exists(lesson_path):
        print("❌ Lesson file not found")
        return
    
    with open(lesson_path, 'r', encoding='utf-8') as f:
        lesson_data = json.load(f)
    
    quiz_data = lesson_data['sections']['opening_quiz']
    print(f"✅ Quiz title: {quiz_data['title']}")
    print(f"✅ Questions: {len(quiz_data['questions'])}")
    
    # Check self-diagnostic detection
    is_self_diagnostic = all(q.get('correct_answer') is None for q in quiz_data['questions'])
    print(f"✅ Self-diagnostic: {is_self_diagnostic}")
    
    # Test scoring scenarios
    scenarios = [
        ("Low impact", 15),   # 10-20 range
        ("Medium impact", 28), # 21-35 range  
        ("High impact", 42),   # 36-50 range
    ]
    
    print("\n📊 TESTING INTERPRETATION SYSTEM:")
    print("-" * 35)
    
    for scenario_name, test_score in scenarios:
        print(f"\n🎯 {scenario_name} ({test_score} points):")
        
        # Find matching interpretation
        interpretation_found = False
        if 'scoring' in quiz_data and 'interpretation' in quiz_data['scoring']:
            for score_range, interpretation in quiz_data['scoring']['interpretation'].items():
                if '-' in score_range:
                    min_score, max_score = map(int, score_range.split('-'))
                    if min_score <= test_score <= max_score:
                        status = interpretation.split(' - ')[0]  # Get the emoji and status
                        print(f"   {status}")
                        interpretation_found = True
                        break
        
        if not interpretation_found:
            print(f"   ❌ No interpretation found")
    
    # Check implementation file
    print(f"\n🔧 CHECKING IMPLEMENTATION FILE:")
    print("-" * 35)
    
    try:
        with open('views/lesson.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Key checks
        checks = [
            "is_self_diagnostic = all(q.get('correct_answer') is None",
            "total_points",
            "📊 Twój wynik:",
            "interpretation_found",
            "Samorefleksja"
        ]
        
        for check in checks:
            if check in content:
                print(f"   ✅ {check}")
            else:
                print(f"   ❌ Missing: {check}")
        
        # Check for problematic old terms
        old_terms = ["poprawne odpowiedzi", "procent poprawnych"]
        for term in old_terms:
            if term in content:
                print(f"   ⚠️ Found old term: {term}")
    
    except Exception as e:
        print(f"   ❌ Error reading implementation: {e}")
    
    print(f"\n🎉 TEST COMPLETE!")
    print("=" * 50)

if __name__ == "__main__":
    test_quiz_logic()
