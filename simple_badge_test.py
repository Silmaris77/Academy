#!/usr/bin/env python3
"""
Simple test to verify BadgeDisplaySystem import
"""

try:
    from utils.badge_display import BadgeDisplaySystem
    print("✅ BadgeDisplaySystem imported successfully")
    
    # Try to initialize it
    system = BadgeDisplaySystem()
    print("✅ BadgeDisplaySystem initialized successfully")
    
    # Check if it has the expected methods
    methods = ['render_enhanced_badge_section', 'add_enhanced_badge_styles']
    for method in methods:
        if hasattr(system, method):
            print(f"✅ Method {method} found")
        else:
            print(f"❌ Method {method} not found")
    
    print("\n🎉 Badge Display System is ready!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
