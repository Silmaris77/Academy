#!/usr/bin/env python3
"""
Final verification of color synchronization between Skills section and mind maps
"""
import json

def verify_color_sync():
    print("🎨 FINAL COLOR SYNCHRONIZATION VERIFICATION")
    print("=" * 55)
    
    # Load Skills block colors
    skills_colors = []
    try:
        with open('data/course_structure.json', 'r', encoding='utf-8') as f:
            course_data = json.load(f)
        
        print("✅ Course structure loaded successfully")
        print("\n📊 Skills Block Colors (gradient start colors):")
        
        for i, (block_id, block_data) in enumerate(course_data.get('blocks', {}).items(), 1):
            color_gradient = block_data.get('color', '')
            if 'linear-gradient' in color_gradient:
                # Extract first color from gradient
                start_color = color_gradient.split('(135deg, ')[1].split(',')[0].strip()
                skills_colors.append(start_color)
                print(f"  Block {block_id}: {block_data.get('name', 'Unknown').split(': ')[0]} → {start_color}")
    
    except Exception as e:
        print(f"❌ Error loading course structure: {e}")
        return False
    
    # Verify mind_map.py implementation
    print(f"\n🗺️ Mind Map Color Implementation Check:")
    try:
        with open('utils/mind_map.py', 'r', encoding='utf-8') as f:
            mind_map_content = f.read()
        
        # Check each Skills color is present
        colors_found = []
        for color in skills_colors:
            count = mind_map_content.count(color)
            if count > 0:
                colors_found.append(color)
                print(f"  ✅ {color} found {count} times in mind_map.py")
            else:
                print(f"  ❌ {color} NOT found in mind_map.py")
        
        # Check for problematic old colors
        old_colors_check = [
            "#6C5CE7",  # Old central color
            "#FD79A8",  # Old quiz color
            "#FDCB6E",  # Old reflection color 
            "#A29BFE",  # Old summary color
            "#FFD93D"   # Old XP color
        ]
        
        print(f"\n🧹 Old Color Removal Check:")
        old_colors_remaining = []
        for old_color in old_colors_check:
            count = mind_map_content.count(old_color)
            if count > 0:
                old_colors_remaining.append(old_color)
                print(f"  ⚠️  {old_color} still found {count} times")
            else:
                print(f"  ✅ {old_color} successfully removed")
                
    except Exception as e:
        print(f"❌ Error reading mind_map.py: {e}")
        return False
    
    # Summary
    print(f"\n📈 SYNCHRONIZATION SUMMARY:")
    print(f"  • Skills block colors: {len(skills_colors)}")
    print(f"  • Colors synchronized: {len(colors_found)}/{len(skills_colors)}")
    print(f"  • Old colors remaining: {len(old_colors_remaining)}")
    
    # Expected color mapping
    print(f"\n🎯 EXPECTED COLOR MAPPING:")
    color_mapping = {
        "#FF9950": "Block 1 (Emocje & Mózg) - Orange-Red",
        "#43C6AC": "Block 2 (Wewnętrzny Kompas) - Teal-Green", 
        "#667eea": "Block 3 (Świadomość Działania) - Blue-Purple",
        "#f093fb": "Block 4 (Elastyczność & Testowanie) - Pink-Magenta",
        "#4facfe": "Block 5 (Mistrzostwo & Wspólnota) - Blue-Cyan"
    }
    
    for color, description in color_mapping.items():
        print(f"  • {color} → {description}")
    
    # Success check
    if len(colors_found) == len(skills_colors) and len(old_colors_remaining) == 0:
        print(f"\n🎉 SUCCESS: Mind map colors are fully synchronized with Skills section!")
        print(f"    All {len(skills_colors)} Skills block colors are implemented in mind maps.")
        print(f"    All old colors have been successfully replaced.")
        return True
    else:
        if len(colors_found) < len(skills_colors):
            print(f"\n⚠️  PARTIAL: {len(skills_colors) - len(colors_found)} Skills colors missing from mind maps")
        if len(old_colors_remaining) > 0:
            print(f"⚠️  CLEANUP: {len(old_colors_remaining)} old colors still present")
        return False

if __name__ == "__main__":
    success = verify_color_sync()
    print(f"\n{'🎊 VERIFICATION PASSED' if success else '❌ VERIFICATION NEEDS ATTENTION'}")
