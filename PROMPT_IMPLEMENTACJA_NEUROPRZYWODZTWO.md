# PROMPT DO IMPLEMENTACJI STRUKTURY ĆWICZEŃ PRAKTYCZNYCH

## 🎯 ZADANIE: Implementacja nowej struktury lekcji - Ćwiczenia Praktyczne

**Cel:** Uprościć strukturę lekcji poprzez połączenie sekcji refleksji i zadań praktycznych w jedną sekcję "Ćwiczenia Praktyczne" z 4 pod-zakładkami, dostosowaną do tematyki neuroprzywództwa.

---

## 📋 WYMAGANIA IMPLEMENTACJI

### **1. STRUKTURA ZAKŁADEK**
Zaimplementuj 4 pod-zakładki w logicznej kolejności uczenia się:

1. **🧠 Autotest** - Testy samooceny i scenariusze decyzyjne
2. **🔍 Refleksja** - Pytania do autorefleksji i dziennik przywódcy  
3. **📊 Analiza** - Case studies, symulacje i analiza przypadków
4. **⚡ Wdrożenie** - Konkretne plany działania i implementacja

### **2. ZAWARTOŚĆ DOSTOSOWANA DO NEUROPRZYWÓDZTWA**

#### **🧠 Autotest:**
- Testy rozpoznawania stylów przywództwa
- Scenariusze decyzyjne w sytuacjach zespołowych
- Quiz samokontroli emocjonalnej lidera
- Ocena gotowości na wyzwania przywódcze

#### **🔍 Refleksja:**
- Analiza własnych doświadczeń przywódczych
- Dziennik rozwoju lidera (tygodniowe obserwacje)
- Samoocena kompetencji przywódczych w różnych obszarach
- Refleksja nad wpływem na zespół

#### **📊 Analiza:**
- Case studies wielkich liderów (pozytywne i negatywne przykłady)
- Symulacje kryzysowych sytuacji zarządczych
- Analiza własnych decyzji przywódczych pod kątem neuronauki
- Audyt stylu komunikacji z zespołem

#### **⚡ Wdrożenie:**
- Plan rozwoju kompetencji przywódczych
- Strategia budowania kultury zespołowej
- Narzędzia do lepszej komunikacji i motywacji
- System monitorowania postępów w przywództwie

---

## 🔧 IMPLEMENTACJA TECHNICZNA

### **KROK 1: Aktualizacja JSON lekcji**

Znajdź plik z danymi lekcji (prawdopodobnie w `data/lessons/`) i zastąp osobne sekcje `reflection` i `application` jedną sekcją:

```json
{
  "sections": {
    "practical_exercises": {
      "description": "Kompleksowe ćwiczenia praktyczne łączące autoanalizę i wdrożenie w kontekście neuroprzywództwa",
      "tabs": {
        "autotest": {
          "description": "🧠 **Autotest** - Testy samooceny, scenariusze decyzyjne i ocena kompetencji przywódczych",
          "sections": [
            {
              "title": "Test: Rozpoznawanie stylu przywództwa",
              "content": "Oceń swoje naturalne tendencje przywódcze...",
              "interactive": true
            }
            // ... więcej sekcji
          ]
        },
        "reflection": {
          "description": "🔍 **Refleksja** - Analiza doświadczeń, dziennik lidera i autorefleksja rozwojowa",
          "sections": [
            {
              "title": "Przywódczy Flashback",
              "content": "Przypomnij sobie sytuację, w której jako lider...",
              "interactive": true
            }
            // ... więcej sekcji
          ]
        },
        "analysis": {
          "description": "📊 **Analiza** - Case studies, symulacje i głęboka analiza zachowań przywódczych",
          "sections": [
            {
              "title": "Analiza przypadku: Lider w kryzysie",
              "content": "Przeanalizuj jak wielcy liderzy radzili sobie...",
              "interactive": true
            }
            // ... więcej sekcji
          ]
        },
        "implementation": {
          "description": "⚡ **Wdrożenie** - Konkretne plany działania, strategie i narzędzia rozwoju przywódczego",
          "sections": [
            {
              "title": "Plan rozwoju przywódczego",
              "content": "Stwórz swój osobisty plan rozwoju...",
              "interactive": true
            }
            // ... więcej sekcji
          ]
        }
      }
    }
  }
}
```

### **KROK 2: Aktualizacja logiki w pliku lesson.py**

Znajdź plik obsługujący wyświetlanie lekcji i dodaj obsługę nowej struktury:

```python
# W funkcji obsługującej kroki lekcji, dodaj:
elif st.session_state.lesson_step == 'practical_exercises':
    practical_data = lesson['sections']['practical_exercises']
    
    if 'tabs' in practical_data:
        sub_tabs_data = practical_data['tabs']
        available_tabs = []
        tab_keys = []
        
        # Logiczna kolejność: Test → Refleksja → Analiza → Akcja
        if 'autotest' in sub_tabs_data:
            available_tabs.append("🧠 Autotest")
            tab_keys.append('autotest')
        
        if 'reflection' in sub_tabs_data:
            available_tabs.append("🔍 Refleksja")
            tab_keys.append('reflection')
        
        if 'analysis' in sub_tabs_data:
            available_tabs.append("📊 Analiza")
            tab_keys.append('analysis')
        
        if 'implementation' in sub_tabs_data:
            available_tabs.append("⚡ Wdrożenie")
            tab_keys.append('implementation')
        
        if available_tabs:
            tabs = st.tabs(available_tabs)
            
            for i, (tab_key, tab_title) in enumerate(zip(tab_keys, available_tabs)):
                with tabs[i]:
                    tab_data = sub_tabs_data[tab_key]
                    
                    if 'description' in tab_data:
                        st.info(tab_data['description'])
                    
                    if 'sections' in tab_data:
                        for section in tab_data['sections']:
                            st.markdown(f"### {section.get('title', 'Sekcja')}")
                            st.markdown(section.get('content', 'Brak treści'), unsafe_allow_html=True)
                            
                            if section.get('interactive', False):
                                section_key = f"practical_{tab_key}_{section.get('title', '').replace(' ', '_').lower()}"
                                
                                with st.form(key=f"form_{section_key}"):
                                    existing_response = st.session_state.get(section_key, "")
                                    
                                    user_response = st.text_area(
                                        "Twoja odpowiedź:",
                                        value=existing_response,
                                        height=200,
                                        key=f"input_{section_key}"
                                    )
                                    
                                    submitted = st.form_submit_button("Zapisz odpowiedź")
                                    
                                    if submitted:
                                        st.session_state[section_key] = user_response
                                        st.success("Twoja odpowiedź została zapisana!")
```

### **KROK 3: Aktualizacja nawigacji i XP**

```python
# W definicji kroków lekcji:
step_names = {
    'intro': 'Wprowadzenie',
    'opening_quiz': 'Diagnoza początkowa',
    'content': 'Materiał',
    'practical_exercises': 'Ćwiczenia praktyczne',  # Nowa nazwa
    'closing_quiz': 'Quiz końcowy',
    'summary': 'Podsumowanie'
}

# W systemie XP:
step_xp_values = {
    'intro': int(base_xp * 0.05),
    'opening_quiz': int(base_xp * 0.00),
    'content': int(base_xp * 0.30),
    'practical_exercises': int(base_xp * 0.40),  # 40% XP za całą sekcję
    'closing_quiz': int(base_xp * 0.20),
    'summary': int(base_xp * 0.05)
}

# W logice kolejności kroków:
if 'practical_exercises' in lesson.get('sections', {}):
    available_steps.append('practical_exercises')
else:
    # Backward compatibility
    if 'reflection' in lesson.get('sections', {}):
        available_steps.append('reflection')
    if 'application' in lesson.get('sections', {}):
        available_steps.append('application')
```

---

## 🎨 DOSTOSOWANIE DO NEUROPRZYWÓDZTWA

### **Przykłady treści do sekcji:**

#### **🧠 Autotest - Przykładowe sekcje:**
1. **"Test neurotypów przywódczych"** - Określenie naturalnego stylu zarządzania
2. **"Scenariusz: Konflikt w zespole"** - Jak zareagowałbyś jako lider?
3. **"Samoocena inteligencji emocjonalnej"** - Ocena kompetencji EQ

#### **🔍 Refleksja - Przykładowe sekcje:**
1. **"Moje największe wyzwanie przywódcze"** - Analiza trudnej sytuacji
2. **"Dziennik wpływu na zespół"** - Cotygodniowe obserwacje
3. **"Ewolucja mojego stylu przywództwa"** - Jak się zmieniałem?

#### **📊 Analiza - Przykładowe sekcje:**
1. **"Case study: Steve Jobs vs. Tim Cook"** - Różne style, podobne sukcesy
2. **"Symulacja: Reorganizacja zespołu"** - Jak poprowadzić zmiany?
3. **"Analiza mojej komunikacji"** - Audit stylu zarządzania

#### **⚡ Wdrożenie - Przykładowe sekcje:**
1. **"90-dniowy plan rozwoju przywódczego"** - Konkretne działania
2. **"Toolkit motywacji zespołu"** - Praktyczne narzędzia
3. **"System feedbacku i mentoringu"** - Jak budować kulturę rozwoju

---

## 🚀 PLAN WDROŻENIA

### **Faza 1: Przygotowanie**
1. Zidentyfikuj plik z danymi lekcji do modyfikacji
2. Stwórz backup istniejącej struktury
3. Przygotuj treści dostosowane do neuroprzywództwa

### **Faza 2: Implementacja**
1. Zaktualizuj JSON z danymi lekcji
2. Zmodyfikuj logikę renderowania w lesson.py
3. Dostosuj system nawigacji i XP

### **Faza 3: Testowanie**
1. Przetestuj wszystkie 4 pod-zakładki
2. Sprawdź zapisy odpowiedzi użytkowników
3. Zweryfikuj przyznawanie XP

### **Faza 4: Dopracowanie**
1. Dostosuj treści do kontekstu aplikacji
2. Przetestuj UX na różnych urządzeniach
3. Sprawdź kompatybilność wsteczną

---

## ✅ CHECKLIST IMPLEMENTACJI

- [ ] Zaktualizowano JSON lekcji z nową strukturą `practical_exercises`
- [ ] Zaimplementowano obsługę 4 pod-zakładek w lesson.py
- [ ] Dostosowano kolejność: Autotest → Refleksja → Analiza → Wdrożenie
- [ ] Zaktualizowano system nawigacji i nazwy kroków
- [ ] Skonfigurowano XP (40% za całą sekcję praktyczną)
- [ ] Dodano obsługę interaktywnych formularzy
- [ ] Przygotowano treści dostosowane do neuroprzywództwa
- [ ] Przetestowano funkcjonalność na przykładowej lekcji
- [ ] Sprawdzono kompatybilność wsteczną ze starymi lekcjami
- [ ] Zweryfikowano działanie na różnych urządzeniach

---

## 🎯 OCZEKIWANE REZULTATY

Po implementacji użytkownicy będą mieli:
- **Bardziej logiczną progresję uczenia się** (od diagnozy do działania)
- **Skoncentrowaną sekcję praktyczną** zamiast rozproszonych elementów
- **Bogate, interaktywne doświadczenie** dostosowane do neuroprzywództwa
- **Lepszy UX** dzięki przemyślanej strukturze pod-zakładek

**Status docelowy: Uproszczona, ale bogatsza struktura lekcji z focus na praktyczne zastosowanie wiedzy o neuroprzywództwie.**
