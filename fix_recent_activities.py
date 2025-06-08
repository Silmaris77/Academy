#!/usr/bin/env python3
"""
Skrypt do czyszczenia nieprawidłowych aktywności i dodania prawidłowej
"""

import json
import os
from datetime import datetime, timezone

def fix_recent_activities():
    """Napraw nieprawidłowe aktywności użytkownika"""
    
    # Wczytaj dane użytkowników
    users_file = os.path.join(os.path.dirname(__file__), 'users_data.json')
    
    with open(users_file, 'r', encoding='utf-8') as f:
        users_data = json.load(f)
    
    # Znajdź użytkownika "a"
    if "a" not in users_data:
        print("Użytkownik 'a' nie został znaleziony!")
        return
    
    user_data = users_data["a"]
    actual_degen_type = user_data.get("degen_type", "Nieznany typ")
    
    print(f"Rzeczywisty typ Degen użytkownika 'a': {actual_degen_type}")
    
    # Wyczyść nieprawidłowe aktywności (usuń wszystkie testowe aktywności z "Bitcoin Maximalist")
    if 'recent_activities' in user_data:
        original_count = len(user_data['recent_activities'])
        # Usuń aktywności z błędnym typem "Bitcoin Maximalist"
        user_data['recent_activities'] = [
            activity for activity in user_data['recent_activities']
            if not (activity.get('type') == 'degen_type_discovered' and 
                   activity.get('details', {}).get('degen_type') == 'Bitcoin Maximalist')
        ]
        new_count = len(user_data['recent_activities'])
        print(f"Usunięto {original_count - new_count} nieprawidłowych aktywności")
    else:
        user_data['recent_activities'] = []
    
    # Dodaj prawidłową aktywność z rzeczywistym typem Degen
    correct_activity = {
        "type": "degen_type_discovered",
        "details": {
            "degen_type": actual_degen_type
        },
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    
    user_data['recent_activities'].insert(0, correct_activity)
    print(f"Dodano prawidłową aktywność z typem: {actual_degen_type}")
    
    # Zapisz poprawione dane
    with open(users_file, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, indent=2, ensure_ascii=False)
    
    print("✅ Aktywności zostały naprawione!")
    
    # Wyświetl aktualną listę aktywności
    print("\nAktualne aktywności użytkownika 'a':")
    for i, activity in enumerate(user_data['recent_activities'][:5]):
        activity_type = activity.get('type')
        details = activity.get('details', {})
        timestamp = activity.get('timestamp')
        
        if activity_type == "degen_type_discovered":
            degen_type = details.get('degen_type')
            print(f"  {i+1}. Odkryto typ inwestora: {degen_type}")
        else:
            print(f"  {i+1}. {activity_type}: {details}")

if __name__ == "__main__":
    fix_recent_activities()
