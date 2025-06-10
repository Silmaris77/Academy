import json

# Test the self-reflection quiz
with open('data/lessons/B1C1L4.json', 'r', encoding='utf-8') as f:
    lesson_data = json.load(f)

quiz_data = lesson_data['sections']['opening_quiz']
print(f"Quiz title: {quiz_data['title']}")
print(f"Questions: {len(quiz_data['questions'])}")

# Check self-diagnostic
is_self_diagnostic = all(q.get('correct_answer') is None for q in quiz_data['questions'])
print(f"Self-diagnostic: {is_self_diagnostic}")

# Test interpretations
scenarios = [(15, "Low"), (28, "Medium"), (42, "High")]
for test_score, name in scenarios:
    print(f"\n{name} ({test_score} points):")
    for score_range, interpretation in quiz_data['scoring']['interpretation'].items():
        min_score, max_score = map(int, score_range.split('-'))
        if min_score <= test_score <= max_score:
            print(f"  {interpretation.split(' - ')[0]}")
            break
