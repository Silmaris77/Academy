"""
Mission Management System for BrainVenture Academy
Handles loading, processing, and tracking of lesson-based missions
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from data.users import load_user_data, save_user_data


class MissionManager:
    """Manages missions for lessons and tracks user progress"""
    
    def __init__(self):
        self.missions_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'missions')
        self.ensure_missions_directory()
    
    def ensure_missions_directory(self):
        """Ensure missions directory exists"""
        if not os.path.exists(self.missions_path):
            os.makedirs(self.missions_path)
    
    def load_lesson_missions(self, lesson_id: str) -> Optional[Dict]:
        """Load missions for a specific lesson"""
        mission_file = os.path.join(self.missions_path, f"{lesson_id}_missions.json")
        
        if not os.path.exists(mission_file):
            return None
            
        try:
            with open(mission_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading missions for {lesson_id}: {e}")
            return None
    
    def get_user_mission_progress(self, username: str, lesson_id: str) -> Dict:
        """Get user's progress for lesson missions"""
        users_data = load_user_data()
        user_data = users_data.get(username, {})
        
        missions_progress = user_data.get('missions_progress', {})
        return missions_progress.get(lesson_id, {})
    
    def initialize_mission_progress(self, username: str, lesson_id: str, mission_id: str) -> Dict:
        """Initialize progress tracking for a mission"""
        users_data = load_user_data()
        user_data = users_data.get(username, {})
        
        if 'missions_progress' not in user_data:
            user_data['missions_progress'] = {}
        
        if lesson_id not in user_data['missions_progress']:
            user_data['missions_progress'][lesson_id] = {}
        
        if mission_id not in user_data['missions_progress'][lesson_id]:
            mission_data = self.load_lesson_missions(lesson_id)
            if mission_data:
                mission_info = None
                for mission in mission_data['missions']:
                    if mission['id'] == mission_id:
                        mission_info = mission
                        break
                
                if mission_info:
                    user_data['missions_progress'][lesson_id][mission_id] = {
                        'status': 'active',
                        'start_date': datetime.now().isoformat(),
                        'current_day': 1,
                        'total_days': mission_info.get('duration_days', 1),
                        'daily_progress': {},
                        'completed_tasks': [],
                        'xp_earned': 0,
                        'last_activity': datetime.now().isoformat()
                    }
        
        users_data[username] = user_data
        save_user_data(users_data)
        return user_data['missions_progress'][lesson_id][mission_id]
    
    def update_daily_progress(self, username: str, lesson_id: str, mission_id: str, 
                            day: int, task_data: Dict) -> bool:
        """Update daily progress for a mission"""
        users_data = load_user_data()
        user_data = users_data.get(username, {})
        
        if lesson_id not in user_data.get('missions_progress', {}):
            self.initialize_mission_progress(username, lesson_id, mission_id)
        
        mission_progress = user_data['missions_progress'][lesson_id][mission_id]
        
        # Update daily progress
        day_key = f"day_{day}"
        if day_key not in mission_progress['daily_progress']:
            mission_progress['daily_progress'][day_key] = {}
        
        mission_progress['daily_progress'][day_key].update(task_data)
        mission_progress['daily_progress'][day_key]['completion_time'] = datetime.now().isoformat()
        mission_progress['last_activity'] = datetime.now().isoformat()
        
        # Check if day is completed
        mission_data = self.load_lesson_missions(lesson_id)
        if mission_data:
            mission_info = None
            for mission in mission_data['missions']:
                if mission['id'] == mission_id:
                    mission_info = mission
                    break
            
            if mission_info and self.is_day_completed(mission_info, day, task_data):
                mission_progress['daily_progress'][day_key]['completed'] = True
                
                # Check if entire mission is completed
                if self.is_mission_completed(mission_progress, mission_info):
                    mission_progress['status'] = 'completed'
                    mission_progress['completion_date'] = datetime.now().isoformat()
                    mission_progress['xp_earned'] = mission_info.get('xp_reward', 0)
                    
                    # Award XP to user
                    user_data['xp'] = user_data.get('xp', 0) + mission_info.get('xp_reward', 0)
        
        users_data[username] = user_data
        save_user_data(users_data)
        return True
    
    def is_day_completed(self, mission_info: Dict, day: int, task_data: Dict) -> bool:
        """Check if a specific day's tasks are completed"""
        day_key = f"day_{day}"
        validation = mission_info.get('validation', {})
        
        if validation.get('type') == 'self_report':
            daily_checklist = validation.get('daily_checklist', {})
            if day_key in daily_checklist:
                required_tasks = daily_checklist[day_key]
                completed_tasks = task_data.get('completed_checklist', [])
                return len(completed_tasks) >= len(required_tasks)
        
        # For other validation types, assume completion if data is provided
        return len(task_data) > 0
    
    def is_mission_completed(self, mission_progress: Dict, mission_info: Dict) -> bool:
        """Check if entire mission is completed"""
        total_days = mission_info.get('duration_days', 1)
        daily_progress = mission_progress.get('daily_progress', {})
        
        completed_days = 0
        for day in range(1, total_days + 1):
            day_key = f"day_{day}"
            if day_key in daily_progress and daily_progress[day_key].get('completed', False):
                completed_days += 1
        
        return completed_days >= total_days
    
    def get_available_missions(self, username: str, lesson_id: str) -> List[Dict]:
        """Get available missions for a lesson"""
        mission_data = self.load_lesson_missions(lesson_id)
        if not mission_data:
            return []
        
        user_progress = self.get_user_mission_progress(username, lesson_id)
        available_missions = []
        
        for mission in mission_data['missions']:
            mission_id = mission['id']
            progress = user_progress.get(mission_id, {})
            
            mission_with_progress = mission.copy()
            mission_with_progress['progress'] = progress
            mission_with_progress['status'] = progress.get('status', 'available')
            
            available_missions.append(mission_with_progress)
        
        return available_missions
    
    def get_daily_mission_info(self, username: str, lesson_id: str, mission_id: str) -> Dict:
        """Get today's mission information and progress"""
        users_data = load_user_data()
        user_data = users_data.get(username, {})
        
        mission_progress = user_data.get('missions_progress', {}).get(lesson_id, {}).get(mission_id, {})
        
        if not mission_progress:
            return {}
        
        current_day = mission_progress.get('current_day', 1)
        start_date = datetime.fromisoformat(mission_progress.get('start_date', datetime.now().isoformat()))
        days_since_start = (datetime.now() - start_date).days + 1
        
        # Update current day if needed
        if days_since_start > current_day:
            mission_progress['current_day'] = days_since_start
            users_data[username] = user_data
            save_user_data(users_data)
        
        mission_data = self.load_lesson_missions(lesson_id)
        if mission_data:
            for mission in mission_data['missions']:
                if mission['id'] == mission_id:
                    instructions = mission.get('instructions', {})
                    day_key = f"day_{days_since_start}"
                    
                    if day_key in instructions:
                        return {
                            'current_day': days_since_start,
                            'total_days': mission.get('duration_days', 1),
                            'day_info': instructions[day_key],
                            'progress': mission_progress,
                            'mission_title': mission.get('title', ''),
                            'is_completed': mission_progress.get('status') == 'completed'
                        }
        
        return {}
    
    def get_lesson_mission_summary(self, username: str, lesson_id: str) -> Dict:
        """Get summary of all missions for a lesson"""
        missions = self.get_available_missions(username, lesson_id)
        
        total_missions = len(missions)
        completed_missions = sum(1 for m in missions if m.get('status') == 'completed')
        active_missions = sum(1 for m in missions if m.get('status') == 'active')
        total_xp = sum(m.get('xp_reward', 0) for m in missions if m.get('status') == 'completed')
        
        return {
            'total_missions': total_missions,
            'completed_missions': completed_missions,
            'active_missions': active_missions,
            'available_missions': total_missions - completed_missions - active_missions,
            'total_xp_earned': total_xp,
            'completion_percentage': (completed_missions / total_missions * 100) if total_missions > 0 else 0
        }


# Global instance
mission_manager = MissionManager()


def get_lesson_missions(lesson_id: str) -> Optional[Dict]:
    """Get missions for a lesson"""
    return mission_manager.load_lesson_missions(lesson_id)


def start_mission(username: str, lesson_id: str, mission_id: str) -> Dict:
    """Start a mission for a user"""
    return mission_manager.initialize_mission_progress(username, lesson_id, mission_id)


def update_mission_progress(username: str, lesson_id: str, mission_id: str, 
                          day: int, task_data: Dict) -> bool:
    """Update mission progress"""
    return mission_manager.update_daily_progress(username, lesson_id, mission_id, day, task_data)


def get_user_missions(username: str, lesson_id: str) -> List[Dict]:
    """Get user's missions for a lesson"""
    return mission_manager.get_available_missions(username, lesson_id)


def get_today_mission_info(username: str, lesson_id: str, mission_id: str) -> Dict:
    """Get today's mission info"""
    return mission_manager.get_daily_mission_info(username, lesson_id, mission_id)


def get_mission_summary(username: str, lesson_id: str) -> Dict:
    """Get mission summary for a lesson"""
    return mission_manager.get_lesson_mission_summary(username, lesson_id)
