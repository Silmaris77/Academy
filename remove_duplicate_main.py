#!/usr/bin/env python3
"""
Script to remove duplicate main files
"""
import os
import sys

def main():
    print("🧹 Cleaning up duplicate main files...")
    
    files_to_remove = [
        "main_new_clean.py"
    ]
    
    removed_count = 0
    
    for filename in files_to_remove:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"✅ Removed: {filename}")
                removed_count += 1
            except Exception as e:
                print(f"❌ Error removing {filename}: {e}")
        else:
            print(f"ℹ️  File not found: {filename}")
    
    print(f"\n📊 Summary:")
    print(f"Files removed: {removed_count}")
    
    # Show remaining main files
    main_files = [f for f in os.listdir('.') if f.startswith('main') and f.endswith('.py')]
    print(f"Remaining main files: {main_files}")
    
    print("\n✅ Cleanup complete!")
    print("Now you have:")
    print("- main.py (original/backup)")
    print("- main_new.py (with NAUKA integration)")

if __name__ == "__main__":
    main()
