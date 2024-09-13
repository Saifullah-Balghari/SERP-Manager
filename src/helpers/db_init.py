import sqlite3

connection = sqlite3.connect('serp.db')  # This creates a new database file if it does not exist
cursor = connection.cursor()

# Create a table for storing student information
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    father_name TEXT,
    institution_name TEXT
)
''')

# Create a table for storing exam information
cursor.execute('''
CREATE TABLE IF NOT EXISTS exams (
    exam_id INTEGER PRIMARY KEY,
    exam_name TEXT NOT NULL,
    grade TEXT NOT NULL
)
''')

# Create a table for storing results
cursor.execute('''
CREATE TABLE IF NOT EXISTS results (
    result_id INTEGER PRIMARY KEY,
    roll_number INTEGER,
    exam_id INTEGER,
    subject_name TEXT,
    marks_obtained INTEGER,
    total_marks INTEGER,
    FOREIGN KEY (roll_number) REFERENCES students (roll_number),
    FOREIGN KEY (exam_id) REFERENCES exams (exam_id)
)
''')
connection.commit()
