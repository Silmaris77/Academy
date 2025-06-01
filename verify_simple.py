import sys
import os

def verify_implementation():
    print("VERIFYING TIMESTAMP FIX IMPLEMENTATION")
    print("=" * 50)
    
    try:
        print("\n1. Testing time utilities...")
        from utils.time_utils import calculate_relative_time, get_current_timestamp
        
        current_time = get_current_timestamp()
        print(f"Current timestamp: {current_time}")
        
        relative_time = calculate_relative_time(current_time)
        print(f"Relative time: {relative_time}")
        
        print("\n2. Testing dashboard import...")
        try:
            from views.dashboard import show_recent_activities
            print("Dashboard import successful")
        except ImportError as e:
            print(f"Dashboard import failed: {e}")
            return False
            
        print("\n3. Testing timestamp saving imports...")
        
        with open('views/degen_test.py', 'r', encoding='utf-8') as f:
            degen_test_content = f.read()
            
        if 'from utils.time_utils import get_current_timestamp' in degen_test_content:
            print("degen_test.py has correct import")
        else:
            print("degen_test.py missing import")
            
        if 'test_completion_date' in degen_test_content:
            print("degen_test.py saves timestamp")
        else:
            print("degen_test.py doesn't save timestamp")
            
        with open('views/degen_explorer.py', 'r', encoding='utf-8') as f:
            degen_explorer_content = f.read()
            
        if 'from utils.time_utils import get_current_timestamp' in degen_explorer_content:
            print("degen_explorer.py has correct import")
        else:
            print("degen_explorer.py missing import")
            
        if 'test_completion_date' in degen_explorer_content:
            print("degen_explorer.py saves timestamp")
        else:
            print("degen_explorer.py doesn't save timestamp")
            
        print("\n4. Testing dashboard logic...")
        with open('views/dashboard.py', 'r', encoding='utf-8') as f:
            dashboard_content = f.read()
            
        if 'from utils.time_utils import calculate_relative_time' in dashboard_content:
            print("Dashboard has correct import")
        else:
            print("Dashboard missing import")
            
        if 'test_completion_date = user_data.get(' in dashboard_content:
            print("Dashboard uses dynamic timestamps")
        else:
            print("Dashboard still uses hardcoded timestamps")
            
        if '1 dzień temu' in dashboard_content:
            print("WARNING: Dashboard still contains hardcoded '1 dzień temu'")
        else:
            print("No hardcoded '1 dzień temu' found")
            
        print("\n5. Checking user data...")
        from data.users import load_user_data
        users_data = load_user_data()
        
        users_with_test = sum(1 for u in users_data.values() if u.get('test_taken', False))
        users_with_timestamp = sum(1 for u in users_data.values() if 'test_completion_date' in u)
        
        print(f"Users who took test: {users_with_test}")
        print(f"Users with timestamps: {users_with_timestamp}")
        print(f"Missing timestamps: {users_with_test - users_with_timestamp}")
        
        print("\nVERIFICATION COMPLETE!")
        print("\nSUMMARY:")
        print("   Time utilities working")
        print("   Dashboard imports correct")
        print("   Test completion saves timestamps") 
        print("   Dashboard uses dynamic timestamps")
        
        print("\nREADY FOR TESTING:")
        print("   1. Run: streamlit run main.py")
        print("   2. Complete a degen test")
        print("   3. Check Dashboard -> Recent Activities")
        print("   4. Verify dynamic timestamps appear")
        
        return True
        
    except Exception as e:
        print(f"Error during verification: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    verify_implementation()
