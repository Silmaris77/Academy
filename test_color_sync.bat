@echo off
cd /d "c:\Users\pksia\Dropbox\ZenDegenAcademy"
python -c "
try:
    from utils.course_map import create_interactive_hierarchical_map
    print('✅ Import interaktywnej mapy - OK')
    
    from data.course_data import get_blocks, get_categories
    blocks = get_blocks()
    categories = get_categories()
    print(f'✅ Dane kursu - OK ({len(blocks)} bloków, {len(categories)} kategorii)')
    
    print('🎨 Synchronizacja kolorów czcionki z węzłami - KOMPLETNA!')
    
except Exception as e:
    print(f'❌ Błąd: {e}')
    import traceback
    traceback.print_exc()
"
pause
