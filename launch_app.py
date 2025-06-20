#!/usr/bin/env python3
"""
App launcher for ZenDegenAcademy
"""
import os
import sys
import subprocess

def main():
    print("🚀 ZenDegenAcademy Launcher")
    print("=" * 40)
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    print(f"📁 Working directory: {current_dir}")
    
    # Check if main_new.py exists
    if not os.path.exists("main_new.py"):
        print("❌ main_new.py not found!")
        return
    
    print("✅ main_new.py found")
    
    # Launch streamlit
    print("\n🔄 Starting Streamlit...")
    print("📝 Note: If you see this message, navigation fixes have been applied")
    print("🎯 After login, look for 'NAUKA' section in the sidebar")
    print("\n" + "=" * 40)
    
    try:
        # Run streamlit in a way that doesn't capture output
        cmd = [sys.executable, "-m", "streamlit", "run", "main_new.py"]
        print(f"Executing: {' '.join(cmd)}")
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Error launching app: {e}")

if __name__ == "__main__":
    main()
