#!/usr/bin/env python3
"""
Test debugowania przyciska "Spróbuj ponownie" w quizie końcowym
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def debug_retry_button():
    """Debuguje dlaczego przycisk 'Spróbuj ponownie' może nie być widoczny"""
    
    print("🐛 Debugowanie przycisku 'Spróbuj ponownie' w quizie końcowym")
    print("=" * 60)
    
    # Sprawdź kod w lesson.py
    try:
        with open('views/lesson.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        print("\n📋 Analiza warunków wyświetlania przycisku:")
        
        # Sprawdź warunki w kodzie
        conditions = [
            ("quiz_completed = True", "quiz_completed" in content),
            ("quiz_passed = False", "quiz_passed" in content),  
            ("passing_threshold=75", "passing_threshold=75" in content),
            ("st.button('🔄 Spróbuj ponownie'", "🔄 Spróbuj ponownie" in content),
            ("st.error z komunikatem", "musisz uzyskać przynajmniej 75%" in content)
        ]
        
        for condition, exists in conditions:
            status = "✅" if exists else "❌"
            print(f"  {status} {condition}")
        
        print("\n🔍 Lokalizacja kodu przycisku:")
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if "🔄 Spróbuj ponownie" in line:
                print(f"  📍 Linia {i}: {line.strip()}")
                # Pokaż kontekst (poprzednie i następne linie)
                start = max(0, i-3)
                end = min(len(lines), i+2)
                print(f"     Kontekst (linie {start+1}-{end}):")
                for j in range(start, end):
                    marker = "  >>> " if j == i-1 else "      "
                    print(f"{marker}{j+1}: {lines[j]}")
                print()
        
        print("\n🎯 MOŻLIWE PRZYCZYNY NIEWIDOCZNOŚCI PRZYCISKU:")
        print("1. Quiz nie jest rozpoznawany jako 'ukończony' (quiz_completed = False)")
        print("2. Quiz jest rozpoznawany jako 'zdany' (quiz_passed = True) - wtedy przycisk się nie pokazuje")
        print("3. Użytkownik nie jest w odpowiedniej zakładce (🎓 Quiz końcowy)")
        print("4. Problem z emoji w nazwie zakładki powoduje niepoprawne działanie")
        print("5. Błąd w logice funkcji display_quiz()")
        
        print("\n🛠️ ROZWIĄZANIA DO PRZETESTOWANIA:")
        print("1. Sprawdź czy jesteś w zakładce '🎓 Quiz końcowy'")
        print("2. Upewnij się że quiz został ukończony z wynikiem < 75%")
        print("3. Sprawdź console developera w przeglądarce czy są błędy JS")
        print("4. Zrestartuj aplikację Streamlit")
        print("5. Sprawdź czy session_state nie jest uszkodzony")
        
        # Sprawdź czy emoji są poprawnie zakodowane
        print("\n🎭 Sprawdzanie emoji w kodzie:")
        problematic_emoji = ["�", "?", "\\u"]
        for emoji in problematic_emoji:
            if emoji in content:
                print(f"  ⚠️  Znaleziono problematyczne znaki: {emoji}")
            else:
                print(f"  ✅ Brak problematycznych znaków: {emoji}")
                
    except Exception as e:
        print(f"❌ Błąd podczas analizy pliku: {e}")
    
    print("\n" + "=" * 60)
    print("💡 REKOMENDACJA: Sprawdź session_state w aplikacji Streamlit")
    print("   Użyj st.write(st.session_state) żeby zobaczyć stan quizu")

if __name__ == "__main__":
    debug_retry_button()
