#!/usr/bin/env python3
"""
Quick launch script for the new ZenDegenAcademy application
"""

import subprocess
import sys
import os

def main():
    print("🚀 ZenDegenAcademy - New Application Launcher")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("main_new.py"):
        print("❌ main_new.py not found. Please run this script from the ZenDegenAcademy directory.")
        return
    
    print("✅ Found main_new.py")
    
    # Check if streamlit is available
    try:
        import streamlit
        print("✅ Streamlit is available")
    except ImportError:
        print("❌ Streamlit not found. Please install it:")
        print("   pip install streamlit")
        return
    
    print("\n🎯 Starting new ZenDegenAcademy interface...")
    print("📱 The app will open in your default browser")
    print("🔄 Use the interface toggle to switch between old/new versions")
    print("\n" + "=" * 50)
    
    try:
        # Launch the new application
        subprocess.run([sys.executable, "-m", "streamlit", "run", "main_new.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching application: {e}")
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")

if __name__ == "__main__":
    main()
