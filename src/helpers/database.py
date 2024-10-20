import sqlite3

from .settings import *

connection = sqlite3.connect(f"{base_path}/serp.db")
c = connection.cursor()

# The tables are created so dont run this function
def create_tables():
    with connection:
        c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            roll_number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            father_name TEXT,
            institution TEXT,
            level TEXT,
            year TEXT,
            contact_no INTEGER,
            mail TEXT,
            address TEXT
        )
        ''')

    with connection:
        c.execute('''
        CREATE TABLE IF NOT EXISTS ssc_cs_results (
            result_id INTEGER PRIMARY KEY,
            roll_number INTEGER,
            exam_name TEXT,
            math INTEGER,
            physics INTEGER,
            chemistry INTEGER,
            computer INTEGER,
            pak_studies INTEGER,
            islamiyat INTEGER,
            urdu INTEGER,
            english INTEGER,
            total_marks INTEGER,
            FOREIGN KEY (roll_number) REFERENCES students (roll_number)
        )
        ''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS ssc_pm_results (
            result_id INTEGER PRIMARY KEY,
            roll_number INTEGER,
            exam_name TEXT,
            math INTEGER,
            physics INTEGER,
            chemistry INTEGER,
            biology INTEGER,
            pak_studies INTEGER,
            islamiyat INTEGER,
            urdu INTEGER,
            english INTEGER,
            total_marks INTEGER,
            FOREIGN KEY (roll_number) REFERENCES students (roll_number)
        )
        ''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS hssc_cs_results (
            result_id INTEGER PRIMARY KEY,
            roll_number INTEGER,
            exam_name TEXT,
            math INTEGER,
            physics INTEGER,
            computer INTEGER,
            islamiyat_pak_studies INTEGER,
            urdu INTEGER,
            english INTEGER,
            total_marks INTEGER,
            FOREIGN KEY (roll_number) REFERENCES students (roll_number)
        )
        ''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS hssc_pm_results (
            result_id INTEGER PRIMARY KEY,
            roll_number INTEGER,
            exam_name TEXT,
            physics INTEGER,
            chemistry INTEGER,
            biology INTEGER,
            islamiyat_pak_studies INTEGER,
            urdu INTEGER,
            english INTEGER,
            total_marks INTEGER,
            FOREIGN KEY (roll_number) REFERENCES students (roll_number)
        )
        ''')

def add_student(roll_no, student_name, std_father_name, institution, level, year, contact_no, mail, address):
    try:
        with connection:
            c.execute('''
            INSERT INTO students (roll_number, name, father_name, institution, level, year, contact_no, mail, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (roll_no, student_name, std_father_name, institution, level, year, contact_no, mail, address)
            )
        print("Student added successfully.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def get_student(roll_no):
    try:
        with connection:
            c.execute('''
            SELECT name, father_name, institution, level, year, contact_no, mail, address 
            FROM students 
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        
        student_info = c.fetchone()
        
        if student_info:
            return {
                "name": student_info[0 ],
                "father_name": student_info[1],
                "institution": student_info[2],
                "level": student_info[3],
                "year": student_info[4],
                "contact_no": student_info[5],
                "mail": student_info[6],
                "address": student_info[7]
            }
        else:
            return None
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return None
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# if student already exists, return True otherwise return False
def student_exist(roll_no):
    try:
        with connection:
            c.execute('''
            SELECT COUNT(*) 
            FROM students 
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        count = c.fetchone()[0]
        return count > 0
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def delete_student(roll_no):
    try:
        with connection:
            c.execute('''
            DELETE FROM students 
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        with connection:
            c.execute('''
            DELETE FROM ssc_cs_results
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        with connection:
            c.execute('''
            DELETE FROM ssc_pm_results
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        with connection:
            c.execute('''
            DELETE FROM hssc_cs_results
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        with connection:
            c.execute('''
            DELETE FROM hssc_pm_results
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        print("Student deleted successfully.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    
def add_result_2_cs_ssc(roll_no, exam_name, math, physics, chemistry, computer, pak_studies,
               islamiyat, urdu, english, total_marks):
    try:
        with connection:
            c.execute('''
            INSERT INTO ssc_cs_results (roll_number, exam_name, math, physics, chemistry, computer,
                                pak_studies, islamiyat, urdu, english, total_marks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (roll_no, exam_name, math, physics, chemistry, computer,
                pak_studies, islamiyat, urdu, english, total_marks)
            )
        print("Result added successfully.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def add_result_2_pm_ssc(roll_no, exam_name, math, physics, chemistry, biology, pak_studies,
               islamiyat, urdu, english, total_marks):
    try:
        with connection:
            c.execute('''
            INSERT INTO ssc_pm_results (roll_number, exam_name, math, physics, chemistry, biology,
                                pak_studies, islamiyat, urdu, english, total_marks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (roll_no, exam_name, math, physics, chemistry, biology,
                pak_studies, islamiyat, urdu, english, total_marks)
            )
        print("Result added successfully.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def add_result_2_cs_hssc(roll_no, exam_name, math, physics, computer, 
                         islamiyat_pak_studies, urdu, english, total_marks):
    try:
        with connection:
            c.execute('''
            INSERT INTO hssc_cs_results (roll_number, exam_name, math, physics, computer,
                                islamiyat_pak_studies, urdu, english, total_marks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (roll_no, exam_name, math, physics, computer, 
                  islamiyat_pak_studies, urdu, english, total_marks)
            )
        print("Result added successfully.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def add_result_2_pm_hssc(roll_no, exam_name, physics, chemistry, biology, 
                         islamiyat_pak_studies, urdu, english, total_marks):
    try:
        with connection:
            c.execute('''
            INSERT INTO hssc_pm_results (roll_number, exam_name, physics, chemistry, biology
                                islamiyat_pak_studies, urdu, english, total_marks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (roll_no, exam_name, physics, chemistry, biology,
                islamiyat_pak_studies, urdu, english, total_marks)
            )
        print("Result added successfully.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Integrity error: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    
def get_results_4_cs_ssc(roll_no):
    try:
        c.execute('''
        SELECT name, father_name, institution, level, year
        FROM students 
        WHERE roll_number = ?
        ''', (roll_no,)
        )
        
        student_info = c.fetchone()
        
        if not student_info:
            return None 
        
        c.execute('''
        SELECT exam_name, math, physics, chemistry, computer, pak_studies, islamiyat, urdu, english, total_marks 
        FROM ssc_cs_results 
        WHERE roll_number = ?
        ''', (roll_no,))
        
        result_info = c.fetchone()
        
        if result_info:
            return {
                "roll_no": roll_no,
                "name": student_info[0],
                "father_name": student_info[1],
                "institution" : student_info[2],
                "level": student_info[3],
                "year": student_info[4],
                "exam_name": result_info[0],
                "math": result_info[1],
                "physics": result_info[2],
                "chemistry": result_info[3],
                "computer": result_info[4],
                "pak_studies": result_info[5],
                "islamiyat": result_info[6],
                "urdu": result_info[7],
                "english": result_info[8],
                "total_marks": result_info[9]
            }
        else:
            return None
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return None
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def get_results_4_pm_ssc(roll_no):
    try:
        c.execute('''
        SELECT name, father_name, institution, level, year
        FROM students 
        WHERE roll_number = ?
        ''', (roll_no,)
        )
        
        student_info = c.fetchone()
        
        if not student_info:
            return None 
        
        c.execute('''
        SELECT exam_name, math, physics, chemistry, biology, pak_studies, islamiyat, urdu, english, total_marks 
        FROM ssc_pm_results 
        WHERE roll_number = ?
        ''', (roll_no,))
        
        result_info = c.fetchone()
        
        if result_info:
            return {
                "roll_no": roll_no,
                "name": student_info[0],
                "father_name": student_info[1],
                "institution" : student_info[2],
                "level": student_info[3],
                "year": student_info[4],
                "exam_name": result_info[0],
                "math": result_info[1],
                "physics": result_info[2],
                "chemistry": result_info[3],
                "biology": result_info[4],
                "pak_studies": result_info[5],
                "islamiyat": result_info[6],
                "urdu": result_info[7],
                "english": result_info[8],
                "total_marks": result_info[9]
            }
        else:
            return None
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return None
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def get_results_4_cs_hssc(roll_no):
    try:
        c.execute('''
        SELECT name, father_name, institution, level, year
        FROM students 
        WHERE roll_number = ?
        ''', (roll_no,)
        )
        
        student_info = c.fetchone()
        
        if not student_info:
            return None 
        
        c.execute('''
        SELECT exam_name, math, physics, computer, islamiyat_pak_studies, urdu, english, total_marks 
        FROM hssc_cs_results 
        WHERE roll_number = ?
        ''', (roll_no,))
        
        result_info = c.fetchone()
        
        if result_info:
            return {
                "roll_no": roll_no,
                "name": student_info[0],
                "father_name": student_info[1],
                "institution" : student_info[2],
                "level": student_info[3],
                "year": student_info[4],
                "exam_name": result_info[0],
                "math": result_info[1],
                "physics": result_info[2],
                "computer": result_info[3],
                "islamiyat/pak_studies": result_info[4],
                "urdu": result_info[5],
                "english": result_info[6],
                "total_marks": result_info[7]
            }
        else:
            return None
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return None
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def get_results_4_pm_hssc(roll_no):
    try:
        c.execute('''
        SELECT name, father_name, institution, level, year
        FROM students 
        WHERE roll_number = ?
        ''', (roll_no,)
        )
        
        student_info = c.fetchone()
        
        if not student_info:
            return None 
        
        c.execute('''
        SELECT exam_name, chemistry, physics, biology, islamiyat_pak_studies, urdu, english, total_marks 
        FROM hssc_cs_results 
        WHERE roll_number = ?
        ''', (roll_no,))
        
        result_info = c.fetchone()
        
        if result_info:
            return {
                "roll_no": roll_no,
                "name": student_info[0],
                "father_name": student_info[1],
                "institution" : student_info[2],
                "level": student_info[3],
                "year": student_info[4],
                "exam_name": result_info[0],
                "chemistry": result_info[1],
                "physics": result_info[2],
                "biology": result_info[3],
                "islamiyat/pak_studies": result_info[4],
                "urdu": result_info[5],
                "english": result_info[6],
                "total_marks": result_info[7]
            }
        else:
            return None
    except sqlite3.OperationalError as e:
        print(f"Operational error: {e}")
        return None
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    