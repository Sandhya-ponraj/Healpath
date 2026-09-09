from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    # Basic Information
    name = request.form.get('name')
    gender = request.form.get('gender')
    age = request.form.get('age')
    personality = request.form.get('personality')

    # Self Reflection
    weaknesses = request.form.get('weaknesses')
    strengths = request.form.get('strengths')
    bad_moment = request.form.get('bad_moment')
    good_moment = request.form.get('good_moment')

    # Mood
    mood = request.form.get('mood')
    mood_score = request.form.get('mood_score')

    # Digital Habits
    screen_time = request.form.get('screen_time')
    social_media_usage = request.form.get('social_media_usage')
    phone_sleep_effect = request.form.get('phone_sleep_effect')

    # Lifestyle
    sleep_hours = request.form.get('sleep_hours')
    physical_activity = request.form.get('physical_activity')
    water_intake = request.form.get('water_intake')

    # Goals & Stress
    academic_goal = request.form.get('academic_goal')
    personal_goal = request.form.get('personal_goal')
    daily_tasks = request.form.get('daily_tasks')
    stress_trigger = request.form.get('stress_trigger')

    # Weekly Reflection
    weekly_success = request.form.get('weekly_success')
    weekly_challenge = request.form.get('weekly_challenge')
    week_satisfaction = request.form.get('week_satisfaction')

    # Emotion Check-In
    energy_level = request.form.get('energy_level')
    motivation_level = request.form.get('motivation_level')

    conn = sqlite3.connect('healpath.db')
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO assessments (
        name,
        gender,
        age,
        personality,
        weaknesses,
        strengths,
        bad_moment,
        good_moment,
        mood,
        mood_score,
        screen_time,
        social_media_usage,
        phone_sleep_effect,
        sleep_hours,
        physical_activity,
        water_intake,
        academic_goal,
        personal_goal,
        daily_tasks,
        stress_trigger,
        weekly_success,
        weekly_challenge,
        week_satisfaction,
        energy_level,
        motivation_level
    )
    VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?
    )
    """, (
        name,
        gender,
        age,
        personality,
        weaknesses,
        strengths,
        bad_moment,
        good_moment,
        mood,
        mood_score,
        screen_time,
        social_media_usage,
        phone_sleep_effect,
        sleep_hours,
        physical_activity,
        water_intake,
        academic_goal,
        personal_goal,
        daily_tasks,
        stress_trigger,
        weekly_success,
        weekly_challenge,
        week_satisfaction,
        energy_level,
        motivation_level
    ))

    conn.commit()
    conn.close()

    return f"""
    <h2>Assessment Submitted Successfully!</h2>
    <h3>Thank You {name}</h3>
    <p>Your HealPath assessment has been saved successfully.</p>
    <a href="/">Fill Another Response</a>
    """

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
