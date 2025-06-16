#!/usr/bin/env python3
"""
Cleanup script for ZenDegenAcademy application
Removes unnecessary test, debug, and temporary files
"""

import os
import glob
import shutil
from pathlib import Path

def count_files_by_pattern(pattern):
    """Count files matching a pattern"""
    files = glob.glob(pattern, recursive=True)
    return len(files), files

def safe_remove_files(file_list, description):
    """Safely remove files with user confirmation"""
    if not file_list:
        print(f"No {description} files found.")
        return 0
    
    print(f"\nFound {len(file_list)} {description} files:")
    for file in file_list[:10]:  # Show first 10
        print(f"  - {file}")
    if len(file_list) > 10:
        print(f"  ... and {len(file_list) - 10} more files")
    
    response = input(f"\nRemove {len(file_list)} {description} files? (y/N): ")
    if response.lower() == 'y':
        removed_count = 0
        for file in file_list:
            try:
                if os.path.isfile(file):
                    os.remove(file)
                    removed_count += 1
                    print(f"Removed: {file}")
                elif os.path.isdir(file):
                    shutil.rmtree(file)
                    removed_count += 1
                    print(f"Removed directory: {file}")
            except Exception as e:
                print(f"Error removing {file}: {e}")
        
        print(f"Successfully removed {removed_count} {description} files.")
        return removed_count
    else:
        print(f"Skipped {description} files.")
        return 0

def main():
    print("=== ZenDegenAcademy Cleanup Script ===")
    print("This script will remove unnecessary test, debug, and temporary files.\n")
    
    # Change to the script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    print(f"Working directory: {os.getcwd()}")
    
    total_removed = 0
    
    # 1. Test files
    patterns = [
        ("test_*.py", "test files"),
        ("*_test.py", "test files (suffix)"),
        ("debug_*.py", "debug files"),
        ("quick_*.py", "quick test files"),
        ("simple_*.py", "simple test files"),
        ("verify_*.py", "verification files"),
        ("validate_*.py", "validation files"),
        ("temp_*.py", "temporary Python files"),
        ("*.log", "log files"),
        ("*_output.txt", "output files"),
        ("*_results.txt", "result files"),
        ("*.broken", "broken files"),
        ("*_backup.py", "backup files"),
        ("*_old.py", "old files"),
        ("*_copy.py", "copy files"),
        ("*_COMPLETE.md", "completion documentation files"),
        ("*_ANALYSIS.md", "analysis documentation files"),
        ("*_FIXED.md", "fix documentation files"),
        ("*_DONE.md", "done documentation files"),
    ]
    
    for pattern, description in patterns:
        count, files = count_files_by_pattern(pattern)
        if count > 0:
            removed = safe_remove_files(files, description)
            total_removed += removed
    
    # 2. Empty directories
    empty_dirs = []
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # Directory is empty
                empty_dirs.append(dir_path)
    
    if empty_dirs:
        removed = safe_remove_files(empty_dirs, "empty directories")
        total_removed += removed
    
    print(f"\n=== Cleanup Complete ===")
    print(f"Total files/directories removed: {total_removed}")
    
    # Show remaining file count
    py_files = len(glob.glob("*.py"))
    md_files = len(glob.glob("*.md"))
    total_files = len(glob.glob("*"))
    
    print(f"\nRemaining files:")
    print(f"  - Python files: {py_files}")
    print(f"  - Markdown files: {md_files}")
    print(f"  - Total files: {total_files}")
    
    print("\nRecommendation: Test the application to ensure it still works correctly.")

if __name__ == "__main__":
    main()
