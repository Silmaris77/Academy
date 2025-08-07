"""
LESSON DATA STRUCTURE STANDARDIZATION
====================================

Analysis of current lesson structure and standardization plan.
This document outlines the inconsistencies found and the unified structure to implement.

CURRENT ISSUES IDENTIFIED:
--------------------------

1. **STRUCTURAL INCONSISTENCIES:**
   - B1C1L1.json: Has complete structure with all sections
   - B1C1L4.json: Has incomplete `practical_exercises` section (cuts off)
   - Different XP rewards (100 vs 20)
   - Different difficulty formats ("expert" vs "Intermediate")

2. **SECTION VARIATIONS:**
   - B1C1L1: Has `closing_quiz` section
   - B1C1L4: Has `practical_exercises` section (incomplete)
   - Both have similar but not identical section structures

3. **METADATA INCONSISTENCIES:**
   - Difficulty field format variations
   - XP reward variations
   - Tag format differences

PROPOSED UNIFIED STRUCTURE:
---------------------------

{
  // METADATA (Required)
  "id": "string",                    // Format: B[block]C[category]L[lesson]
  "title": "string",                 // Lesson title
  "description": "string",           // Brief lesson description
  "tag": "string",                   // Category/topic tag
  "xp_reward": number,               // XP points (standardized range: 50-150)
  "difficulty": "string",            // Standardized: "beginner", "intermediate", "advanced", "expert"
  
  // INTRODUCTION (Required)
  "intro": {
    "main": "string",                // Main introduction content
    "case_study": "string"           // Opening case study (optional)
  },
  
  // MAIN SECTIONS (Required)
  "sections": {
    
    // Pre-lesson assessment
    "opening_quiz": {
      "title": "string",
      "description": "string",
      "questions": [
        {
          "question": "string",
          "options": ["string", ...],
          "correct_answer": number | null,  // null for self-assessment
          "explanation": "string"
        }
      ],
      "scoring": {                   // Optional, for self-assessment quizzes
        "interpretation": {
          "low_range": "description",
          "medium_range": "description", 
          "high_range": "description"
        }
      }
    },
    
    // Main learning content
    "learning": {
      "sections": [
        {
          "title": "string",
          "content": "string"         // HTML content
        }
      ]
    },
    
    // Reflection exercises
    "reflection": {
      "sections": [
        {
          "title": "string",
          "content": "string"
        }
      ]
    },
    
    // Practical application
    "application": {
      "sections": [
        {
          "title": "string", 
          "content": "string"
        }
      ]
    },
    
    // Post-lesson assessment (Optional)
    "closing_quiz": {
      "title": "string",
      "description": "string", 
      "questions": [
        {
          "question": "string",
          "options": ["string", ...],
          "correct_answer": number,
          "explanation": "string"
        }
      ]
    },
    
    // Summary and key takeaways (Optional)
    "summary": {
      "key_points": ["string", ...],
      "next_steps": ["string", ...],
      "resources": [
        {
          "title": "string",
          "url": "string", 
          "type": "string"  // "article", "video", "tool", etc.
        }
      ]
    }
  },
  
  // OPTIONAL ENHANCEMENTS
  "mind_map": {                      // For lessons with custom mind maps
    "nodes": [...],
    "edges": [...],
    "config": {...}
  },
  
  "estimated_time": "string",        // e.g., "15-20 minutes"
  "prerequisites": ["string", ...],  // Required lesson IDs
  "learning_objectives": ["string", ...],
  "tags": ["string", ...]           // Additional categorization tags
}

STANDARDIZATION ACTIONS NEEDED:
--------------------------------

1. **Fix B1C1L4.json structure**
   - Complete the truncated practical_exercises section
   - Standardize difficulty format
   - Review XP reward appropriateness

2. **Create validation schema**
   - JSON schema for structure validation
   - Content validation rules
   - Automated testing

3. **Create migration tools**
   - Script to validate existing lessons
   - Script to convert/upgrade lesson structures
   - Backup and rollback capabilities

4. **Update lesson loading system**
   - Enhanced error handling for malformed lessons
   - Fallback content for missing sections
   - Compatibility layer for old formats

5. **Create lesson template**
   - Standard template for new lessons
   - Content guidelines
   - Examples and best practices

IMPLEMENTATION PRIORITY:
-----------------------

Priority 1: Fix existing lesson files
Priority 2: Create validation and migration tools  
Priority 3: Update lesson loading system
Priority 4: Create authoring guidelines and templates
Priority 5: Migrate any additional lesson files

"""
