#!/usr/bin/env python3
"""
Verification script for mind map and course map color synchronization with Skills section.
"""

import json
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_skills_colors():
    """Load Skills section block colors from course_structure.json"""
    try:
        with open('data/course_structure.json', 'r', encoding='utf-8') as f:
            course_data = json.load(f)
        
        skills_colors = []
        for block in course_data.get('skills', []):
            gradient_start = block.get('gradient', {}).get('start', '')
            if gradient_start:
                skills_colors.append(gradient_start)
        
        return skills_colors
    except Exception as e:
        print(f"❌ Error loading course structure: {e}")
        return []

def check_mind_map_colors():
    """Check if mind map colors are synchronized with Skills colors"""
    try:
        with open('utils/mind_map.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        skills_colors = load_skills_colors()
        expected_colors = ["#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe"]
        
        print("🧠 MIND MAP COLOR VERIFICATION")
        print("=" * 50)
        
        # Check if expected colors are present
        colors_found = []
        for color in expected_colors:
            if color in content:
                colors_found.append(color)
                print(f"✅ Found color: {color}")
            else:
                print(f"❌ Missing color: {color}")
        
        # Check for old colors that should be removed
        old_colors = ["#6C5CE7", "#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A"]
        old_colors_found = []
        for color in old_colors:
            if color in content:
                old_colors_found.append(color)
                print(f"⚠️  Old color still present: {color}")
        
        if len(colors_found) == len(expected_colors) and len(old_colors_found) == 0:
            print("✅ Mind map colors successfully synchronized!")
            return True
        else:
            print("❌ Mind map color synchronization incomplete")
            return False
            
    except Exception as e:
        print(f"❌ Error checking mind map: {e}")
        return False

def check_course_map_colors():
    """Check if course map colors are synchronized with Skills colors"""
    try:
        with open('utils/course_map.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        expected_colors = ["#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe"]
        
        print("\n🗺️  COURSE MAP COLOR VERIFICATION")
        print("=" * 50)
        
        # Check if expected colors are present
        colors_found = []
        for color in expected_colors:
            if color in content:
                colors_found.append(color)
                print(f"✅ Found color: {color}")
            else:
                print(f"❌ Missing color: {color}")
        
        # Check for old colors that should be removed
        old_colors = ["#E74C3C", "#3498DB", "#2ECC71", "#F39C12", "#9B59B6", 
                     "#A29BFE", "#FD79A8", "#FDCB6E", "#34495E", "#7F8C8D"]
        old_colors_found = []
        for color in old_colors:
            if color in content:
                old_colors_found.append(color)
                print(f"⚠️  Old color still present: {color}")
        
        # Check for central node color
        if "#43C6AC" in content and "course_center" in content:
            print("✅ Central node color synchronized")
        else:
            print("❌ Central node color not synchronized")
        
        if len(colors_found) == len(expected_colors) and len(old_colors_found) == 0:
            print("✅ Course map colors successfully synchronized!")
            return True
        else:
            print("❌ Course map color synchronization incomplete")
            return False
            
    except Exception as e:
        print(f"❌ Error checking course map: {e}")
        return False

def main():
    """Main verification function"""
    print("🎨 COLOR SYNCHRONIZATION VERIFICATION")
    print("=" * 60)
    
    # Load expected colors from Skills section
    skills_colors = load_skills_colors()
    if skills_colors:
        print(f"📚 Skills section colors loaded: {skills_colors}")
    else:
        print("❌ Could not load Skills section colors")
        return False
    
    # Verify mind map colors
    mind_map_ok = check_mind_map_colors()
    
    # Verify course map colors  
    course_map_ok = check_course_map_colors()
    
    # Final summary
    print("\n🏁 FINAL VERIFICATION SUMMARY")
    print("=" * 60)
    
    if mind_map_ok and course_map_ok:
        print("✅ SUCCESS: All color synchronization completed!")
        print("🎯 Mind maps and course maps now use Skills section colors")
        print("🌈 Visual consistency achieved across all components")
        return True
    else:
        print("❌ INCOMPLETE: Some issues remain")
        if not mind_map_ok:
            print("   - Mind map colors need attention")
        if not course_map_ok:
            print("   - Course map colors need attention")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
