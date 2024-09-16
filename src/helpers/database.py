import sqlite3

base_path = r'/home/sbalghari/Documents/GitHub/SERP-Manager'

connection = sqlite3.connect(f"{base_path}/serp.db")
c = connection.cursor()

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
        CREATE TABLE IF NOT EXISTS results (
            result_id INTEGER PRIMARY KEY,
            roll_number INTEGER,
            exam_name TEXT,
            math INTEGER,
            physics INTEGER,
            chemistry INTEGER,
            biology INTEGER,
            computer INTEGER,
            pak_studies INTEGER,
            islamiyat INTEGER,
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
    
def add_result(roll_no, exam_name, math, physics, chemistry, biology, computer, pak_studies,
               islamiyat, urdu, english, total_marks):
    try:
        with connection:
            c.execute('''
            INSERT INTO results (roll_number, exam_name, math, physics, chemistry, biology, computer,
                                pak_studies, islamiyat, urdu, english, total_marks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (roll_no, exam_name, math, physics, chemistry, biology, computer,
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

def get_results(roll_no):
    try:
        with connection:
            c.execute('''
            SELECT name, father_name, level, year 
            FROM students 
            WHERE roll_number = ?
            ''', (roll_no,)
            )
        
        student_info = c.fetchone()
        
        if not student_info:
            return None 
        
        c.execute('''
        SELECT exam_name, math, physics, chemistry, biology, computer, pak_studies, islamiyat, urdu, english, total_marks 
        FROM results 
        WHERE roll_number = ?
        ''', (roll_no,))
        
        result_info = c.fetchone()
        
        if result_info:
            return {
                "roll_number": roll_no,
                "name": student_info[0],
                "father_name": student_info[1],
                "level": student_info[2],
                "year": student_info[3],
                "exam_name": result_info[0],
                "math": result_info[1],
                "physics": result_info[2],
                "chemistry": result_info[3],
                "biology": result_info[4],
                "computer": result_info[5],
                "pak_studies": result_info[6],
                "islamiyat": result_info[7],
                "urdu": result_info[8],
                "english": result_info[9],
                "total_marks": result_info[10]
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