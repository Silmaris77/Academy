from utils.achievements import check_achievements
from data.users import load_user_data

print("Testing badge system...")
users = load_user_data()
print(f"Found {len(users)} users")

# Test user 'a'
user_a = users.get('a', {})
print(f"User 'a' badges before: {user_a.get('badges', [])}")

# Award badges
new_badges = check_achievements('a')
print(f"New badges awarded to 'a': {new_badges}")

# Check after
users_after = load_user_data()
user_a_after = users_after.get('a', {})
print(f"User 'a' badges after: {user_a_after.get('badges', [])}")

# Check if first_degen_test badge was awarded
has_degen_badge = 'first_degen_test' in user_a_after.get('badges', [])
print(f"Has degen test badge: {has_degen_badge}")
