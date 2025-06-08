#!/usr/bin/env python3
"""
Test color synchronization between Skills section and mind maps
"""
import json
import os
from utils.mind_map import create_auto_generated_mind_map, create_b1c1l1_mind_map

def test_color_sync():
    print("🎨 Testing Color Synchronization Between Skills and Mind Maps")
    print("=" * 60)
    
    # Load course structure to get Skills block colors
    try:
        with open('data/course_structure.json', 'r', encoding='utf-8') as f:
            course_data = json.load(f)
        
        print("✅ Course structure loaded successfully")
        
        # Extract Skills block colors
        skills_colors = []
        for block in course_data.get('blocks', []):
            bg_color = block.get('bg_color', '')
            if bg_color and 'linear-gradient' in bg_color:
                # Extract first color from gradient
                start_color = bg_color.split('(135deg, ')[1].split(',')[0].strip()
                skills_colors.append(start_color)
                print(f"  Block: {block.get('title', 'Unknown')} → {start_color}")
        
        print(f"\n📊 Skills block colors: {skills_colors}")
        
    except Exception as e:
        print(f"❌ Error loading course structure: {e}")
        return False
    
    # Test auto-generated mind map
    print("\n🗺️ Testing auto-generated mind map colors...")
    try:
        # Load lesson data for testing
        lesson_path = os.path.join("data", "lessons", "B1C1L1.json")
        with open(lesson_path, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        # Create mind map and inspect colors
        nodes, edges = create_auto_generated_mind_map(lesson_data)
        
        print(f"✅ Mind map created with {len(nodes)} nodes and {len(edges)} edges")
        
        # Check central node color
        central_node = next((n for n in nodes if n['id'] == 'central'), None)
        if central_node:
            print(f"  Central node color: {central_node.get('color', 'Not set')}")
            if central_node.get('color') == '#43C6AC':
                print("  ✅ Central node color matches Skills Block 2 color")
            else:
                print("  ❌ Central node color doesn't match expected color")
        
        # Check section colors
        section_nodes = [n for n in nodes if n['id'].startswith('section_')]
        print(f"  Section nodes found: {len(section_nodes)}")
        
        for node in section_nodes[:5]:  # Check first 5 sections
            color = node.get('color', 'Not set')
            font_color = node.get('font', {}).get('color', 'Not set')
            print(f"    {node.get('label', 'Unknown')}: color={color}, font={font_color}")
            
            # Verify color matches Skills blocks
            if color in skills_colors:
                print(f"      ✅ Color matches Skills block color")
            else:
                print(f"      ❌ Color doesn't match any Skills block color")
        
    except Exception as e:
        print(f"❌ Error testing auto-generated mind map: {e}")
        return False
    
    # Test B1C1L1 specific mind map
    print("\n🗺️ Testing B1C1L1 specific mind map colors...")
    try:
        nodes, edges = create_b1c1l1_mind_map(lesson_data)
        
        print(f"✅ B1C1L1 mind map created with {len(nodes)} nodes and {len(edges)} edges")
        
        # Check central node
        central_node = next((n for n in nodes if n['id'] == 'central'), None)
        if central_node:
            print(f"  Central node color: {central_node.get('color', 'Not set')}")
            
        # Check concept colors
        concept_nodes = [n for n in nodes if n['id'] != 'central']
        for node in concept_nodes:
            color = node.get('color', 'Not set')
            font_color = node.get('font', {}).get('color', 'Not set')
            print(f"    {node.get('label', 'Unknown')}: color={color}, font={font_color}")
            
            if color in skills_colors:
                print(f"      ✅ Color matches Skills block color")
            else:
                print(f"      ❌ Color doesn't match any Skills block color")
                
    except Exception as e:
        print(f"❌ Error testing B1C1L1 mind map: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Color synchronization test completed!")
    return True

if __name__ == "__main__":
    test_color_sync()
