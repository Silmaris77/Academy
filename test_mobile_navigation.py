"""
Mobile Navigation Test Script
Tests the mobile navigation implementation and CSS changes
"""

import sys
import os

# Add the app directory to Python path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.append(APP_DIR)

def test_mobile_navigation_css():
    """Test that mobile navigation CSS has been properly updated"""
    css_file = os.path.join(APP_DIR, 'static', 'css', 'mobile-navigation.css')
    
    if not os.path.exists(css_file):
        print("❌ Mobile navigation CSS file not found!")
        return False
    
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Check for our icon-only optimizations
    checks = [
        ('height: 50px', 'Navigation bar height reduced'),
        ('min-width: 40px', 'Navigation items width reduced'),
        ('font-size: 1.2rem', 'Icon size optimized'),
        ('display: none', 'Labels hidden for icon-only view'),
        ('margin-bottom: 0', 'Icon margin optimized')
    ]
    
    results = []
    for check, description in checks:
        if check in css_content:
            print(f"✅ {description}: Found '{check}'")
            results.append(True)
        else:
            print(f"❌ {description}: Missing '{check}'")
            results.append(False)
    
    return all(results)

def test_app_structure():
    """Test that required files exist for mobile navigation"""
    required_files = [
        'static/css/mobile-navigation.css',
        'static/js/mobile-navigation.js',
        'utils/mobile_navigation.py',
        'main.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = os.path.join(APP_DIR, file_path)
        if os.path.exists(full_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - Missing!")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def main():
    """Run mobile navigation tests"""
    print("🔍 Mobile Navigation Test Suite")
    print("=" * 50)
    
    print("\n📁 Testing app structure...")
    structure_ok = test_app_structure()
    
    print("\n🎨 Testing CSS optimizations...")
    css_ok = test_mobile_navigation_css()
    
    print("\n📱 Testing HTML test file...")
    test_file = os.path.join(APP_DIR, 'mobile_nav_test.html')
    test_file_exists = os.path.exists(test_file)
    
    if test_file_exists:
        print(f"✅ Test file created: {test_file}")
    else:
        print(f"❌ Test file missing: {test_file}")
    
    print("\n" + "=" * 50)
    print("📊 RESULTS SUMMARY:")
    print(f"App Structure: {'✅ PASS' if structure_ok else '❌ FAIL'}")
    print(f"CSS Optimizations: {'✅ PASS' if css_ok else '❌ FAIL'}")
    print(f"Test File: {'✅ PASS' if test_file_exists else '❌ FAIL'}")
    
    if structure_ok and css_ok and test_file_exists:
        print("\n🎉 All tests passed! Mobile navigation is ready!")
        print("\n📋 Next steps:")
        print("1. Open mobile_nav_test.html in browser")
        print("2. Use browser dev tools to simulate mobile view")
        print("3. Verify only icons are visible (no labels)")
        print("4. Test navigation interactions")
        print("5. Run the main Streamlit app to test integration")
        return True
    else:
        print("\n⚠️ Some tests failed. Check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
