# 🎨 Prototypy i Demonstracje ZenDegenAcademy

Ten folder zawiera wszystkie prototypy HTML, demonstracje UI/UX i propozycje designu dla projektu ZenDegenAcademy.

## 📁 Struktura prototypów

### 🧭 `/navigation/` - Prototypy nawigacji
- **navigation_prototype.html** - Podstawowy prototyp nowej nawigacji
- **navigation_prototype_fixed.html** - Poprawiona wersja nawigacji
- **mobile_layout_variants.html** - Różne warianty layoutu mobilnego

### 🎛️ `/ui-components/` - Komponenty UI
- **quiz_button_test.html** - Test przycisków quiz
- **quiz_button_types_demo.html** - Demonstracja różnych typów przycisków
- **selective_quiz_buttons_demo.html** - Demo selektywnych przycisków quiz
- **new_quiz_buttons_demo.html** - Nowe wersje przycisków quiz

### 🎮 `/demos/` - Demonstracje funkcji
- **practical_exercises_demo.html** - Demo ćwiczeń praktycznych
- **course_map_integration_demo.html** - Demo integracji mapy kursu

### 💡 `/proposals/` - Propozycje architektoniczne
- **app_structure_proposals.html** - Propozycje nowej struktury aplikacji

## 🎯 Przeznaczenie i użycie

### Dla deweloperów UI/UX 🎨
- **Szybkie prototypowanie** - Testowanie pomysłów bez Streamlit
- **Visual reference** - Wzorce designu do implementacji
- **Component library** - Referencje dla komponentów

### Dla stakeholderów 👥
- **Demo funkcji** - Pokazanie konceptów przed implementacją
- **Design review** - Dyskusja nad zmianami UI
- **User testing** - Testy użyteczności prototypów

### Dla QA 🧪
- **Expected behavior** - Jak powinny działać komponenty
- **Visual regression testing** - Porównania designu
- **Cross-browser testing** - Testy prototypów

## 🚀 Jak otwierać prototypy

### Lokalne otwieranie:
```bash
# Windows
start prototypes/navigation/navigation_prototype.html

# macOS
open prototypes/navigation/navigation_prototype.html

# Linux
xdg-open prototypes/navigation/navigation_prototype.html
```

### Serwer deweloperski:
```bash
# Python simple server
cd prototypes
python -m http.server 8000

# Node.js serve
npx serve prototypes

# Live Server (VS Code extension)
# Kliknij prawym przyciskiem myszy na plik HTML → "Open with Live Server"
```

## 📋 Status prototypów

### ✅ Aktywne prototypy (do konsultacji):
- `app_structure_proposals.html` - **PRIORYTET** - decyzje o strukturze
- `navigation_prototype_fixed.html` - Poprawiona nawigacja
- `mobile_layout_variants.html` - Layouty mobilne

### 🔄 W rozwoju:
- `course_map_integration_demo.html` - Integracja map
- `practical_exercises_demo.html` - Ćwiczenia praktyczne

### 🗄️ Archiwalne (zrealizowane):
- `quiz_button_*.html` - Zaimplementowane w Streamlit
- `navigation_prototype.html` - Zastąpiony wersją fixed

## 🔧 Maintenance prototypów

### Dodawanie nowych prototypów:
1. **Utwórz plik** w odpowiednim folderze tematycznym
2. **Dodaj dokumentację** - cel, status, screenshot
3. **Zaktualizuj README** - dodaj do listy
4. **Oznacz status** - aktywny/archiwalne/deprecated

### Archiwizacja:
- Przenieś stare prototypy do `archived/` (jeśli potrzebne)
- Lub usuń po potwierdzeniu implementacji
- Zachowaj tylko referencyjne

## 🎨 Standardy prototypów

### CSS Framework: 
- Używaj nowoczesnego CSS (Grid, Flexbox)
- Mobile-first approach
- Spójne zmienne kolorów

### Responsive Design:
- Testuj na różnych rozdzielczościach
- Graceful degradation
- Touch-friendly (min 44px buttons)

### Accessibility:
- Semantic HTML
- Proper contrast ratios
- Keyboard navigation
- Screen reader friendly

## 🔗 Integracja z główną aplikacją

### Z prototypu do Streamlit:
1. **Ekstraktuj CSS** → `static/css/`
2. **Komponent logic** → `utils/components.py`
3. **Test implementacji** → porównaj z prototypem
4. **Responsive check** → mobile compatibility

### Feedback loop:
- Prototyp → Implementacja → User feedback → Iteracja prototypu

---

## 📊 Przegląd prototypów

| Kategoria | Plików | Status | Priorytet |
|-----------|--------|--------|-----------|
| Navigation | 3 | ✅ Aktywne | Wysoki |
| UI Components | 4 | 🗄️ Zrealizowane | Niski |
| Demos | 2 | 🔄 W rozwoju | Średni |
| Proposals | 1 | ✅ Aktywne | **BARDZO WYSOKI** |

---

*Dokumentacja prototypów automatycznie wygenerowana - 2025-06-22*

**🎯 Katalog główny jest teraz znacznie czystszy dzięki organizacji prototypów!** ✨
