#!/usr/bin/env python3
"""
Analizuje pliki w aplikacji i identyfikuje te które mogą być niepotrzebne
"""

import os
import glob
from collections import defaultdict

def analyze_files():
    """Analizuje pliki w aplikacji"""
    
    print("🔍 ANALIZA PLIKÓW ZENDEGENACADEMY")
    print("=" * 50)
    
    categories = {
        'main_files': [],
        'test_files': [],
        'debug_files': [],
        'quick_files': [],
        'simple_files': [],
        'verify_files': [],
        'documentation': [],
        'demo_files': [],
        'broken_files': [],
        'backup_files': [],
        'temp_files': []
    }
    
    # Analyze all Python files
    for file in glob.glob("*.py"):
        if any(x in file.lower() for x in ['test_', 'test.py']):
            categories['test_files'].append(file)
        elif any(x in file.lower() for x in ['debug_', 'debug.py']):
            categories['debug_files'].append(file)
        elif any(x in file.lower() for x in ['quick_', 'quick.py']):
            categories['quick_files'].append(file)
        elif any(x in file.lower() for x in ['simple_', 'simple.py']):
            categories['simple_files'].append(file)
        elif any(x in file.lower() for x in ['verify_', 'verify.py', 'validate_']):
            categories['verify_files'].append(file)
        elif any(x in file.lower() for x in ['demo', '_demo']):
            categories['demo_files'].append(file)
        elif 'broken' in file.lower() or '.broken' in file.lower():
            categories['broken_files'].append(file)
        elif any(x in file.lower() for x in ['_new', '_old', '_backup', '_copy']):
            categories['backup_files'].append(file)
        elif file.lower() in ['main.py', 'main_new.py', 'main_new_clean.py']:
            categories['main_files'].append(file)
        else:
            categories['main_files'].append(file)
    
    # Analyze documentation files
    for file in glob.glob("*.md"):
        categories['documentation'].append(file)
    
    # Analyze HTML demo files
    for file in glob.glob("*.html"):
        categories['demo_files'].append(file)
    
    # Analyze other potential temp files
    for file in glob.glob("*.txt"):
        if any(x in file.lower() for x in ['test', 'output', 'result', 'temp']):
            categories['temp_files'].append(file)
    
    # Print analysis
    for category, files in categories.items():
        if files:
            print(f"\n📁 {category.upper().replace('_', ' ')} ({len(files)} plików):")
            for file in sorted(files):
                print(f"   - {file}")
    
    # Calculate totals
    total_files = sum(len(files) for files in categories.values())
    potentially_removable = (
        len(categories['test_files']) +
        len(categories['debug_files']) +
        len(categories['quick_files']) +
        len(categories['simple_files']) +
        len(categories['verify_files']) +
        len(categories['demo_files']) +
        len(categories['broken_files']) +
        len(categories['backup_files']) +
        len(categories['temp_files'])
    )
    
    print(f"\n📊 PODSUMOWANIE:")
    print(f"   Łączna liczba plików: {total_files}")
    print(f"   Potencjalnie do usunięcia: {potentially_removable}")
    print(f"   Główne pliki aplikacji: {len(categories['main_files'])}")
    print(f"   Dokumentacja: {len(categories['documentation'])}")
    
    return categories

if __name__ == "__main__":
    analyze_files()
