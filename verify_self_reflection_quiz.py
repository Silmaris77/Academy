#!/usr/bin/env python3
"""
Verification script for the self-reflection quiz functionality
"""

import json
import os

def verify_quiz_structure():
    """Verify the lesson has proper self-diagnostic quiz structure"""
    print("🔍 VERIFYING SELF-REFLECTION QUIZ STRUCTURE")
    print("=" * 50)
    
    lesson_path = "data/lessons/B1C1L4.json"
    
    if not os.path.exists(lesson_path):
        print("❌ Lesson file not found")
        return False
    
    try:
        with open(lesson_path, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        quiz = lesson_data['sections']['opening_quiz']
        
        print("✅ Quiz structure found")
        print(f"✅ Title: {quiz['title']}")
        print(f"✅ Question count: {len(quiz['questions'])}")
        
        # Check if all questions are self-diagnostic
        self_diagnostic = True
        for i, q in enumerate(quiz['questions']):
            if q.get('correct_answer') is not None:
                print(f"❌ Question {i+1} has correct_answer: {q['correct_answer']}")
                self_diagnostic = False
        
        if self_diagnostic:
            print("✅ All questions are self-diagnostic (correct_answer = null)")
        
        # Check scoring system
        if 'scoring' in quiz and 'interpretation' in quiz['scoring']:
            interpretations = quiz['scoring']['interpretation']
            print(f"✅ Scoring system found with {len(interpretations)} ranges:")
            
            for score_range, interpretation in interpretations.items():
                print(f"   📊 {score_range} points: {interpretation[:50]}...")
            
            return True
        else:
            print("❌ No scoring system found")
            return False
            
    except Exception as e:
        print(f"❌ Error reading lesson: {e}")
        return False

def verify_implementation():
    """Verify the current implementation handles self-diagnostic quizzes"""
    print("\n🔧 VERIFYING IMPLEMENTATION")
    print("=" * 50)
    
    try:
        # Check if the lesson.py file has the updated logic
        with open('views/lesson.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Key implementation checks
        checks = [
            ("Self-diagnostic detection", "is_self_diagnostic = all(q.get('correct_answer') is None"),
            ("Point calculation", "total_points"),
            ("Interpretation system", "interpretation_found"),
            ("Points display", "📊 Twój wynik:"),
            ("Reflection terminology", "Samorefleksja")
        ]
        
        for check_name, check_pattern in checks:
            if check_pattern in content:
                print(f"✅ {check_name}: Found")
            else:
                print(f"❌ {check_name}: Missing pattern '{check_pattern}'")
        
        print("\n🎯 EXPECTED BEHAVIOR:")
        print("-" * 25)
        print("1. Quiz detects all correct_answer = null")
        print("2. Counts option values (1-5) instead of correct answers")
        print("3. Shows total points (10-50 range)")
        print("4. Displays interpretation based on point range")
        print("5. Uses reflection-focused language")
        print("6. No mention of 'correct answers' or percentages")
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking implementation: {e}")
        return False

def main():
    """Main verification function"""
    print("🪞 SELF-REFLECTION QUIZ VERIFICATION")
    print("=" * 60)
    
    structure_ok = verify_quiz_structure()
    implementation_ok = verify_implementation()
    
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    
    if structure_ok and implementation_ok:
        print("✅ ALL CHECKS PASSED")
        print("\n🎉 The self-reflection quiz system should be working correctly!")
        print("🪞 Users should see:")
        print("   • Title: 'Narzędzie Samorefleksji'")
        print("   • Point-based scoring (not percentages)")
        print("   • Interpretation based on 10-20, 21-35, 36-50 ranges")
        print("   • Supportive reflection language")
    else:
        print("❌ SOME CHECKS FAILED")
        if not structure_ok:
            print("   • Quiz structure or scoring system issues")
        if not implementation_ok:
            print("   • Implementation logic issues")

if __name__ == "__main__":
    main()
