#!/usr/bin/env python3
"""
Script to migrate existing users to include inspirations field
"""

import json
import os
import sys
from datetime import datetime

def migrate_users():
    """Migrate existing users to include inspirations field"""
    
    # Path to users_data.json
    users_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'users_data.json')
    
    if not os.path.exists(users_file):
        print("❌ Plik users_data.json nie istnieje!")
        return False
    
    print(f"📁 Ładowanie danych użytkowników z: {users_file}")
    
    # Load existing data
    try:
        with open(users_file, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
    except Exception as e:
        print(f"❌ Błąd podczas ładowania pliku: {e}")
        return False
    
    # Create backup
    backup_file = users_file + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    try:
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(users_data, f, indent=2, ensure_ascii=False)
        print(f"💾 Utworzono kopię zapasową: {backup_file}")
    except Exception as e:
        print(f"⚠️ Nie udało się utworzyć kopii zapasowej: {e}")
        return False
    
    # Migrate users
    migrated_count = 0
    total_users = len(users_data)
    
    print(f"👥 Znaleziono {total_users} użytkowników")
    
    for username, user_data in users_data.items():
        if 'inspirations' not in user_data:
            user_data['inspirations'] = {
                'read': [],
                'favorites': []
            }
            migrated_count += 1
            print(f"✅ Zmigrowano użytkownika: {username}")
        else:
            print(f"⏭️ Użytkownik {username} już ma pole inspirations")
    
    # Save updated data
    if migrated_count > 0:
        try:
            with open(users_file, 'w', encoding='utf-8') as f:
                json.dump(users_data, f, indent=2, ensure_ascii=False)
            print(f"💾 Zapisano zmiany dla {migrated_count} użytkowników")
        except Exception as e:
            print(f"❌ Błąd podczas zapisywania: {e}")
            return False
    else:
        print("ℹ️ Brak użytkowników do migracji")
    
    print("✅ Migracja zakończona pomyślnie!")
    return True

if __name__ == "__main__":
    print("🚀 Start migracji użytkowników - dodanie pola inspirations")
    print("=" * 60)
    
    if migrate_users():
        print("=" * 60)
        print("✅ Migracja zakończona sukcesem!")
        sys.exit(0)
    else:
        print("=" * 60)
        print("❌ Migracja nie powiodła się!")
        sys.exit(1)
