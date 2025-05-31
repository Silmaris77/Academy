import streamlit as st

# Page configuration
PAGE_CONFIG = {
    "page_title": "DegApp",  # zakładam, że to są aktualne ustawienia
    "page_icon": "🧘‍♂️",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
}

# XP levels configuration
XP_LEVELS = {
    1: 0,
    2: 100,
    3: 250,
    4: 500,
    5: 1000,
    6: 2000,
    7: 3500,
    8: 5000,
    9: 7500,
    10: 10000
}

# CSS styles moved to static/css/style.css
# This variable is kept for backward compatibility
APP_STYLES = """
<style>
    /* CSS styles are now in static/css/style.css */
    /* This is kept for backward compatibility */
</style>
"""

# Daily missions configuration
DAILY_MISSIONS = [
    {"title": "Medytacja mindfulness", "description": "Wykonaj 10-minutową medytację uważności", "xp": 50, "badge": "🧘‍♂️"},
    {"title": "Analiza rynku", "description": "Przeanalizuj jeden projekt/token przez 30 minut", "xp": 70, "badge": "📊"},
    {"title": "Przegląd portfela", "description": "Dokonaj przeglądu swojego portfela i strategii", "xp": 60, "badge": "💼"},
    {"title": "Dziennik inwestora", "description": "Zapisz swoje decyzje i emocje z dzisiejszego dnia", "xp": 40, "badge": "📓"},
    {"title": "Nowa wiedza", "description": "Przeczytaj artykuł/raport o rynku lub psychologii inwestowania", "xp": 30, "badge": "🧠"}
]

# User avatar options
USER_AVATARS = {
    "default": "👤",
    "zen": "🧘‍♂️",
    "yolo": "🚀",
    "emo": "😭",
    "strategist": "🎯",
    "scientist": "🔬",
    "spreadsheet": "📊",
    "meta": "🔄",
    "hype": "📣"
}

# Theme options
THEMES = {
    "default": {
        "primary": "#2980B9",
        "secondary": "#6DD5FA",
        "accent": "#27ae60",
        "background": "#f7f7f7",
        "card": "#ffffff"
    },
    "dark": {
        "primary": "#3498db",
        "secondary": "#2c3e50",
        "accent": "#e74c3c",
        "background": "#1a1a1a",
        "card": "#2d2d2d"
    },
    "zen": {
        "primary": "#4CAF50",
        "secondary": "#8BC34A",
        "accent": "#009688",
        "background": "#f9f9f9",
        "card": "#ffffff"
    },
    "yolo": {
        "primary": "#FF5722",
        "secondary": "#FF9800",
        "accent": "#FFEB3B",
        "background": "#f5f5f5",
        "card": "#ffffff"
    },
    "emo": {
        "primary": "#9C27B0",
        "secondary": "#673AB7",
        "accent": "#E91E63",
        "background": "#f0f0f0",
        "card": "#ffffff"
    }
}

# Degen types
DEGEN_TYPES = {
    "Zen Degen": {
        "icon": "🧘", 
        "color": "#4CAF50", 
        "theme": "zen", 
        "description": "Dąży do równowagi i spokoju nawet w zmiennych warunkach rynkowych. Kontroluje emocje i podejmuje świadome decyzje.",
        "strengths": ["Spokój i kontrola nad emocjami", "Świadome podejmowanie decyzji", "Odporność na wahania rynku"],
        "challenges": ["Może być zbyt ostrożny", "Czasem trudno mu wykorzystać nagłe okazje", "Może przeoczyć niektóre trendy"],
        "strategy": "Długoterminowe strategie oparte na solidnej analizie fundamentalnej i zrównoważonym podejściu do ryzyka."
    },
    "YOLO Degen": {
        "icon": "🚀", 
        "color": "#FF5722", 
        "theme": "yolo", 
        "description": "Dynamiczny inwestor kierujący się intuicją i chęcią maksymalizacji zysków. Nie boi się podejmować ryzykownych decyzji.",
        "strengths": ["Szybkie podejmowanie decyzji", "Zdolność dostrzegania nowych okazji", "Odwaga i determinacja"],
        "challenges": ["Podatność na działanie pod wpływem emocji", "Ryzyko dużych strat", "Brak długoterminowej strategii"],
        "strategy": "Strategia bazująca na szybkich decyzjach i wykorzystywaniu krótkoterminowych trendów. Wymaga dyscypliny w zarządzaniu ryzykiem."
    },
    "Emo Degen": {
        "icon": "😭", 
        "color": "#9C27B0", 
        "theme": "emo", 
        "description": "Inwestor silnie reagujący emocjonalnie na zmiany rynkowe. Intensywnie przeżywa zarówno zyski jak i straty.",
        "strengths": ["Entuzjazm i zaangażowanie", "Umiejętność szybkiej adaptacji", "Intuicja społeczna"],
        "challenges": ["Decyzje pod wpływem strachu lub euforii", "Trudności z trzymaniem się planu", "Stres związany z inwestowaniem"],
        "strategy": "Strukturyzowane podejście z określonymi punktami wejścia i wyjścia, połączone z technikami zarządzania emocjami."
    },
    "Strategist Degen": {
        "icon": "🎯", 
        "color": "#3F51B5", 
        "theme": "default", 
        "description": "Planujący inwestor, który opracowuje dokładne strategie i trzyma się ich. Działa zgodnie z planem i ustalonymi celami.",
        "strengths": ["Metodyczne podejście", "Dyscyplina i konsekwencja", "Jasno określone cele"],
        "challenges": ["Brak elastyczności", "Może przeoczyć spontaniczne okazje", "Czasem zbyt przywiązany do teorii"],
        "strategy": "Precyzyjnie zdefiniowane strategie z jasnymi zasadami wejścia i wyjścia, regularnie weryfikowane i optymalizowane."
    },
    "Mad Scientist Degen": {
        "icon": "🔬", 
        "color": "#009688", 
        "theme": "default", 
        "description": "Eksperymentujący inwestor, który testuje nowe podejścia i teorie. Lubi badać niestandardowe rozwiązania i innowacje.",
        "strengths": ["Innowacyjność", "Analityczne myślenie", "Odkrywanie niewykorzystanych możliwości"],
        "challenges": ["Ryzyko nietestowanych strategii", "Skomplikowane podejście", "Nadmierne teoretyzowanie"],
        "strategy": "Eksperymentowanie z innowacyjnymi podejściami, przy jednoczesnym zarządzaniu ryzykiem poprzez alokację kapitału w sposób kontrolowany."
    },
    "Spreadsheet Degen": {
        "icon": "📊", 
        "color": "#795548", 
        "theme": "default", 
        "description": "Inwestor opierający decyzje na danych i analizach. Tworzy szczegółowe modele i kalkulacje przed każdą decyzją.",
        "strengths": ["Podejście bazujące na danych", "Dokładna analiza", "Ograniczenie wpływu emocji"],
        "challenges": ["Analiza paraliżująca", "Pomijanie czynników jakościowych", "Czasem przesadny perfekcjonizm"],
        "strategy": "Strategie oparte na modelach matematycznych, analizie danych i wskaźnikach technicznych, z regularną weryfikacją założeń."
    },
    "Meta Degen": {
        "icon": "🔄", 
        "color": "#607D8B", 
        "theme": "default", 
        "description": "Inwestor analizujący swoje własne procesy myślowe i decyzyjne. Ciągle doskonali swoje podejście i uczy się na błędach.",
        "strengths": ["Samoświadomość", "Ciągłe doskonalenie", "Adaptacyjność"],
        "challenges": ["Nadmierna autorefleksja", "Trudności z podjęciem decyzji", "Zbyt częste zmiany strategii"],
        "strategy": "Podejście adaptacyjne, łączące różne style inwestowania w zależności od okoliczności, z naciskiem na ciągłe uczenie się."
    },
    "Hype Degen": {
        "icon": "📣", 
        "color": "#FFC107", 
        "theme": "default", 
        "description": "Inwestor podążający za popularnymi trendami i projektami. Bardzo aktywny w mediach społecznościowych i śledzący opinie influencerów.",
        "strengths": ["Wczesne wykrywanie trendów", "Znajomość nastrojów społeczności", "Szybka reakcja na nowe projekty"],
        "challenges": ["Podatność na manipulacje", "FOMO (strach przed pominięciem)", "Brak własnej analizy"],
        "strategy": "Śledzenie trendów społecznościowych z jednoczesnym zachowaniem krytycznego myślenia i weryfikacją informacji z wielu źródeł."
    }
}

# BADGE SYSTEM - STEP 1: Categories and Structure
# ===================================================

# Badge Categories Configuration
BADGE_CATEGORIES = {
    "getting_started": {
        "name": "Początkujący",
        "description": "Pierwsze kroki w BrainVenture Academy",
        "icon": "🌱",
        "color": "#4CAF50",
        "order": 1
    },
    "learning_progress": {
        "name": "Postęp w Nauce",
        "description": "Osiągnięcia związane z ukończeniem lekcji i kursów",
        "icon": "📚",
        "color": "#2196F3",
        "order": 2
    },
    "engagement": {
        "name": "Zaangażowanie",
        "description": "Regularna aktywność i konsekwencja w nauce",
        "icon": "🔥",
        "color": "#FF5722",
        "order": 3
    },
    "expertise": {
        "name": "Ekspertyza",
        "description": "Mistrzostwo w konkretnych obszarach wiedzy",
        "icon": "🎓",
        "color": "#9C27B0",
        "order": 4
    },
    "degen_mastery": {
        "name": "Mistrzostwo Degena",
        "description": "Poznanie i rozwój różnych typów osobowości inwestorskich",
        "icon": "👑",
        "color": "#FFC107",
        "order": 5
    },
    "social": {
        "name": "Społeczność",
        "description": "Interakcje społeczne i budowanie społeczności",
        "icon": "🤝",
        "color": "#00BCD4",
        "order": 6
    },
    "achievements": {
        "name": "Osiągnięcia",
        "description": "Meta-osiągnięcia i kolekcjonowanie odznak",
        "icon": "🏆",
        "color": "#795548",
        "order": 7
    },
    "special": {
        "name": "Specjalne",
        "description": "Rzadkie i wyjątkowe osiągnięcia",
        "icon": "✨",
        "color": "#E91E63",
        "order": 8
    }
}

# Badge Tiers/Levels
BADGE_TIERS = {
    "bronze": {"name": "Brązowa", "color": "#CD7F32", "multiplier": 1.0},
    "silver": {"name": "Srebrna", "color": "#C0C0C0", "multiplier": 1.5},
    "gold": {"name": "Złota", "color": "#FFD700", "multiplier": 2.0},
    "platinum": {"name": "Platynowa", "color": "#E5E4E2", "multiplier": 3.0},
    "diamond": {"name": "Diamentowa", "color": "#B9F2FF", "multiplier": 5.0}
}

# Complete Badge System Configuration
BADGES = {
    # ==========================================
    # KATEGORIA: POCZĄTKUJĄCY (getting_started)
    # ==========================================
    "welcome": {
        "name": "Witaj w Akademii",
        "description": "Pierwszy krok w BrainVenture Academy",
        "icon": "👋",
        "category": "getting_started",
        "tier": "bronze",
        "xp_reward": 25,
        "condition": "register_account",
        "requirement": 1,
        "secret": False,
        "stackable": False
    },
    "profile_complete": {
        "name": "Profil Kompletny",
        "description": "Uzupełnij wszystkie informacje w profilu",
        "icon": "📝",
        "category": "getting_started",
        "tier": "bronze",
        "xp_reward": 50,
        "condition": "complete_profile",
        "requirement": 1,
        "secret": False,
        "stackable": False
    },
    "first_degen_test": {
        "name": "Odkrywca Osobowości",
        "description": "Wykonaj pierwszy test typu degena",
        "icon": "🔍",
        "category": "getting_started",
        "tier": "silver",
        "xp_reward": 100,
        "condition": "degen_test_completed",
        "requirement": 1,
        "secret": False,
        "stackable": False
    },
    "first_lesson": {
        "name": "Pierwszy Uczeń",
        "description": "Ukończ pierwszą lekcję w akademii",
        "icon": "🎯",
        "category": "getting_started",
        "tier": "silver",
        "xp_reward": 75,
        "condition": "lesson_completed",
        "requirement": 1,
        "secret": False,
        "stackable": False
    },

    # ==============================================
    # KATEGORIA: POSTĘP W NAUCE (learning_progress)
    # ==============================================
    "lesson_rookie": {
        "name": "Nowicjusz Lekcji",
        "description": "Ukończ 5 lekcji",
        "icon": "📖",
        "category": "learning_progress",
        "tier": "bronze",
        "xp_reward": 100,
        "condition": "lesson_completed",
        "requirement": 5,
        "secret": False,
        "stackable": False
    },
    "lesson_apprentice": {
        "name": "Uczeń Zaawansowany",
        "description": "Ukończ 15 lekcji",
        "icon": "📚",
        "category": "learning_progress",
        "tier": "silver",
        "xp_reward": 200,
        "condition": "lesson_completed",
        "requirement": 15,
        "secret": False,
        "stackable": False
    },
    "lesson_scholar": {
        "name": "Uczony",
        "description": "Ukończ 30 lekcji",
        "icon": "🎓",
        "category": "learning_progress",
        "tier": "gold",
        "xp_reward": 400,
        "condition": "lesson_completed",
        "requirement": 30,
        "secret": False,
        "stackable": False
    },
    "lesson_master": {
        "name": "Mistrz Lekcji",
        "description": "Ukończ 50 lekcji",
        "icon": "👨‍🎓",
        "category": "learning_progress",
        "tier": "platinum",
        "xp_reward": 750,
        "condition": "lesson_completed",
        "requirement": 50,
        "secret": False,
        "stackable": False
    },
    "quiz_perfectionist": {
        "name": "Perfekcjonista",
        "description": "Uzyskaj 100% w quizie",
        "icon": "💯",
        "category": "learning_progress",
        "tier": "gold",
        "xp_reward": 150,
        "condition": "quiz_completed",
        "requirement": {"score": 100},
        "secret": False,
        "stackable": True
    },
    "speed_learner": {
        "name": "Szybki Umysł",
        "description": "Ukończ 3 lekcje w jeden dzień",
        "icon": "⚡",
        "category": "learning_progress",
        "tier": "silver",
        "xp_reward": 200,
        "condition": "lessons_per_day",
        "requirement": 3,
        "secret": False,
        "stackable": False
    },

    # ==========================================
    # KATEGORIA: ZAANGAŻOWANIE (engagement)
    # ==========================================
    "login_streak_3": {
        "name": "Konsekwentny Początek",
        "description": "Zaloguj się 3 dni z rzędu",
        "icon": "📅",
        "category": "engagement",
        "tier": "bronze",
        "xp_reward": 75,
        "condition": "user_login",
        "requirement": {"streak": 3},
        "secret": False,
        "stackable": False
    },
    "login_streak_7": {
        "name": "Tygodniowy Wojownik",
        "description": "Zaloguj się 7 dni z rzędu",
        "icon": "🗓️",
        "category": "engagement",
        "tier": "silver",
        "xp_reward": 150,
        "condition": "user_login",
        "requirement": {"streak": 7},
        "secret": False,
        "stackable": False
    },
    "login_streak_30": {
        "name": "Mistrz Miesiąca",
        "description": "Zaloguj się 30 dni z rzędu",
        "icon": "🔥",
        "category": "engagement",
        "tier": "gold",
        "xp_reward": 500,
        "condition": "user_login",
        "requirement": {"streak": 30},
        "secret": False,
        "stackable": False
    },
    "daily_mission_hero": {
        "name": "Bohater Misji",
        "description": "Ukończ wszystkie misje dzienne w jeden dzień",
        "icon": "⭐",
        "category": "engagement",
        "tier": "silver",
        "xp_reward": 100,
        "condition": "daily_mission_completed",
        "requirement": {"all_in_day": True},
        "secret": False,
        "stackable": True
    },
    "weekend_scholar": {
        "name": "Weekendowy Uczony",
        "description": "Ukończ lekcję w weekend",
        "icon": "📅",
        "category": "engagement",
        "tier": "bronze",
        "xp_reward": 50,
        "condition": "weekend_learning",
        "requirement": 1,
        "secret": False,
        "stackable": True
    },
    "night_owl": {
        "name": "Nocna Sowa",
        "description": "Ukończ lekcję po godzinie 22:00",
        "icon": "🦉",
        "category": "engagement",
        "tier": "bronze",
        "xp_reward": 50,
        "condition": "late_learning",
        "requirement": {"hour": 22},
        "secret": False,
        "stackable": True
    },
    "early_bird": {
        "name": "Ranny Ptaszek",
        "description": "Ukończ lekcję przed godziną 8:00",
        "icon": "🐦",
        "category": "engagement",
        "tier": "bronze",
        "xp_reward": 50,
        "condition": "early_learning",
        "requirement": {"hour": 8},
        "secret": False,
        "stackable": True
    },

    # =====================================
    # KATEGORIA: EKSPERTYZA (expertise)
    # =====================================
    "zen_master": {
        "name": "Mistrz Zen",
        "description": "Ukończ wszystkie lekcje z kategorii Mindfulness",
        "icon": "🧘‍♂️",
        "category": "expertise",
        "tier": "gold",
        "xp_reward": 300,
        "condition": "category_completed",
        "requirement": {"category": "mindfulness"},
        "secret": False,
        "stackable": False
    },
    "market_analyst": {
        "name": "Analityk Rynku",
        "description": "Ukończ wszystkie lekcje z kategorii Analiza Rynku",
        "icon": "📊",
        "category": "expertise",
        "tier": "gold",
        "xp_reward": 300,
        "condition": "category_completed",
        "requirement": {"category": "market_analysis"},
        "secret": False,
        "stackable": False
    },
    "strategy_guru": {
        "name": "Guru Strategii",
        "description": "Ukończ wszystkie lekcje z kategorii Strategie",
        "icon": "🎯",
        "category": "expertise",
        "tier": "gold",
        "xp_reward": 300,
        "condition": "category_completed",
        "requirement": {"category": "strategies"},
        "secret": False,
        "stackable": False
    },
    "psychology_expert": {
        "name": "Ekspert Psychologii",
        "description": "Ukończ wszystkie lekcje z kategorii Psychologia",
        "icon": "🧠",
        "category": "expertise",
        "tier": "gold",
        "xp_reward": 300,
        "condition": "category_completed",
        "requirement": {"category": "psychology"},
        "secret": False,
        "stackable": False
    },
    "xp_collector": {
        "name": "Kolekcjoner XP",
        "description": "Zgromadź 1000 punktów doświadczenia",
        "icon": "💎",
        "category": "expertise",
        "tier": "silver",
        "xp_reward": 200,
        "condition": "xp_awarded",
        "requirement": {"total": 1000},
        "secret": False,
        "stackable": False
    },
    "xp_master": {
        "name": "Mistrz Doświadczenia",
        "description": "Zgromadź 5000 punktów doświadczenia",
        "icon": "💠",
        "category": "expertise",
        "tier": "platinum",
        "xp_reward": 500,
        "condition": "xp_awarded",
        "requirement": {"total": 5000},
        "secret": False,
        "stackable": False
    },

    # =============================================
    # KATEGORIA: MISTRZOSTWO DEGENA (degen_mastery)
    # =============================================
    "degen_explorer": {
        "name": "Odkrywca Degenów",
        "description": "Poznaj wszystkie typy degenów w eksploratorze",
        "icon": "🗺️",
        "category": "degen_mastery",
        "tier": "silver",
        "xp_reward": 150,
        "condition": "explore_all_types",
        "requirement": 8,
        "secret": False,
        "stackable": False
    },
    "multi_degen": {
        "name": "Wieloaspektowy Degen",
        "description": "Wykonaj test 3 razy z różnymi wynikami",
        "icon": "🎭",
        "category": "degen_mastery",
        "tier": "gold",
        "xp_reward": 250,
        "condition": "multiple_test_results",
        "requirement": 3,
        "secret": False,
        "stackable": False
    },
    "self_aware": {
        "name": "Samoświadomy",
        "description": "Potwierdź swój typ degena wykonując test ponownie",
        "icon": "🔮",
        "category": "degen_mastery",
        "tier": "silver",
        "xp_reward": 100,
        "condition": "confirm_degen_type",
        "requirement": 1,
        "secret": False,
        "stackable": False
    },
    "degen_king": {
        "name": "Król Degenów",
        "description": "Osiągnij mistrzostwo we wszystkich aspektach degeneracy",
        "icon": "👑",
        "category": "degen_mastery",
        "tier": "diamond",
        "xp_reward": 1000,
        "condition": "complete_degen_mastery",
        "requirement": 1,
        "secret": True,
        "stackable": False
    },

    # =======================================
    # KATEGORIA: SPOŁECZNOŚĆ (social)
    # =======================================
    "community_member": {
        "name": "Członek Społeczności",
        "description": "Dołącz do społeczności akademii",
        "icon": "🏘️",
        "category": "social",
        "tier": "bronze",
        "xp_reward": 50,
        "condition": "join_community",
        "requirement": 1,
        "secret": False,
        "stackable": False
    },
    "helpful_friend": {
        "name": "Pomocny Przyjaciel",
        "description": "Pomóż innemu użytkownikowi",
        "icon": "🤗",
        "category": "social",
        "tier": "silver",
        "xp_reward": 100,
        "condition": "help_user",
        "requirement": 1,
        "secret": False,
        "stackable": True
    },
    "mentor": {
        "name": "Mentor",
        "description": "Pomóż 5 różnym użytkownikom",
        "icon": "👨‍🏫",
        "category": "social",
        "tier": "gold",
        "xp_reward": 300,
        "condition": "help_user",
        "requirement": 5,
        "secret": False,
        "stackable": False
    },
    "influencer": {
        "name": "Influencer",
        "description": "Podziel się swoimi osiągnięciami",
        "icon": "📣",
        "category": "social",
        "tier": "silver",
        "xp_reward": 75,
        "condition": "share_achievement",
        "requirement": 1,
        "secret": False,
        "stackable": True
    },

    # ==========================================
    # KATEGORIA: OSIĄGNIĘCIA (achievements)
    # ==========================================
    "first_badge": {
        "name": "Pierwsza Odznaka",
        "description": "Zdobądź swoją pierwszą odznakę",
        "icon": "🏅",
        "category": "achievements",
        "tier": "bronze",
        "xp_reward": 25,
        "condition": "earn_badge",
        "requirement": 1,
        "secret": False,
        "stackable": False
    },
    "badge_collector": {
        "name": "Kolekcjoner Odznak",
        "description": "Zdobądź 10 różnych odznak",
        "icon": "🎖️",
        "category": "achievements",
        "tier": "silver",
        "xp_reward": 200,
        "condition": "earn_badge",
        "requirement": 10,
        "secret": False,
        "stackable": False
    },
    "badge_master": {
        "name": "Mistrz Odznak",
        "description": "Zdobądź 25 różnych odznak",
        "icon": "🏆",
        "category": "achievements",
        "tier": "gold",
        "xp_reward": 500,
        "condition": "earn_badge",
        "requirement": 25,
        "secret": False,
        "stackable": False
    },
    "achievement_hunter": {
        "name": "Łowca Osiągnięć",
        "description": "Zdobądź wszystkie odznaki z jednej kategorii",
        "icon": "🎯",
        "category": "achievements",
        "tier": "platinum",
        "xp_reward": 750,
        "condition": "complete_category",
        "requirement": 1,
        "secret": False,
        "stackable": True
    },

    # ====================================
    # KATEGORIA: SPECJALNE (special)
    # ====================================
    "pioneer": {
        "name": "Pionier",
        "description": "Jeden z pierwszych 100 użytkowników akademii",
        "icon": "🚀",
        "category": "special",
        "tier": "diamond",
        "xp_reward": 500,
        "condition": "early_adopter",
        "requirement": 100,
        "secret": True,
        "stackable": False
    },
    "legend": {
        "name": "Legenda",
        "description": "Osiągnij wszystkie możliwe odznaki",
        "icon": "👑",
        "category": "special",
        "tier": "diamond",
        "xp_reward": 2000,
        "condition": "complete_all_badges",
        "requirement": 1,
        "secret": True,
        "stackable": False
    },
    "dedicated_student": {
        "name": "Oddany Uczeń",
        "description": "Spędź łącznie 50 godzin w akademii",
        "icon": "⏰",
        "category": "special",
        "tier": "platinum",
        "xp_reward": 1000,
        "condition": "total_study_time",
        "requirement": {"hours": 50},
        "secret": False,
        "stackable": False
    },
    "secret_discoverer": {
        "name": "Odkrywca Sekretów",
        "description": "Znajdź ukryty easter egg w aplikacji",
        "icon": "🕵️",
        "category": "special",
        "tier": "gold",
        "xp_reward": 300,
        "condition": "find_easter_egg",
        "requirement": 1,
        "secret": True,
        "stackable": False
    },
    "midnight_learner": {
        "name": "Uczący się o Północy",
        "description": "Ukończ lekcję dokładnie o północy",
        "icon": "🌙",
        "category": "special",
        "tier": "gold",
        "xp_reward": 200,
        "condition": "midnight_learning",
        "requirement": 1,
        "secret": True,
        "stackable": False
    }
}