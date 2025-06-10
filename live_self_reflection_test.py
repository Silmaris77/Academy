#!/usr/bin/env python3
"""
Live test of the self-reflection quiz to identify any remaining issues
"""

import streamlit as st
import json
import sys
import os

# Add the project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def simulate_quiz_interaction():
    """Simulate how the quiz would work with user interactions"""
    print("🧪 SIMULATING SELF-REFLECTION QUIZ INTERACTION")
    print("=" * 60)
    
    # Load the lesson data
    try:
        with open('data/lessons/B1C1L4.json', 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        quiz_data = lesson_data['sections']['opening_quiz']
        print(f"✅ Quiz loaded: {quiz_data['title']}")
        print(f"✅ Questions: {len(quiz_data['questions'])}")
        
        # Test the self-diagnostic detection logic
        is_self_diagnostic = all(q.get('correct_answer') is None for q in quiz_data['questions'])
        print(f"✅ Self-diagnostic detection: {is_self_diagnostic}")
        
        # Simulate user answering all questions with different scores
        test_scenarios = [
            ("Low score", [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),  # Total: 15 points
            ("Medium score", [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),  # Total: 30 points  
            ("High score", [4, 4, 4, 4, 4, 3, 3, 3, 3, 3]),  # Total: 38 points
        ]
        
        for scenario_name, answers in test_scenarios:
            print(f"\n🎭 SCENARIO: {scenario_name}")
            print("-" * 30)
            
            # Calculate total points (answers are 0-4, so add 1 to each)
            total_points = sum(answer + 1 for answer in answers)
            print(f"📊 Total points: {total_points}")
            
            # Find interpretation
            interpretation_found = False
            if 'scoring' in quiz_data and 'interpretation' in quiz_data['scoring']:
                for score_range, interpretation in quiz_data['scoring']['interpretation'].items():
                    if '-' in score_range:
                        min_score, max_score = map(int, score_range.split('-'))
                        if min_score <= total_points <= max_score:
                            print(f"🧮 Interpretation: {interpretation}")
                            interpretation_found = True
                            break
            
            if not interpretation_found:
                print("❌ No interpretation found for this score")
        
        # Test the current implementation logic
        print(f"\n🔧 TESTING IMPLEMENTATION LOGIC")
        print("-" * 40)
        
        # Import the actual display_quiz function
        try:
            from views.lesson import display_quiz
            print("✅ display_quiz function imported successfully")
            
            # The function should detect self-diagnostic and handle accordingly
            print("✅ Function should:")
            print("   • Detect is_self_diagnostic = True")
            print("   • Count points instead of correct answers")
            print("   • Show total points instead of percentage")
            print("   • Display appropriate interpretation")
            print("   • Use reflection-focused language")
            
        except Exception as e:
            print(f"❌ Error importing display_quiz: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in simulation: {e}")
        return False

def check_terminology_consistency():
    """Check if all terminology is consistently updated"""
    print(f"\n🔤 CHECKING TERMINOLOGY CONSISTENCY")
    print("-" * 40)
    
    try:
        with open('views/lesson.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for old terminology that should be updated
        old_terms = [
            ("Quiz startowy", "Should be 'Samorefleksja'"),
            ("quiz diagnostyczny", "Should use reflection language"),
            ("poprawne odpowiedzi", "Should not appear for self-diagnostic"),
            ("procent", "Should show points for self-diagnostic"),
        ]
        
        issues_found = []
        for term, issue in old_terms:
            if term in content:
                # Count occurrences
                count = content.count(term)
                issues_found.append(f"{term} appears {count} times - {issue}")
        
        if issues_found:
            print("⚠️ Terminology issues found:")
            for issue in issues_found:
                print(f"   • {issue}")
        else:
            print("✅ No obvious terminology issues found")
        
        # Check for correct new terminology
        good_terms = [
            "Samorefleksja",
            "Narzędzie Samorefleksji", 
            "total_points",
            "is_self_diagnostic",
            "szczera samorefleksja"
        ]
        
        print("\n✅ Good terminology found:")
        for term in good_terms:
            if term in content:
                print(f"   • {term} ✓")
            else:
                print(f"   • {term} ❌")
                
    except Exception as e:
        print(f"❌ Error checking terminology: {e}")

def main():
    """Main test function"""
    print("🪞 LIVE SELF-REFLECTION QUIZ TEST")
    print("=" * 60)
    
    success = simulate_quiz_interaction()
    check_terminology_consistency()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    if success:
        print("✅ Basic simulation completed successfully")
        print("\n🎯 NEXT STEPS:")
        print("1. Test the quiz in the actual Streamlit app")
        print("2. Verify the user sees point-based scoring")
        print("3. Check that interpretations appear correctly")
        print("4. Ensure no 'correct answers' messaging")
        print("\n🚀 The implementation should be working correctly!")
    else:
        print("❌ Issues found during simulation")

if __name__ == "__main__":
    main()
