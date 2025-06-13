print("Test started")
try:
    from utils.course_map import create_interactive_hierarchical_map
    print("✅ Import successful")
except Exception as e:
    print(f"❌ Import failed: {e}")
    import traceback
    traceback.print_exc()
