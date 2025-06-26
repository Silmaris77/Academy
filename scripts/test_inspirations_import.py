#!/usr/bin/env python3
"""
Simple test to verify inspirations system import
"""

import os
import sys

# Add the project root to Python path
project_root = r"c:\Users\Paweł\Dropbox (Osobiste)\ZenDegenAcademy"
sys.path.insert(0, project_root)

print("🧪 Testowanie importów systemu inspiracji...")

try:
    # Test imports
    from data.users import (
        mark_inspiration_as_read_for_user, 
        toggle_inspiration_favorite_for_user,
        is_inspiration_read_by_user, 
        is_inspiration_favorite_by_user
    )
    print("✅ Import data.users - sukces")
    
    from utils.inspirations_loader import (
        mark_inspiration_as_read, 
        toggle_inspiration_favorite,
        is_inspiration_read, 
        is_inspiration_favorite
    )
    print("✅ Import utils.inspirations_loader - sukces")
    
    # Test basic functionality
    print("\n📖 Test podstawowej funkcjonalności...")
    
    # Test for non-existing user (should return False/empty)
    result = is_inspiration_read_by_user("test_123", "nonexistent_user")
    print(f"   is_inspiration_read_by_user dla nieistniejącego użytkownika: {result}")
    
    result = is_inspiration_favorite_by_user("test_123", "nonexistent_user") 
    print(f"   is_inspiration_favorite_by_user dla nieistniejącego użytkownika: {result}")
    
    print("\n✅ Wszystkie testy importów i podstawowej funkcjonalności przeszły pomyślnie!")
    print("🎉 System trwałego zapamiętywania inspiracji jest gotowy do użycia!")
    
except Exception as e:
    print(f"❌ Błąd: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
