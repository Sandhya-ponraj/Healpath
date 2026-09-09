import sqlite3

conn = sqlite3.connect("healpath.db")
cur = conn.cursor()

cur.execute("SELECT * FROM assessments")
rows = cur.fetchall()

for row in rows:

    print("\n==============================")
    print("ID:", row[0])

    print("\n--- Basic Information ---")
    print("Name:", row[1])
    print("Gender:", row[2])
    print("Age:", row[3])
    print("Personality:", row[4])

    print("\n--- Self Reflection ---")
    print("Weaknesses:", row[5])
    print("Strengths:", row[6])
    print("Bad Moment:", row[7])
    print("Good Moment:", row[8])

    print("\n--- Current Mood ---")
    print("Mood:", row[9])
    print("Mood Score:", row[10])

    print("\n--- Digital Habits ---")
    print("Screen Time:", row[11])
    print("Social Media Usage:", row[12])
    print("Phone Sleep Effect:", row[13])

    print("\n--- Lifestyle Assessment ---")
    print("Sleep Hours:", row[14])
    print("Physical Activity:", row[15])
    print("Water Intake:", row[16])

    print("\n--- Goals & Stress Assessment ---")
    print("Academic Goal:", row[17])
    print("Personal Goal:", row[18])
    print("Daily Tasks:", row[19])
    print("Stress Trigger:", row[20])

    print("\n--- Weekly Reflection ---")
    print("Weekly Success:", row[21])
    print("Weekly Challenge:", row[22])
    print("Week Satisfaction:", row[23])

    print("\n--- Emotion Check-In ---")
    print("Energy Level:", row[24])
    print("Motivation Level:", row[25])

conn.close()