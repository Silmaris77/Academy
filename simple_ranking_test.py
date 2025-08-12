"""
Prosty test rankingu XP
"""

import json
import os

def load_user_data():
    """Load user data from JSON file"""
    try:
        with open('users_data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return {}

def get_top_users(limit=5):
    """Get top users by XP"""
    users_data = load_user_data()
    leaderboard = []
    
    for username, data in users_data.items():
        leaderboard.append({
            'username': username,
            'level': data.get('level', 1),
            'xp': data.get('xp', 0)
        })
    
    # Sort by XP (descending)
    leaderboard.sort(key=lambda x: x['xp'], reverse=True)
    return leaderboard[:limit]

def get_user_rank(username):
    """Get user rank in the leaderboard"""
    users_data = load_user_data()
    leaderboard = []
    
    for user, data in users_data.items():
        leaderboard.append({
            'username': user,
            'xp': data.get('xp', 0)
        })
    
    # Sort by XP (descending)
    leaderboard.sort(key=lambda x: x['xp'], reverse=True)
    
    # Find user rank
    for i, user in enumerate(leaderboard):
        if user['username'] == username:
            return {'rank': i + 1, 'xp': user['xp']}
    
    return {'rank': 0, 'xp': 0}

# Test
print("🧪 Test rankingu XP")
print("=" * 40)

# Test top 10
top_10 = get_top_users(10)
print(f"📊 Top 10 użytkowników ({len(top_10)}):")

for i, user in enumerate(top_10):
    rank = i + 1
    icon = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank}."
    print(f"   {icon} {user['username']} - {user['xp']} XP")

# Test konkretnego użytkownika
if len(top_10) > 0:
    test_username = top_10[0]['username']
    rank_data = get_user_rank(test_username)
    print(f"\n📍 Pozycja użytkownika {test_username}:")
    print(f"   Miejsce: #{rank_data['rank']}")
    print(f"   XP: {rank_data['xp']}")

print("\n✅ Test zakończony!")
