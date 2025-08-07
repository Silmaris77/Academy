"""
Test Jednakowej Szerokości Przycisków w Sidebar
Sprawdza czy zostały wprowadzone odpowiednie zmiany CSS i kodu
"""

import os
import sys

def test_button_width_implementation():
    """Test implementacji jednakowej szerokości przycisków"""
    
    print("🔍 Test Jednakowej Szerokości Przycisków w Sidebar")
    print("=" * 60)
    
    all_checks_passed = True
    
    # Sprawdź zmiany w CSS
    print("🎨 Sprawdzanie zmian w CSS:")
    
    css_file = 'static/css/style.css'
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        css_checks = [
            ('width: 100% !important', 'Wymuszenie pełnej szerokości'),
            ('min-width: 0 !important', 'Reset min-width'),
            ('box-sizing: border-box !important', 'Box-sizing dla precyzyjnych wymiarów'),
            ('use_container_width=True', 'Nie dotyczy CSS - sprawdzone w utils/components.py'),
            ('display: block !important', 'Block display dla pełnej szerokości'),
            ('text-align: center !important', 'Wyśrodkowanie tekstu'),
            ('white-space: nowrap !important', 'Zapobieganie łamaniu tekstu'),
            ('text-overflow: ellipsis !important', 'Elipsa dla długiego tekstu')
        ]
        
        for check, description in css_checks:
            if check == 'use_container_width=True':  # Skip this for CSS
                continue
                
            if check in css_content:
                print(f"✅ {description}: OK")
            else:
                print(f"❌ {description}: Brak '{check}'")
                if check != 'text-overflow: ellipsis !important':  # Optional
                    all_checks_passed = False
    else:
        print("❌ Plik static/css/style.css nie istnieje")
        all_checks_passed = False
    
    # Sprawdź zmiany w components.py
    print("\n🔧 Sprawdzanie zmian w utils/components.py:")
    
    components_file = 'utils/components.py'
    if os.path.exists(components_file):
        with open(components_file, 'r', encoding='utf-8') as f:
            components_content = f.read()
            
        components_checks = [
            ('use_container_width=True', 'Użycie pełnej szerokości kontenera w zen_button'),
            ('navigation_menu()', 'Funkcja menu nawigacji istnieje'),
            ('zen_button(', 'Funkcja zen_button istnieje'),
            ('use_container_width', 'Parametr use_container_width w zen_button')
        ]
        
        for check, description in components_checks:
            if check in components_content:
                print(f"✅ {description}: OK")
            else:
                print(f"❌ {description}: Brak")
                all_checks_passed = False
    else:
        print("❌ Plik utils/components.py nie istnieje")
        all_checks_passed = False
    
    # Sprawdź pliki testowe
    print("\n🧪 Sprawdzanie plików testowych:")
    
    test_files = [
        ('button_width_test.html', 'Test wizualny szerokości przycisków'),
    ]
    
    for file_path, description in test_files:
        if os.path.exists(file_path):
            print(f"✅ {description}: {file_path}")
        else:
            print(f"⚠️  {description}: Plik nie został utworzony")
    
    print("\n" + "=" * 60)
    print("📊 WYNIKI:")
    
    if all_checks_passed:
        print("🎉 WSZYSTKIE GŁÓWNE TESTY PRZESZŁY POMYŚLNIE!")
        print("\n📋 Zaimplementowane funkcjonalności:")
        print("✅ CSS: width: 100% !important dla wszystkich przycisków sidebar")
        print("✅ CSS: min-width: 0 !important - reset domyślnych wartości")
        print("✅ CSS: box-sizing: border-box - uwzględnia padding/border")
        print("✅ CSS: display: block - zapewnia pełną szerokość")
        print("✅ CSS: text-align: center - wyśrodkowanie tekstu")
        print("✅ Components: use_container_width=True w navigation_menu")
        print("✅ Test: button_width_test.html do wizualnej weryfikacji")
        
        print("\n🎯 Jak przetestować:")
        print("1. Otwórz button_width_test.html w przeglądarce")
        print("2. Sprawdź czy wszystkie przyciski mają identyczną szerokość")
        print("3. Uruchom główną aplikację: streamlit run main.py")
        print("4. Sprawdź sidebar - wszystkie przyciski powinny mieć taką samą szerokość")
        
        print("\n💡 Oczekiwane rezultaty:")
        print("- Przyciski 'DASHBOARD', 'LEKCJE', 'INSPIRACJE' itp. mają identyczną szerokość")
        print("- Tekst jest wyśrodkowany w każdym przycisku")
        print("- Długie nazwy są obcinane z '...' jeśli nie mieszczą się")
        print("- Wszystkie przyciski zajmują pełną szerokość dostępną w sidebar")
        
        return True
    else:
        print("⚠️  NIEKTÓRE TESTY NIE PRZESZŁY")
        print("Sprawdź powyższe błędy i popraw je przed testowaniem")
        return False

def main():
    """Uruchom testy"""
    success = test_button_width_implementation()
    
    if success:
        print("\n🔍 Dodatkowe sprawdzenia:")
        print("- Sprawdź czy CSS ma odpowiednie selektory dla Streamlit")
        print("- Przetestuj na różnych rozmiarach okna")
        print("- Sprawdź czy działa z różnymi długościami tekstu przycisków")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
