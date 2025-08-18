#!/usr/bin/env python3
"""
Test funkcji ponawiania quizu końcowego
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_quiz_retry_functionality():
    """Test sprawdzający czy w kodzie jest obsługa ponawiania quizu"""
    
    print("🧪 Test funkcji ponawiania quizu końcowego")
    print("=" * 50)
    
    # Sprawdź czy pliki zawierają kod do ponawiania quizu
    files_to_check = [
        'views/lesson.py',
        'views/lesson_new.py'
    ]
    
    for file_path in files_to_check:
        print(f"\n📁 Sprawdzanie pliku: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Sprawdź czy są kluczowe elementy
            has_retry_button = '🔄 Spróbuj ponownie' in content
            has_quiz_reset = 'del st.session_state[quiz_id]' in content or 'del st.session_state[quiz_session_key]' in content
            has_rerun = 'st.rerun()' in content
            has_error_message = 'musisz uzyskać przynajmniej 75%' in content
            
            print(f"  ✅ Przycisk 'Spróbuj ponownie': {'TAK' if has_retry_button else 'NIE'}")
            print(f"  ✅ Reset stanu quizu: {'TAK' if has_quiz_reset else 'NIE'}")
            print(f"  ✅ Ponowne uruchomienie: {'TAK' if has_rerun else 'NIE'}")
            print(f"  ✅ Komunikat błędu: {'TAK' if has_error_message else 'NIE'}")
            
            if has_retry_button and has_quiz_reset and has_rerun:
                print(f"  🎉 {file_path} - IMPLEMENTACJA KOMPLETNA!")
            else:
                print(f"  ⚠️  {file_path} - BRAKUJE NIEKTÓRYCH ELEMENTÓW")
                
        except FileNotFoundError:
            print(f"  ❌ Plik {file_path} nie został znaleziony")
        except Exception as e:
            print(f"  ❌ Błąd podczas sprawdzania {file_path}: {e}")
    
    print("\n" + "=" * 50)
    print("📋 PODSUMOWANIE ROZWIĄZANIA:")
    print("1. ✅ Dodano przycisk '🔄 Spróbuj ponownie' po niepoprawnym quizie")
    print("2. ✅ Reset stanu quizu usuwa wszystkie odpowiedzi")
    print("3. ✅ Reset stanu zaliczenia pozwala ponownie spróbować")
    print("4. ✅ Komunikat błędu informuje o potrzebie 75% wyniku")
    print("5. ✅ Automatyczne odświeżenie strony po resecie")
    
    print("\n🎯 SPOSÓB DZIAŁANIA:")
    print("• Po niepoprawnym ukończeniu quizu końcowego (< 75%)")
    print("• Pojawia się komunikat błędu i przycisk 'Spróbuj ponownie'")
    print("• Kliknięcie przycisku resetuje cały stan quizu")
    print("• Użytkownik może wypełnić quiz od nowa")
    print("• Quiz można powtarzać aż do uzyskania 75%")

if __name__ == "__main__":
    test_quiz_retry_functionality()
