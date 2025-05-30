#!/usr/bin/env python3
"""
Quick test to verify badge imports and data integrity
"""

try:
    from config.settings import BADGES, BADGE_CATEGORIES
    print("✅ Import successful")
    
    print(f"📊 Total badges: {len(BADGES)}")
    print(f"📊 Total categories: {len(BADGE_CATEGORIES)}")
    
    # Check badge categories exist
    for category_id, category_info in BADGE_CATEGORIES.items():
        print(f"  📁 {category_id}: {category_info['name']} (order: {category_info['order']})")
    
    # Check some badges
    print(f"\n🏆 First 5 badges:")
    for i, (badge_id, badge_info) in enumerate(list(BADGES.items())[:5]):
        print(f"  {i+1}. {badge_id}: {badge_info['name']} (category: {badge_info.get('category', 'N/A')})")
    
    # Check if badges have categories properly assigned
    badges_with_categories = [b for b_id, b in BADGES.items() if b.get('category')]
    print(f"\n📂 Badges with categories: {len(badges_with_categories)}/{len(BADGES)}")
    
    # Test empty user badges scenario
    user_badges = set()  # Empty set like user without badges
    print(f"\n🧪 Testing empty user badges scenario:")
    print(f"   User badges: {len(user_badges)}")
    print(f"   Total badges: {len(BADGES)}")
    print(f"   Should show full interface: YES")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
