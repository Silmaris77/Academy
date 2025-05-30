#!/usr/bin/env python3
"""
Test naprawy systemu odznak - sprawdzenie czy odznaka "Odkrywca Osobowości" jest przyznawana
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.achievements import check_achievements, check_badge_condition
from data.users import load_user_data
from config.settings import BADGES

def test_degen_badge_fix():
    """Test sprawdzający czy odznaka za test degena działa"""
    print("🧪 TEST NAPRAWY SYSTEMU ODZNAK - ODKRYWCA OSOBOWOŚCI")
    print("=" * 60)
    
    # Sprawdź konfigurację odznaki
    badge_id = "first_degen_test"
    if badge_id not in BADGES:
        print(f"❌ Odznaka {badge_id} nie istnieje w konfiguracji!")
        return
    
    badge_info = BADGES[badge_id]
    print(f"✅ Odznaka znaleziona: {badge_info['name']}")
    print(f"📝 Opis: {badge_info['description']}")
    print(f"💎 XP nagroda: {badge_info['xp_reward']}")
    print(f"🔍 Warunek: {badge_info['condition']}")
    print()
    
    # Załaduj dane użytkowników
    users_data = load_user_data()
    
    print("👥 ANALIZA UŻYTKOWNIKÓW:")
    print("-" * 30)
    
    for username, user_data in users_data.items():
        test_taken = user_data.get('test_taken', False)
        degen_type = user_data.get('degen_type')
        has_badge = badge_id in user_data.get('badges', [])
        
        print(f"\n🔍 Użytkownik: {username}")
        print(f"   Test wykonany: {'✅' if test_taken else '❌'}")
        print(f"   Typ degena: {degen_type if degen_type else '❌ Brak'}")
        print(f"   Ma odznakę: {'✅' if has_badge else '❌'}")
        
        # Sprawdź warunki odznaki
        should_have_badge = check_badge_condition(badge_id, user_data)
        print(f"   Powinien mieć odznakę: {'✅' if should_have_badge else '❌'}")
        
        # Jeśli powinien mieć ale nie ma
        if should_have_badge and not has_badge:
            print(f"   🚨 PROBLEM: Spełnia warunki ale nie ma odznaki!")
            
            # Przetestuj przyznanie odznaki
            print(f"   🔧 Testowanie przyznania odznaki...")
            new_badges = check_achievements(username)
            if badge_id in new_badges:
                print(f"   ✅ Odznaka została przyznana!")
            else:
                print(f"   ❌ Odznaka nadal nie została przyznana")
    
    print("\n" + "=" * 60)
    print("TEST ZAKOŃCZONY")

if __name__ == "__main__":
    test_degen_badge_fix()
