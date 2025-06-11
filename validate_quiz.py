import json

print("Testing quiz implementation...")

# Test JSON loading
with open('data/lessons/B1C1L4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("✅ JSON loaded successfully")

# Check closing quiz
quiz = data['sections']['closing_quiz']
print(f"✅ Questions count: {len(quiz['questions'])}")

# Check question types
types = []
for q in quiz['questions']:
    types.append(q.get('type', 'single_choice'))

print(f"✅ Question types: {set(types)}")

# Check multiple choice
mc_count = sum(1 for q in quiz['questions'] if q.get('type') == 'multiple_choice')
print(f"✅ Multiple choice questions: {mc_count}")

# Check interpretation
if 'result_interpretation' in quiz:
    print("✅ Result interpretation found")
else:
    print("❌ Result interpretation missing")

print("✅ Basic validation complete!")
