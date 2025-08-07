"""
Quick Mobile Navigation Test
Uruchamia Streamlit app i testuje mobilną nawigację
"""

import subprocess
import webbrowser
import time
import sys
import os

def test_mobile_navigation():
    """Test mobilnej nawigacji w aplikacji Streamlit"""
    
    print("🚀 Uruchamianie aplikacji Streamlit...")
    print("=" * 50)
    
    # Sprawdź czy jesteśmy w odpowiednim katalogu
    if not os.path.exists('main.py'):
        print("❌ Nie znaleziono main.py - upewnij się, że jesteś w katalogu aplikacji")
        return False
    
    try:
        # Uruchom Streamlit
        print("📱 Uruchamianie: streamlit run main.py --server.port 8502")
        print("🌐 Aplikacja będzie dostępna pod: http://localhost:8502")
        print("📋 Instrukcje testowania:")
        print("1. Otwórz DevTools (F12)")
        print("2. Przełącz na widok mobilny (Ctrl+Shift+M)")
        print("3. Sprawdź dolną nawigację")
        print("4. Powinny być widoczne TYLKO ikony (🏠📚🌳👤)")
        print("5. NIE powinny być widoczne etykiety tekstowe")
        print("\n⚠️  Jeśli etykiety nadal są widoczne:")
        print("   - Wymuś odświeżenie (Ctrl+F5)")
        print("   - Wyczyść cache przeglądarki")
        print("   - Sprawdź CSS w DevTools")
        print("\n" + "=" * 50)
        
        # Uruchom Streamlit w tle
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "main.py", 
            "--server.port", "8502",
            "--server.headless", "true"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Poczekaj chwilę na uruchomienie
        time.sleep(3)
        
        # Sprawdź czy proces działa
        if process.poll() is None:
            print("✅ Aplikacja uruchomiona pomyślnie!")
            print("🌐 Otwórz: http://localhost:8502")
            
            # Opcjonalnie otwórz przeglądarkę
            try:
                webbrowser.open('http://localhost:8502')
                print("🔗 Przeglądarka została otwarta automatycznie")
            except:
                print("⚠️  Otwórz przeglądarkę ręcznie")
            
            print("\n⏱️  Naciśnij Ctrl+C aby zatrzymać aplikację")
            
            # Czekaj na zakończenie przez użytkownika
            try:
                process.wait()
            except KeyboardInterrupt:
                print("\n🛑 Zatrzymywanie aplikacji...")
                process.terminate()
                print("✅ Aplikacja zatrzymana")
                
            return True
        else:
            print("❌ Nie udało się uruchomić aplikacji")
            stdout, stderr = process.communicate()
            if stderr:
                print(f"Błąd: {stderr.decode()}")
            return False
            
    except Exception as e:
        print(f"❌ Błąd podczas uruchamiania: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_mobile_navigation()
    if not success:
        print("\n💡 Alternatywne sposoby testowania:")
        print("1. Otwórz mobile_nav_test.html w przeglądarce")
        print("2. Uruchom ręcznie: streamlit run main.py")
        print("3. Sprawdź CSS w static/css/mobile-navigation.css")
