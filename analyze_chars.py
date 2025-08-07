#!/usr/bin/env python3
"""
Analiza uszkodzonych znaków w pliku
"""

import os

def analyze_damaged_chars():
    """Analizuje uszkodzone znaki w pliku"""
    
    file_path = "views/lesson.py"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines[615:635], 616):  # Linie 616-635
        if 'Quiz końcowy' in line or 'Zadania Praktyczne' in line:
            print(f"Linia {i}: {repr(line.strip())}")
            
            # Analizuj każdy znak w linii
            for j, char in enumerate(line):
                if ord(char) > 127:  # Znaki spoza ASCII
                    print(f"  Pozycja {j}: '{char}' (U+{ord(char):04X})")

def main():
    print("🔍 ANALIZA USZKODZONYCH ZNAKÓW")
    print("=" * 40)
    
    analyze_damaged_chars()

if __name__ == "__main__":
    main()
