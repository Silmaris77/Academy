#!/usr/bin/env python3
"""
Test modyfikacji rankingu XP - sprawdza czy wyświetla top 10 + pozycję użytkownika
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from views.dashboard import get_top_users, get_user_rank
from utils.data_utils import load_user_data

def test_ranking_functionality():
    """Test funkcjonalności rankingu XP"""
    print("🧪 Testowanie modyfikacji rankingu XP...")
    
    # Test 1: Sprawdź czy get_top_users(10) zwraca maksymalnie 10 użytkowników
    print("\n1. Test top 10 użytkowników:")
    top_10 = get_top_users(10)
    print(f"   ✓ Liczba użytkowników w top 10: {len(top_10)}")
    
    if len(top_10) > 0:
        print(f"   ✓ #1: {top_10[0]['username']} - {top_10[0]['xp']} XP")
        if len(top_10) > 1:
            print(f"   ✓ #2: {top_10[1]['username']} - {top_10[1]['xp']} XP")
        if len(top_10) > 2:
            print(f"   ✓ #3: {top_10[2]['username']} - {top_10[2]['xp']} XP")
        
        # Sprawdź czy są posortowani malejąco
        is_sorted = all(top_10[i]['xp'] >= top_10[i+1]['xp'] for i in range(len(top_10)-1))
        print(f"   ✓ Ranking posortowany malejąco: {'TAK' if is_sorted else 'NIE'}")
    
    # Test 2: Sprawdź funkcję get_user_rank
    print("\n2. Test pozycji użytkowników:")
    users_data = load_user_data()
    
    # Znajdź kilku użytkowników do testów
    test_users = list(users_data.keys())[:3] if users_data else []
    
    for username in test_users:
        rank_data = get_user_rank(username)
        user_xp = users_data[username].get('xp', 0)
        print(f"   ✓ {username}: #{rank_data['rank']} miejsce ({rank_data['xp']} XP)")
        
        # Sprawdź czy XP się zgadza
        if rank_data['xp'] == user_xp:
            print(f"     ✅ XP się zgadza")
        else:
            print(f"     ❌ XP się nie zgadza! Funkcja: {rank_data['xp']}, Dane: {user_xp}")
    
    # Test 3: Symulacja scenariuszy
    print("\n3. Test scenariuszy:")
    
    # Sprawdź czy user w top 10
    top_10_usernames = [user['username'] for user in top_10]
    
    for username in test_users[:2]:
        is_in_top_10 = username in top_10_usernames
        rank_data = get_user_rank(username)
        
        print(f"   📊 {username}:")
        print(f"     - W top 10: {'TAK' if is_in_top_10 else 'NIE'}")
        print(f"     - Pozycja: #{rank_data['rank']}")
        print(f"     - XP: {rank_data['xp']}")
        
        if not is_in_top_10 and rank_data['rank'] > 10:
            print(f"     ✅ Scenariusz: użytkownik poza top 10 - będzie pokazany jako #{rank_data['rank']}")
        elif is_in_top_10 and rank_data['rank'] <= 10:
            print(f"     ✅ Scenariusz: użytkownik w top 10 - będzie podświetlony")
    
    print("\n🎉 Test zakończony!")
    
    # Pokaż przykład działania nowego rankingu
    print("\n" + "="*60)
    print("PRZYKŁAD DZIAŁANIA NOWEGO RANKINGU:")
    print("="*60)
    
    print("🏆 TOP 10 RANKING XP:")
    for i, user in enumerate(top_10):
        rank = i + 1
        icon = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank}."
        print(f"   {icon} {user['username']} - {user['xp']} XP")
    
    # Przykład użytkownika poza top 10
    if len(test_users) > 0:
        test_user = test_users[0]
        if test_user not in top_10_usernames:
            rank_data = get_user_rank(test_user)
            print(f"\n💡 TWOJA POZYCJA (jeśli jesteś {test_user}):")
            print(f"   {rank_data['rank']}. {test_user} - {rank_data['xp']} XP")
            print(f"   📍 #{rank_data['rank']} miejsce w rankingu")

if __name__ == "__main__":
    test_ranking_functionality()
