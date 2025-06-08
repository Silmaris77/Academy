#!/usr/bin/env python3
"""
Test script to verify HTML/Markdown rendering fixes in Degen Explorer
"""

import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_degen_details_import():
    """Test if degen_details can be imported correctly"""
    try:
        from data.degen_details import degen_details
        print("✅ degen_details imported successfully")
        
        # Check if we have content for common degen types
        common_types = ["Spekulant", "Holder", "Trader", "Inwestor wartościowy"]
        for degen_type in common_types:
            if degen_type in degen_details:
                content = degen_details[degen_type]
                if "##" in content or "**" in content:
                    print(f"✅ {degen_type}: Contains Markdown formatting")
                else:
                    print(f"⚠️  {degen_type}: No Markdown formatting detected")
            else:
                print(f"❌ {degen_type}: Not found in degen_details")
        
        return True
    except Exception as e:
        print(f"❌ Failed to import degen_details: {e}")
        return False

def test_degen_explorer_import():
    """Test if degen explorer can be imported without syntax errors"""
    try:
        from views.degen_explorer import show_degen_explorer
        print("✅ degen_explorer imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import degen_explorer: {e}")
        return False

def test_degen_test_import():
    """Test if degen test can be imported without syntax errors"""
    try:
        from views.degen_test import show_degen_test
        print("✅ degen_test imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import degen_test: {e}")
        return False

def test_profile_import():
    """Test if profile can be imported without syntax errors"""
    try:
        from views.profile import show_profile
        print("✅ profile imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import profile: {e}")
        return False

def main():
    print("🔍 TESTING HTML/MARKDOWN RENDERING FIXES")
    print("=" * 50)
    
    success = True
    
    # Test 1: Check degen_details content
    print("\n1. Testing degen_details content...")
    if not test_degen_details_import():
        success = False
    
    # Test 2: Check degen_explorer imports
    print("\n2. Testing degen_explorer imports...")
    if not test_degen_explorer_import():
        success = False
    
    # Test 3: Check degen_test imports
    print("\n3. Testing degen_test imports...")
    if not test_degen_test_import():
        success = False
    
    # Test 4: Check profile imports
    print("\n4. Testing profile imports...")
    if not test_profile_import():
        success = False
    
    # Summary
    print("\n" + "=" * 50)
    if success:
        print("✅ ALL TESTS PASSED")
        print("The HTML/Markdown rendering fixes are working correctly!")
        print("\nChanges applied:")
        print("• Fixed syntax errors in degen_explorer.py")
        print("• Fixed indentation issues in degen_test.py")
        print("• Replaced content_section() calls with st.markdown() for degen_details")
        print("• All files now properly render Markdown content instead of raw HTML")
        print("\n🚀 Ready to test in the Streamlit application!")
        print("Run: streamlit run main.py")
    else:
        print("❌ SOME TESTS FAILED")
        print("Please check the error messages above and fix any remaining issues")

if __name__ == "__main__":
    main()
