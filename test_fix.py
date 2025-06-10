print("🔧 TESTING TOTAL_POINTS KEYERROR FIX")
print("=" * 50)

with open('views/lesson.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for fixes
fixes = [
    ('if "total_points" not in st.session_state[quiz_id]:', "Backward compatibility"),
    ('total_points = st.session_state[quiz_id].get("total_points", 0)', "Safe access")
]

for pattern, description in fixes:
    if pattern in content:
        print(f"✅ {description}: Found")
    else:
        print(f"❌ {description}: Missing")

print("\n🚀 KeyError fix verification complete!")
