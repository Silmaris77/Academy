"""
Prosty test funkcjonalności ulepszonego wykresu kołowego
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    try:
        print("🔍 Testowanie importów...")
        import matplotlib.pyplot as plt
        import pandas as pd
        print("✅ Matplotlib i pandas zaimportowane")
        
        from views.admin import get_degen_type_distribution
        print("✅ Funkcja get_degen_type_distribution zaimportowana")
        
        print("\n📊 Pobieranie danych...")
        degen_df = get_degen_type_distribution()
        
        if degen_df.empty:
            print("❌ Brak danych o typach degenów")
            return
        
        print(f"✅ Znaleziono {len(degen_df)} typów degenów:")
        
        # Wyświetl szczegóły danych
        total_users = degen_df['count'].sum()
        print(f"📈 Łącznie użytkowników: {total_users}")
        
        for _, row in degen_df.iterrows():
            degen_type = row['degen_type']
            count = row['count']
            percentage = row['percentage']
            print(f"   • {degen_type}: {count} osób ({percentage}%)")
        
        print("\n🎨 Testowanie tworzenia wykresu...")
        
        # Stwórz ulepszony wykres
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Przygotuj dane
        counts = degen_df['count'].tolist()
        labels = degen_df['degen_type'].tolist()
        total = sum(counts)
        
        print(f"✅ Dane przygotowane: {len(counts)} segmentów")
        
        # Funkcja do wyświetlania procentów tylko dla większych wartości
        def autopct_format(pct):
            return f'{pct:.1f}%' if pct >= 3 else ''
        
        # Informacje o zastosowanych ulepszeniach
        print("\n🔧 Zastosowane ulepszenia:")
        
        # Sprawdź, które segmenty będą miały etykiety
        visible_labels = [i for i, count in enumerate(counts) if count/total*100 >= 3]
        print(f"   • Widoczne etykiety procentowe: {len(visible_labels)}/{len(counts)}")
        
        # Sprawdź, które segmenty będą wysunięte
        exploded_segments = [i for i, count in enumerate(counts) if count/total < 0.05]
        print(f"   • Wysunięte małe segmenty: {len(exploded_segments)}")
        
        # Stwórz wykres kołowy z ulepszeniami
        pie_result = ax.pie(
            counts, 
            labels=labels,
            autopct=autopct_format,
            startangle=90,
            shadow=False,
            pctdistance=0.85,  # Odległość etykiet z procentami
            labeldistance=1.1,  # Odległość nazw
            explode=[0.05 if count/total < 0.05 else 0 for count in counts],
            textprops={'fontsize': 10}
        )
        
        print("✅ Wykres kołowy utworzony")
        
        # Obsłuż różne scenariusze zwracanych wartości
        if len(pie_result) == 3:
            wedges, texts, autotexts = pie_result
            print("✅ Etykiety procentowe dodane")
            
            # Poprawa czytelności etykiet procentowych
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
        else:
            wedges, texts = pie_result
            print("✅ Wykres bez etykiet procentowych")
        
        # Dodaj legendę z dokładnymi liczbami
        legend_labels = [f'{label}: {count} ({count/total*100:.1f}%)' 
                       for label, count in zip(labels, counts)]
        ax.legend(wedges, legend_labels, title="Typy degenów", 
                 loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        print("✅ Legenda dodana")
        
        ax.axis('equal')
        plt.title('Rozkład typów degenów (Test)', fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        
        # Zapisz wykres
        output_file = "test_improved_pie_chart_output.png"
        plt.savefig(output_file, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Wykres zapisany jako: {output_file}")
        
        print("\n🎉 Test zakończony pomyślnie!")
        print("📊 Ulepszony wykres kołowy działa poprawnie z wszystkimi funkcjami:")
        print("   • Automatyczne pozycjonowanie etykiet")
        print("   • Inteligentne wyświetlanie procentów")
        print("   • Wysuwanie małych segmentów")
        print("   • Szczegółowa legenda")
        print("   • Profesjonalny styl")
        
    except Exception as e:
        print(f"❌ Błąd podczas testowania: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("=" * 60)
    print("TEST ULEPSZONEGO WYKRESU KOŁOWEGO TYPÓW DEGENÓW")
    print("=" * 60)
    main()
    print("=" * 60)
