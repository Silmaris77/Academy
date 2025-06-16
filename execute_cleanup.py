import os
import glob

def main():
    print("Starting cleanup process...")
    
    # List of file patterns to remove
    patterns_to_remove = [
        'test_*.py',
        'debug_*.py', 
        'quick_*.py',
        'simple_*.py',
        'verify_*.py',
        'validate_*.py',
    ]
    
    total_removed = 0
    
    for pattern in patterns_to_remove:
        files = glob.glob(pattern)
        print(f"\nFound {len(files)} files matching pattern '{pattern}'")
        
        for file in files:
            if os.path.exists(file):
                try:
                    os.remove(file)
                    print(f"✓ Removed: {file}")
                    total_removed += 1
                except Exception as e:
                    print(f"✗ Error removing {file}: {e}")
    
    # Also remove specific files
    specific_files = [
        'app.log',
        'test_output.txt',
        'test_result.txt', 
        'test_result_q.txt',
        'verification_output.txt',
        'badge_award_results.txt',
        'main.py.broken'
    ]
    
    print(f"\nRemoving specific files...")
    for file in specific_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"✓ Removed: {file}")
                total_removed += 1
            except Exception as e:
                print(f"✗ Error removing {file}: {e}")
    
    print(f"\n=== Cleanup Summary ===")
    print(f"Total files removed: {total_removed}")
    
    # Count remaining files
    remaining_py = len(glob.glob("*.py"))
    remaining_md = len(glob.glob("*.md"))
    print(f"Remaining Python files: {remaining_py}")
    print(f"Remaining Markdown files: {remaining_md}")

if __name__ == "__main__":
    main()
