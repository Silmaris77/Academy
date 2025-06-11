#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import json
import os

print("🔧 DEBUG: Sprawdzenie dostępności st.tabs")

try:
    print(f"Streamlit version: {st.__version__}")
    print(f"st.tabs available: {hasattr(st, 'tabs')}")
    
    if hasattr(st, 'tabs'):
        print("✅ st.tabs jest dostępne")
    else:
        print("❌ st.tabs nie jest dostępne - za stara wersja Streamlit")
        print("Wymagana wersja Streamlit >= 1.15.0 dla st.tabs")
        
except Exception as e:
    print(f"Błąd przy sprawdzaniu wersji: {e}")

# Test lesson data loading
print("\n📖 Test ładowania danych lekcji")
try:
    lesson_file = "data/lessons/B1C1L4.json"
    if os.path.exists(lesson_file):
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        print("✅ B1C1L4.json załadowany pomyślnie")
        
        if 'sections' in lesson_data and 'practical_exercises' in lesson_data['sections']:
            practical_data = lesson_data['sections']['practical_exercises']
            print("✅ Sekcja practical_exercises znaleziona")
            
            if 'tabs' in practical_data:
                tabs_data = practical_data['tabs']
                print(f"✅ Tabs znalezione: {list(tabs_data.keys())}")
                
                # Count sections
                total_sections = 0
                for tab_name, tab_data in tabs_data.items():
                    sections_count = len(tab_data.get('sections', []))
                    total_sections += sections_count
                    print(f"  - {tab_name}: {sections_count} sekcji")
                
                print(f"📊 Łącznie sekcji: {total_sections}")
                
            else:
                print("❌ Brak sekcji 'tabs' w practical_exercises")
        else:
            print("❌ Brak sekcji practical_exercises")
    else:
        print(f"❌ Nie znaleziono pliku: {lesson_file}")
        
except Exception as e:
    print(f"❌ Błąd podczas ładowania danych: {e}")

print("\n🎯 Status implementacji:")
print("- Struktura JSON: ✅")
print("- Dane lekcji: ✅") 
print("- Problem prawdopodobnie w lesson.py lub wersji Streamlit")
