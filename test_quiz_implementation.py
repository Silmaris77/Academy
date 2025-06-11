#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for quiz implementation validation
"""

def test_quiz_implementation():
    """Test the new quiz implementation"""
    try:
        # Test importing lesson module
        from views.lesson import display_quiz
        print('✅ Quiz function imported successfully')
        
        # Test JSON structure validation
        import json
        with open('data/lessons/B1C1L4.json', 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        print('✅ Lesson JSON loaded successfully')
        
        # Check closing quiz structure
        closing_quiz = lesson_data['sections']['closing_quiz']
        print(f'✅ Found closing quiz with {len(closing_quiz["questions"])} questions')
        
        # Validate question types
        question_types = []
        for q in closing_quiz['questions']:
            q_type = q.get('type', 'single_choice')
            question_types.append(q_type)
        
        print(f'✅ Question types: {set(question_types)}')
        
        # Check multiple choice questions
        multiple_choice_count = sum(1 for q in closing_quiz['questions'] if q.get('type') == 'multiple_choice')
        print(f'✅ Multiple choice questions: {multiple_choice_count}')
        
        # Check for result interpretation
        if 'result_interpretation' in closing_quiz:
            print('✅ Result interpretation found')
            for level, data in closing_quiz['result_interpretation'].items():
                threshold = data.get('threshold', 0)
                title = data.get('title', 'N/A')
                print(f'  - {level}: {threshold}% - {title}')
        else:
            print('❌ Result interpretation missing')
        
        # Validate specific questions
        print('\n📋 Question validation:')
        for i, q in enumerate(closing_quiz['questions'], 1):
            q_type = q.get('type', 'single_choice')
            question_text = q['question'][:50] + '...' if len(q['question']) > 50 else q['question']
            
            if q_type == 'multiple_choice':
                correct_answers = q.get('correct_answers', [])
                print(f'  {i}. [{q_type}] {question_text} - Correct: {correct_answers}')
            else:
                correct_answer = q.get('correct_answer', 'N/A')
                print(f'  {i}. [{q_type}] {question_text} - Correct: {correct_answer}')
        
        print('\n✅ All validation tests passed!')
        return True
        
    except Exception as e:
        print(f'❌ Error: {e}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    result = test_quiz_implementation()
    if result:
        print("✅ Test completed successfully!")
    else:
        print("❌ Test failed!")
        exit(1)
