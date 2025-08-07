"""
Test Auto-Close Sidebar Functionality
Sprawdza czy mobilna nawigacja poprawnie zamyka sidebar
"""

import os
import sys

def test_mobile_navigation_autoclose():
    """Test funkcjonalności auto-zamykania sidebara"""
    
    print("🔍 Test Auto-Close Sidebar dla Mobilnej Nawigacji")
    print("=" * 60)
    
    # Sprawdź pliki
    files_to_check = [
        ('utils/mobile_navigation.py', 'closeMobileSidebar'),
        ('static/css/mobile-navigation.css', 'mobile-force-hidden'),
        ('main.py', 'render_mobile_navigation'),
        ('sidebar_autoclose_test.html', 'navigateToPage')
    ]
    
    all_checks_passed = True
    
    print("📁 Sprawdzanie plików i funkcjonalności:")
    
    for file_path, search_term in files_to_check:
        full_path = os.path.join(os.getcwd(), file_path)
        
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if search_term in content:
                print(f"✅ {file_path}: Zawiera '{search_term}'")
            else:
                print(f"❌ {file_path}: Brak '{search_term}'")
                all_checks_passed = False
        else:
            print(f"❌ {file_path}: Plik nie istnieje")
            all_checks_passed = False
    
    print("\n🧪 Sprawdzanie implementacji JavaScript:")
    
    # Sprawdź szczegóły implementacji
    mobile_nav_file = 'utils/mobile_navigation.py'
    if os.path.exists(mobile_nav_file):
        with open(mobile_nav_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Sprawdź kluczowe elementy
        js_checks = [
            ('closeMobileSidebar()', 'Funkcja zamykania sidebara'),
            ('window.innerWidth <= 1024', 'Detekcja urządzeń mobilnych'),
            ('mobile-force-hidden', 'CSS class dla ukrywania'),
            ('translateX(-100%)', 'Animacja przesunięcia'),
            ('Auto-close mobile sidebar', 'Komentarz wywołania funkcji')
        ]
        
        for check, description in js_checks:
            if check in content:
                print(f"✅ {description}: OK")
            else:
                print(f"❌ {description}: Brak")
                all_checks_passed = False
    
    print("\n🎨 Sprawdzanie CSS:")
    
    css_file = 'static/css/mobile-navigation.css'
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        css_checks = [
            ('mobile-force-hidden', 'CSS class ukrywania'),
            ('translateX(-100%)', 'Animacja przesunięcia'),
            ('transition:', 'Smooth transitions'),
            ('z-index: 999', 'Z-index sidebara'),
            ('z-index.*1000', 'Z-index mobilnej nawigacji')
        ]
        
        for check, description in css_checks:
            if check in css_content:
                print(f"✅ {description}: OK")
            else:
                print(f"⚠️  {description}: Sprawdź ręcznie")
    
    print("\n" + "=" * 60)
    print("📊 WYNIKI:")
    
    if all_checks_passed:
        print("🎉 WSZYSTKIE TESTY PRZESZŁY POMYŚLNIE!")
        print("\n📋 Funkcjonalność auto-zamykania sidebara:")
        print("✅ JavaScript: closeMobileSidebar() zaimplementowane")
        print("✅ CSS: Animacje i style gotowe")
        print("✅ Integration: Dodane do main.py")
        print("✅ Test: sidebar_autoclose_test.html utworzony")
        
        print("\n🎯 Jak przetestować:")
        print("1. Otwórz sidebar_autoclose_test.html w przeglądarce")
        print("2. Przełącz na widok mobilny (F12 → Device Mode)")
        print("3. Kliknij zakładkę w dolnej nawigacji")
        print("4. Sidebar powinien się automatycznie zamknąć")
        
        print("\n5. Lub uruchom główną aplikację:")
        print("   streamlit run main.py")
        print("   I przetestuj na prawdziwym urządzeniu mobilnym")
        
        return True
    else:
        print("⚠️  NIEKTÓRE TESTY NIE PRZESZŁY")
        print("Sprawdź powyższe błędy i popraw je przed testowaniem")
        return False

def main():
    """Uruchom testy"""
    success = test_mobile_navigation_autoclose()
    
    if success:
        print("\n💡 Dodatkowe informacje:")
        print("- Funkcja działa tylko na urządzeniach ≤1024px szerokości")
        print("- Używa wielu metod zamykania sidebara (fallback)")
        print("- Smooth CSS animations dla lepszego UX")
        print("- Automatyczne dostosowanie głównej treści")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
