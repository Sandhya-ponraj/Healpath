import sqlite3

conn = sqlite3.connect("healpath.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS assessments")

cur.execute("""
CREATE TABLE assessments(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,
gender TEXT,
age TEXT,
personality TEXT,

weaknesses TEXT,
strengths TEXT,
bad_moment TEXT,
good_moment TEXT,

mood TEXT,
mood_score TEXT,

screen_time TEXT,
social_media_usage TEXT,
phone_sleep_effect TEXT,

sleep_hours TEXT,
physical_activity TEXT,
water_intake TEXT,

academic_goal TEXT,
personal_goal TEXT,
daily_tasks TEXT,
stress_trigger TEXT,

weekly_success TEXT,
weekly_challenge TEXT,
week_satisfaction TEXT,

energy_level TEXT,
motivation_level TEXT

)
""")

conn.commit()
conn.close()

print("Database Created Successfully")