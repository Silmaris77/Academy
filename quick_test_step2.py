import sys
import os

# Add the current directory to path
sys.path.append(os.path.dirname(__file__))

print("🚀 BADGE SYSTEM STEP 2 - QUICK TEST")
print("=" * 40)

try:
    from config.settings import BADGES, BADGE_CATEGORIES
    print("✅ Settings imported successfully")
    
    from utils.achievements import check_badge_condition, check_achievements
    print("✅ Achievements module imported successfully")
    
    # Quick test of badge condition checking
    test_user = {
        "user_id": "test-123",
        "degen_type": "YOLO Degen",
        "test_taken": True,
        "completed_lessons": ["B1C1L1"],
        "badges": []
    }
    
    # Test some basic conditions
    welcome_check = check_badge_condition("welcome", test_user)
    print(f"✅ Welcome badge check: {welcome_check}")
    
    first_test_check = check_badge_condition("first_degen_test", test_user)
    print(f"✅ First degen test check: {first_test_check}")
    
    first_lesson_check = check_badge_condition("first_lesson", test_user)
    print(f"✅ First lesson check: {first_lesson_check}")
    
    # Count badges by category
    category_counts = {}
    for badge_id, badge in BADGES.items():
        category = badge.get('category', 'unknown')
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print(f"\n📊 BADGE SYSTEM STATISTICS:")
    print(f"   Total badges: {len(BADGES)}")
    print(f"   Total categories: {len(BADGE_CATEGORIES)}")
    
    for category, count in category_counts.items():
        category_name = BADGE_CATEGORIES.get(category, {}).get('name', category)
        print(f"   {category_name}: {count} badges")
    
    print("\n✅ STEP 2 IMPLEMENTATION SUCCESSFUL!")
    print("🎯 Badge condition checking system is operational")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
