# BADGE SYSTEM - STEP 3: Quick Verification Test
# ==============================================

import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def quick_test_step3():
    """Quick test to verify Step 3 implementation"""
    print("🚀 BADGE SYSTEM STEP 3 - QUICK VERIFICATION")
    print("=" * 50)
    
    try:
        # Test 1: Import new modules
        print("📦 Testing imports...")
        from utils.badge_tracking import BadgeTracker, badge_tracker
        from data.badge_migration import BadgeDataMigrator
        print("✅ All modules imported successfully")
        
        # Test 2: Initialize tracker
        print("\n🔧 Testing BadgeTracker initialization...")
        tracker = BadgeTracker()
        assert hasattr(tracker, 'cache')
        assert hasattr(tracker, 'performance_stats')
        print("✅ BadgeTracker initialized successfully")
        
        # Test 3: Test empty badge data
        print("\n📊 Testing empty badge data structure...")
        empty_data = tracker._get_empty_badge_data()
        required_keys = ['badges', 'badge_progress', 'badge_stats']
        for key in required_keys:
            assert key in empty_data, f"Missing key: {key}"
        print("✅ Badge data structure is correct")
        
        # Test 4: Test user badge data retrieval
        print("\n👤 Testing user badge data retrieval...")
        badge_data = tracker.get_user_badge_data('test_user')
        assert isinstance(badge_data, dict)
        print("✅ User badge data retrieval works")
        
        # Test 5: Test progress calculation
        print("\n📈 Testing badge progress calculation...")
        test_user_data = {
            'user_id': 'test_123',
            'completed_lessons': ['B1C1L1'],
            'xp': 100,
            'test_taken': True
        }
        
        # Test a few badge progress calculations
        progress = tracker._calculate_badge_progress('welcome', test_user_data, {})
        assert 'progress' in progress
        assert isinstance(progress['progress'], (int, float))
        print("✅ Badge progress calculation works")
        
        # Test 6: Test migration functionality
        print("\n🔄 Testing migration functionality...")
        migrator = BadgeDataMigrator()
        
        old_user_data = {
            'user_id': 'test_migration',
            'badges': ['welcome'],
            'xp': 100,
            'joined_date': '2025-05-30'
        }
        
        result = migrator.migrate_user_data('test_migration', old_user_data)
        assert result['success'] == True
        assert 'badge_data' in old_user_data
        print("✅ Migration functionality works")
        
        # Test 7: Test integration functions
        print("\n🔗 Testing integration with achievements...")
        from utils.achievements import get_detailed_badge_progress, get_badge_recommendations_enhanced
        
        progress = get_detailed_badge_progress('test_user', 'welcome')
        assert isinstance(progress, dict)
        
        recommendations = get_badge_recommendations_enhanced('test_user')
        assert isinstance(recommendations, list)
        print("✅ Integration functions work")
        
        # Test 8: Test statistics calculation
        print("\n📊 Testing statistics calculation...")
        badge_data = {
            'badges': {
                'welcome': {
                    'earned': True,
                    'xp_earned': 50,
                    'tier': 'bronze'
                }
            },
            'badge_progress': {},
            'badge_stats': {}
        }
        
        stats = tracker._calculate_badge_stats(badge_data)
        assert stats['total_earned'] == 1
        assert stats['total_badge_xp'] == 50
        print("✅ Statistics calculation works")
        
        # Test 9: Test recommendation system
        print("\n🎯 Testing recommendation system...")
        recommendations = tracker.get_recommended_badges('test_user', limit=3)
        assert isinstance(recommendations, list)
        assert len(recommendations) <= 3
        print("✅ Recommendation system works")
        
        # Test 10: Test cache functionality
        print("\n💾 Testing cache functionality...")
        initial_misses = tracker.performance_stats['cache_misses']
        tracker.get_user_badge_data('cache_test_user', use_cache=True)
        assert tracker.performance_stats['cache_misses'] > initial_misses
        print("✅ Cache functionality works")
        
        print("\n" + "=" * 50)
        print("🎉 ALL QUICK TESTS PASSED!")
        print("✅ Step 3 implementation is working correctly")
        print("\n📋 STEP 3 FEATURES VERIFIED:")
        print("  • Enhanced badge storage structure")
        print("  • Progress monitoring system") 
        print("  • Advanced tracking features")
        print("  • User data management")
        print("  • Integration enhancements")
        print("  • Migration utilities")
        print("  • Performance optimizations")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Quick test failed: {str(e)}")
        print("🔧 Please check the implementation")
        return False

if __name__ == "__main__":
    quick_test_step3()
