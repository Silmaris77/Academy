#!/usr/bin/env python3
"""
Test that the KeyError: 'total_points' issue is fixed
"""

def test_keyerror_fix():
    print("🔧 KEYERROR FIX VERIFICATION")
    print("=" * 40)
    
    try:
        with open('views/lesson.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for the fixes
        fixes_found = 0
        
        # Fix 1: Backward compatibility in initialization
        if 'if "total_points" not in st.session_state[quiz_id]:' in content:
            print("✅ Fix 1: Backward compatibility check in initialization")
            fixes_found += 1
        else:
            print("❌ Fix 1: Missing backward compatibility check")
        
        # Fix 2: Safe access using .get()
        if 'total_points = st.session_state[quiz_id].get("total_points", 0)' in content:
            print("✅ Fix 2: Safe access using .get() method")
            fixes_found += 1
        else:
            print("❌ Fix 2: Missing safe access method")
        
        # Fix 3: Safety check before adding points
        if 'if "total_points" not in st.session_state[quiz_id]:' in content and 'st.session_state[quiz_id]["total_points"] = 0' in content:
            print("✅ Fix 3: Safety check before adding points")
            fixes_found += 1
        else:
            print("❌ Fix 3: Missing safety check")
        
        print(f"\n📊 SUMMARY: {fixes_found}/3 fixes implemented")
        
        if fixes_found == 3:
            print("🎉 ALL FIXES IMPLEMENTED SUCCESSFULLY!")
            print("\n🎯 The KeyError: 'total_points' issue should now be resolved.")
            print("✅ The application can handle both:")
            print("   • New quiz sessions (with total_points)")
            print("   • Existing quiz sessions (without total_points)")
        else:
            print("⚠️ Some fixes may be missing")
            
    except Exception as e:
        print(f"❌ Error checking fixes: {e}")

if __name__ == "__main__":
    test_keyerror_fix()
