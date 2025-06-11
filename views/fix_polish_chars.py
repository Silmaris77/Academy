#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script to fix corrupted Polish characters in lesson.py

def fix_polish_characters():
    # Read the current file
    with open('lesson.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Common corrupted Polish character patterns found in the file
    fixes = [
        ('ukoĹ„czona', 'ukończona'),
        ('ukoĹ„czony', 'ukończony'), 
        ('ukoĹ„czone', 'ukończone'),
        ('ukoĹ„czenie', 'ukończenie'),
        ('ukoĹ„czyĹ‚eĹ›', 'ukończyłeś'),
        ('SprawdĹş', 'Sprawdź'),
        ('ZdobyĹ‚eĹ›', 'Zdobyłeś'),
        ('ksztaĹ‚t', 'kształt'),
        ('UkoĹ„czony', 'Ukończony'),
        ('pominiÄ™ty', 'pominięty'),
        ('ukoĹ„ony', 'ukończony'),
        ('zostaĹ‚', 'został'),
        ('lekcjÄ™', 'lekcję'),
        ('caĹ‚Ä…', 'całą'),
        ('Ĺ‚Ä…cznie', 'łącznie'),
        ('przyciskĂłw', 'przycisków'),
        ('wpĹ‚ywa', 'wpływa'),
        ('nawigacjÄ™', 'nawigację'),
        ('WyĹ›wietla', 'Wyświetla'),
        ('koĹ„cowego', 'końcowego'),
        ('wyĹ›wietl', 'wyświetl'),
        ('koniecznoĹ›ci', 'konieczności'),
        ('jeĹ›li', 'jeśli'),
        ('GratulajeĹ„', 'Gratulacje'),
        ('Quiz nie jest jeszcze ukoĹ„czony', 'Quiz nie jest jeszcze ukończony')
    ]

    # Apply fixes
    changes_made = 0
    for corrupted, correct in fixes:
        if corrupted in content:
            count = content.count(corrupted)
            content = content.replace(corrupted, correct)
            changes_made += count
            print(f'Fixed {count} instances: {corrupted} -> {correct}')

    print(f'Total changes made: {changes_made}')

    # Write back if changes were made  
    if changes_made > 0:
        with open('lesson.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Polish characters restored and saved to lesson.py')
        return True
    else:
        print('No corrupted patterns found to fix')
        return False

if __name__ == '__main__':
    fix_polish_characters()
