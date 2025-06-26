#!/usr/bin/env python3
"""
Analiza i organizacja plików w projekcie ZenDegenAcademy
Generuje raport z rekomendacjami dotyczącymi struktury folderów
"""

import os
import glob
from pathlib import Path
from datetime import datetime

def analyze_files():
    """Analizuje pliki w katalogu głównym i kategoryzuje je"""
    
    # Pliki produkcyjne - potrzebne do działania aplikacji
    production_files = {
        'main.py': 'Główny plik aplikacji - UŻYWANY przez start.bat',
        'requirements.txt': 'Zależności Python',
        'runtime.txt': 'Wersja Python dla Heroku',
        'start.bat': 'Launcher aplikacji',
        '.gitignore': 'Konfiguracja Git',
        'users_data.json': 'Dane użytkowników',
        'user_status.json': 'Status użytkowników'
    }
    
    # Foldery produkcyjne
    production_folders = {
        'views/', 'utils/', 'data/', 'config/', 'pages/', 'static/', 'assets/'
    }
    
    # Pliki dokumentacji - do przeniesienia do docs/
    docs_files = []
    
    # Pliki testowe - do przeniesienia do tests/
    test_files = []
    
    # Pliki prototypowe/demonstracyjne - do przeniesienia do prototypes/
    prototype_files = []
    
    # Pliki do usunięcia - niepotrzebne/zduplikowane
    files_to_delete = []
    
    # Pliki cleanup/organizacyjne - do przeniesienia do scripts/
    script_files = []
    
    # Skanuj pliki w katalogu głównym
    root_files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    for file in root_files:
        if file in production_files:
            continue
            
        # Kategoryzuj według wzorców
        file_lower = file.lower()
        
        if file.startswith('test_'):
            test_files.append(file)
        elif file.endswith('.md') and any(keyword in file_lower for keyword in ['complete', 'fix', 'status', 'analysis']):
            docs_files.append(file)
        elif file.endswith('.html') and any(keyword in file_lower for keyword in ['prototype', 'proposal', 'layout', 'mobile']):
            prototype_files.append(file)
        elif any(keyword in file_lower for keyword in ['cleanup', 'organize', 'analyze', 'execute', 'validate', 'verify']):
            script_files.append(file)
        elif file.startswith('main_') and file != 'main.py':
            # Sprawdź czy to puste pliki main
            if os.path.getsize(file) == 0:
                files_to_delete.append(f"{file} (plik pusty)")
            else:
                prototype_files.append(f"{file} (alternatywny main)")
        elif file in ['launch_app.py', 'launch_new_app.py', 'streamlit_runner.py']:
            prototype_files.append(file)
        elif any(keyword in file_lower for keyword in ['quick_', 'simple_', 'remove_']):
            script_files.append(file)
        elif file.endswith('.ps1'):
            script_files.append(file)
        else:
            # Nieznane pliki - wymagają ręcznej analizy
            pass
    
    return {
        'production': production_files,
        'production_folders': production_folders,
        'docs': docs_files,
        'tests': test_files,
        'prototypes': prototype_files,
        'scripts': script_files,
        'delete': files_to_delete
    }

def generate_organization_report():
    """Generuje raport z rekomendacjami organizacji"""
    
    analysis = analyze_files()
    
    report = f"""
# 📁 ANALIZA I ORGANIZACJA PLIKÓW - ZenDegenAcademy

**Data analizy:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🎯 CELE ORGANIZACJI
1. Wydzielenie plików produkcyjnych od deweloperskich
2. Przeniesienie dokumentacji do docs/
3. Centralizacja testów w tests/
4. Uporządkowanie prototypów w prototypes/
5. Usunięcie niepotrzebnych plików

## 📊 AKTUALNA STRUKTURA

### ✅ PLIKI PRODUKCYJNE (pozostają w root)
```
"""
    
    for file, desc in analysis['production'].items():
        if os.path.exists(file):
            report += f"✅ {file} - {desc}\n"
        else:
            report += f"❌ {file} - BRAK PLIKU!\n"
    
    report += """```

### 📁 FOLDERY PRODUKCYJNE (pozostają w root)
```
"""
    
    for folder in analysis['production_folders']:
        if os.path.exists(folder):
            report += f"✅ {folder}\n"
        else:
            report += f"❌ {folder} - BRAK FOLDERU!\n"
    
    report += f"""```

## 🗂️ PLIKI DO PRZENIESIENIA

### 📚 docs/ ({len(analysis['docs'])} plików)
```
"""
    
    for file in analysis['docs']:
        report += f"• {file}\n"
    
    report += f"""```

### 🧪 tests/ ({len(analysis['tests'])} plików) 
```
"""
    
    for file in analysis['tests']:
        report += f"• {file}\n"
    
    report += f"""```

### 🛠️ prototypes/ ({len(analysis['prototypes'])} plików)
```
"""
    
    for file in analysis['prototypes']:
        report += f"• {file}\n"
    
    report += f"""```

### ⚙️ scripts/ ({len(analysis['scripts'])} plików)
```
"""
    
    for file in analysis['scripts']:
        report += f"• {file}\n"
    
    report += f"""```

## 🗑️ PLIKI DO USUNIĘCIA ({len(analysis['delete'])} plików)
```
"""
    
    for file in analysis['delete']:
        report += f"• {file}\n"
    
    report += """```

## 📋 PLAN DZIAŁANIA

### Krok 1: Stworzenie folderów
```bash
mkdir -p tests scripts
```

### Krok 2: Przeniesienie plików dokumentacji
```bash
# Wszystkie pliki .md z fiksami/statusami
mv *_COMPLETE.md docs/fixes/
mv *_FIX*.md docs/fixes/
mv *_STATUS.md docs/status/
mv *_ANALYSIS.md docs/analysis/
```

### Krok 3: Przeniesienie testów
```bash
mv test_*.py tests/
```

### Krok 4: Przeniesienie prototypów
```bash
mv *_prototype*.html prototypes/
mv *_proposal*.html prototypes/
mv main_new*.py prototypes/ (jeśli nie są używane)
mv launch_*.py prototypes/
```

### Krok 5: Przeniesienie skryptów
```bash
mv *cleanup*.py scripts/
mv *organize*.py scripts/
mv analyze_*.py scripts/
mv *.ps1 scripts/
```

### Krok 6: Usunięcie niepotrzebnych plików
```bash
# Usuń puste pliki main_*
rm main_new.py main_new_fixed.py (jeśli puste)
```

## 🎯 STRUKTURA DOCELOWA

```
ZenDegenAcademy/
├── 📁 config/           # Konfiguracja aplikacji
├── 📁 data/             # Dane aplikacji  
├── 📁 utils/            # Narzędzia pomocnicze
├── 📁 views/            # Widoki Streamlit
├── 📁 pages/            # Strony aplikacji
├── 📁 static/           # Pliki statyczne
├── 📁 assets/           # Zasoby (obrazy, ikony)
├── 📁 docs/             # Dokumentacja
│   ├── fixes/           # Raporty napraw
│   ├── status/          # Statusy projektów  
│   ├── planning/        # Plany rozwoju
│   └── implementation/  # Dokumentacja implementacji
├── 📁 tests/            # Testy automatyczne
├── 📁 prototypes/       # Prototypy i eksperymenty
│   ├── navigation/      # Prototypy nawigacji
│   ├── ui-components/   # Komponenty UI
│   └── demos/           # Demonstracje
├── 📁 scripts/          # Skrypty pomocnicze
├── 📄 main.py           # Główny plik aplikacji
├── 📄 requirements.txt  # Zależności
├── 📄 start.bat         # Launcher
└── 📄 .gitignore        # Konfiguracja Git
```

## ⚠️ UWAGI BEZPIECZEŃSTWA

1. **Sprawdź przed usunięciem:** Upewnij się, że żaden plik nie jest importowany
2. **Backup:** Zrób kopię zapasową przed reorganizacją
3. **Testy:** Uruchom aplikację po każdej fazie reorganizacji
4. **Git:** Commituj zmiany po każdym kroku

## 🤖 AUTOMATYZACJA

Możesz użyć skryptu `organize_files.py` aby automatycznie przeprowadzić reorganizację.
"""
    
    return report

if __name__ == "__main__":
    # Sprawdź czy jesteśmy w katalogu głównym projektu
    if not os.path.exists('main.py'):
        print("❌ Błąd: Uruchom skrypt z katalogu głównego projektu (gdzie jest main.py)")
        exit(1)
    
    print("🔍 Analizuję strukturę plików...")
    
    # Generuj raport
    report = generate_organization_report()
    
    # Zapisz raport
    with open('FILE_ORGANIZATION_ANALYSIS.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("✅ Raport wygenerowany: FILE_ORGANIZATION_ANALYSIS.md")
    print("\n📋 Podsumowanie:")
    
    analysis = analyze_files()
    print(f"📚 Pliki do docs/: {len(analysis['docs'])}")
    print(f"🧪 Pliki do tests/: {len(analysis['tests'])}")  
    print(f"🛠️ Pliki do prototypes/: {len(analysis['prototypes'])}")
    print(f"⚙️ Pliki do scripts/: {len(analysis['scripts'])}")
    print(f"🗑️ Pliki do usunięcia: {len(analysis['delete'])}")
