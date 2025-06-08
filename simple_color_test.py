#!/usr/bin/env python3
"""
Simple test to verify color synchronization values
"""
import json

def test_color_values():
    print("🎨 Testing Color Synchronization Values")
    print("=" * 50)
    
    # Load course structure to get Skills block colors
    try:
        with open('data/course_structure.json', 'r', encoding='utf-8') as f:
            course_data = json.load(f)
        
        print("✅ Course structure loaded")
        
        # Extract Skills block colors
        print("\n📊 Skills Block Colors:")
        skills_colors = []
        for i, block in enumerate(course_data.get('blocks', []), 1):
            bg_color = block.get('bg_color', '')
            if 'linear-gradient' in bg_color:
                # Extract first color from gradient
                start_color = bg_color.split('(135deg, ')[1].split(',')[0].strip()
                skills_colors.append(start_color)
                print(f"  Block {i}: {block.get('title', 'Unknown')} → {start_color}")
        
        print(f"\n🎯 Expected Mind Map Colors: {skills_colors}")
        
        # Read mind_map.py file to verify our changes
        print("\n🗺️ Checking Mind Map Implementation:")
        with open('utils/mind_map.py', 'r', encoding='utf-8') as f:
            mind_map_content = f.read()
            
        # Check for our synchronized colors
        colors_found = []
        for color in skills_colors:
            if color in mind_map_content:
                colors_found.append(color)
                print(f"  ✅ Found {color} in mind_map.py")
            else:
                print(f"  ❌ Missing {color} in mind_map.py")
        
        # Check for old colors that should be replaced
        old_colors = ["#6C5CE7", "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57"]
        print(f"\n🔍 Checking for old colors:")
        for old_color in old_colors:
            count = mind_map_content.count(old_color)
            if count > 0:
                print(f"  ⚠️  Found {count} instances of old color {old_color}")
            else:
                print(f"  ✅ Old color {old_color} successfully replaced")
        
        print(f"\n📈 Summary:")
        print(f"  Skills colors found in mind map: {len(colors_found)}/{len(skills_colors)}")
        print(f"  Skills colors: {skills_colors}")
        print(f"  Found colors: {colors_found}")
        
        if len(colors_found) == len(skills_colors):
            print("  🎉 Color synchronization appears successful!")
        else:
            print("  ⚠️  Some colors may not be synchronized correctly")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_color_values()
