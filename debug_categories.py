#!/usr/bin/env python3
"""
Test systemu odznak - sprawdzenie konfiguracji
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.settings import BADGES, BADGE_CATEGORIES

def test_badge_categories():
    """Test kategorii odznak"""
    print("🔍 Sprawdzanie kategorii odznak...")
    print("=" * 50)
    
    print(f"📋 Znaleziono {len(BADGE_CATEGORIES)} kategorii:")
    for cat_id, cat_info in sorted(BADGE_CATEGORIES.items(), key=lambda x: x[1]['order']):
        print(f"   {cat_info['order']}. {cat_info['icon']} {cat_info['name']} ({cat_id})")
    
    print(f"\n🏆 Znaleziono {len(BADGES)} odznak:")
    
    # Sprawdź odznaki w każdej kategorii
    for cat_id, cat_info in sorted(BADGE_CATEGORIES.items(), key=lambda x: x[1]['order']):
        category_badges = [b_id for b_id, b_info in BADGES.items() 
                          if b_info.get('category') == cat_id]
        print(f"\n📂 {cat_info['name']} ({len(category_badges)} odznak):")
        
        if not category_badges:
            print("   ❌ Brak odznak w tej kategorii!")
        else:
            for badge_id in category_badges[:5]:  # Pokaż pierwsze 5
                badge_info = BADGES[badge_id]
                tier = badge_info.get('tier', 'bronze')
                xp = badge_info.get('xp_reward', 0)
                print(f"   - {badge_info['icon']} {badge_info['name']} ({tier}, {xp} XP)")
            if len(category_badges) > 5:
                print(f"   ... i {len(category_badges) - 5} więcej")
    
    print("\n" + "=" * 50)
    return True

if __name__ == "__main__":
    test_badge_categories()
