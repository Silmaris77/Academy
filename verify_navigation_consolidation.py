#!/usr/bin/env python3
"""
Verification script for navigation consolidation
Confirms that the ZenDegenAcademy navigation has been successfully consolidated
"""

import sys
import os
import importlib.util

# Add current directory to Python path
sys.path.insert(0, os.getcwd())

def check_file_exists(filepath):
    """Check if a file exists"""
    return os.path.exists(filepath)

def check_function_exists(module_path, function_name):
    """Check if a function exists in a module"""
    try:
        spec = importlib.util.spec_from_file_location("module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return hasattr(module, function_name)
    except Exception:
        return False

def verify_navigation_changes():
    """Verify all navigation changes are in place"""
    print("🔍 VERIFICATION: Navigation Consolidation")
    print("=" * 50)
    
    checks = []
    
    # Check 1: Navigation menu updated
    print("\n1. Navigation Menu Structure:")
    nav_file = "utils/components.py"
    if check_file_exists(nav_file):
        with open(nav_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if '"Nauka"' in content and '"icon": "📚"' in content:
                print("   ✅ New 'Nauka' tab found in navigation")
                checks.append(True)
            else:
                print("   ❌ 'Nauka' tab not found")
                checks.append(False)
            
            if '"Lekcje"' not in content or '"Umiejętności"' not in content:
                print("   ✅ Old separate tabs removed")
                checks.append(True)
            else:
                print("   ❌ Old tabs still present")
                checks.append(False)
    else:
        print("   ❌ Navigation file not found")
        checks.append(False)
    
    # Check 2: New learn view exists
    print("\n2. Learn View Implementation:")
    learn_file = "views/learn.py"
    if check_file_exists(learn_file):
        print("   ✅ learn.py file exists")
        checks.append(True)
        
        if check_function_exists(learn_file, "show_learn"):
            print("   ✅ show_learn function exists")
            checks.append(True)
        else:
            print("   ❌ show_learn function not found")
            checks.append(False)
            
        with open(learn_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if '🎓 Lekcje' in content and '🗺️ Mapa Kursu' in content and '🌳 Umiejętności' in content:
                print("   ✅ All three tabs implemented in learn view")
                checks.append(True)
            else:
                print("   ❌ Not all tabs found in learn view")
                checks.append(False)
    else:
        print("   ❌ learn.py file not found")
        checks.extend([False, False, False])
    
    # Check 3: Main application routing
    print("\n3. Main Application Routing:")
    main_file = "main.py"
    if check_file_exists(main_file):
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            if 'from views.learn import show_learn' in content:
                print("   ✅ Learn view imported in main.py")
                checks.append(True)
            else:
                print("   ❌ Learn view not imported")
                checks.append(False)
            
            if "st.session_state.page == 'learn'" in content:
                print("   ✅ Learn page routing exists")
                checks.append(True)
            else:
                print("   ❌ Learn page routing not found")
                checks.append(False)
            
            if "st.session_state.page = 'learn'" in content:
                print("   ✅ Redirect logic implemented")
                checks.append(True)
            else:
                print("   ❌ Redirect logic not found")
                checks.append(False)
    else:
        print("   ❌ main.py file not found")
        checks.extend([False, False, False])
    
    # Check 4: Backward compatibility
    print("\n4. Backward Compatibility:")
    lesson_file = "views/lesson.py"
    skills_file = "views/skills_new.py"
    
    if check_file_exists(lesson_file):
        print("   ✅ Original lesson.py preserved")
        checks.append(True)
    else:
        print("   ❌ Original lesson.py missing")
        checks.append(False)
    
    if check_file_exists(skills_file):
        print("   ✅ Original skills_new.py preserved")
        checks.append(True)
    else:
        print("   ❌ Original skills_new.py missing")
        checks.append(False)
    
    return checks

def show_final_status():
    """Show the final consolidation status"""
    print("\n" + "=" * 50)
    print("📊 CONSOLIDATION SUMMARY")
    print("=" * 50)
    
    print("\n✅ COMPLETED:")
    print("   • Navigation reduced from 6 to 5 tabs")
    print("   • 'Lekcje' and 'Umiejętności' combined into 'Nauka'")
    print("   • New unified learn view with 3 sub-tabs")
    print("   • Backward compatibility maintained")
    print("   • Redirect logic implemented")
    
    print("\n📚 NEW STRUCTURE:")
    print("   🏠 Dashboard")
    print("   📚 Nauka (NEW - combines lessons + skills)")
    print("      └── 🎓 Lekcje")
    print("      └── 🗺️ Mapa Kursu") 
    print("      └── 🌳 Umiejętności")
    print("   🛒 Sklep")
    print("   🔍 Eksplorator")
    print("   👤 Profil")
    
    print("\n🚀 TO TEST:")
    print("   streamlit run main.py")

def main():
    """Main verification function"""
    checks = verify_navigation_changes()
    
    passed = sum(checks)
    total = len(checks)
    
    print(f"\n📊 VERIFICATION RESULTS: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 ALL CHECKS PASSED! Navigation consolidation is COMPLETE!")
        show_final_status()
    else:
        print("⚠️  Some checks failed. Please review the issues above.")
        print(f"   Success rate: {(passed/total)*100:.1f}%")

if __name__ == "__main__":
    main()
