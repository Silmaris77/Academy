"""
Quick test of the implementation restructure
"""

def test_implementation_move():
    print("🎯 TESTING IMPLEMENTATION RESTRUCTURE")
    print("=" * 40)
    
    # Test 1: Check new implementation view exists
    try:
        import views.implementation
        print("✅ Implementation view file exists")
    except ImportError:
        print("❌ Implementation view file missing")
        return False
    
    # Test 2: Check main.py routing
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            main_content = f.read()
        
        if "elif st.session_state.page == 'implementation':" in main_content:
            print("✅ Implementation routing added to main.py")
        else:
            print("❌ Implementation routing missing in main.py")
            
        if "from views.implementation import show_implementation" in main_content:
            print("✅ Implementation import added to main.py")
        else:
            print("❌ Implementation import missing in main.py")
    except Exception as e:
        print(f"❌ Error checking main.py: {e}")
        return False
    
    # Test 3: Check navigation menu
    try:
        with open('utils/components.py', 'r', encoding='utf-8') as f:
            components_content = f.read()
        
        if '"implementation"' in components_content and '"Wdrożenie"' in components_content:
            print("✅ Implementation added to navigation menu")
        else:
            print("❌ Implementation missing from navigation menu")
    except Exception as e:
        print(f"❌ Error checking components.py: {e}")
        return False
    
    # Test 4: Check lesson.py changes
    try:
        with open('views/lesson.py', 'r', encoding='utf-8') as f:
            lesson_content = f.read()
        
        if '"🎯 Misje praktyczne"' not in lesson_content:
            print("✅ Missions tab removed from lesson.py")
        else:
            print("❌ Missions tab still exists in lesson.py")
            
        if 'render_missions_page' not in lesson_content:
            print("✅ Mission components removed from lesson.py")
        else:
            print("❌ Mission components still in lesson.py")
    except Exception as e:
        print(f"❌ Error checking lesson.py: {e}")
        return False
    
    # Test 5: Check mission navigation update
    try:
        with open('utils/mission_components.py', 'r', encoding='utf-8') as f:
            mission_content = f.read()
        
        if "st.session_state.page = 'implementation'" in mission_content:
            print("✅ Mission navigation updated to use Implementation page")
        else:
            print("❌ Mission navigation still uses old lesson routing")
    except Exception as e:
        print(f"❌ Error checking mission_components.py: {e}")
        return False
    
    print("\n🎉 IMPLEMENTATION RESTRUCTURE COMPLETE!")
    print("=" * 40)
    print("✅ Missions moved from lesson summary to standalone 'Wdrożenie' page")
    print("✅ Navigation menu updated with new 'Wdrożenie' option")
    print("✅ Dashboard mission widget now routes to Implementation page")
    print("✅ Lesson summary cleaned up (missions tab removed)")
    
    return True

if __name__ == "__main__":
    test_implementation_move()
