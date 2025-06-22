# streamlit_runner.py - Pomocnik do uruchomienia
import subprocess
import sys
import os

def run_app(app_file="main_new.py"):
    """Uruchamia aplikację Streamlit"""
    print(f"🚀 Uruchamiam aplikację: {app_file}")
    
    # Change to app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(app_dir)
    
    # Run streamlit
    cmd = [sys.executable, "-m", "streamlit", "run", app_file]
    
    try:
        print(f"Wykonuję: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        if result.stdout:
            print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
            
    except subprocess.TimeoutExpired:
        print("✅ Aplikacja uruchamia się (timeout po 10s - to normalne)")
    except Exception as e:
        print(f"❌ Błąd: {e}")

if __name__ == "__main__":
    run_app()
