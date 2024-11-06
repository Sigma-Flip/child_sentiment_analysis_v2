import sqlite3
import os
"""
필요한 데이터베이스 생성 함수 및 데이터베이스 연결 함수 

"""

# SQLite 데이터베이스 파일 경로 설정
DB_PATH = os.path.join(os.path.dirname(__file__), 'user_diary.db')

# SQLite 데이터베이스 연결 함수
def connect_db():
    return sqlite3.connect(DB_PATH)

# 데이터베이스 테이블 생성 함수
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    # id_table 생성
    cursor.execute('''CREATE TABLE IF NOT EXISTS id_table (
                        id TEXT PRIMARY KEY,
                        password TEXT,
                        keyNum TEXT UNIQUE
                     )''')
    
    # userinfo_table 생성
    cursor.execute('''CREATE TABLE IF NOT EXISTS userinfo_table (
                        keyNum TEXT PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        gender TEXT,
                        type TEXT CHECK(type IN ('student', 'parent')),
                        relative TEXT
                     )''')

    conn.commit()
    conn.close()
    print("테이블이 성공적으로 생성되었습니다.")

# 예시 데이터 추가 함수
def insert_example_data():
    conn = connect_db()
    cursor = conn.cursor()
    
    # id_table과 userinfo_table에 예시 데이터 추가
    users = [
        ("user1", "pass1", "key1", "Alice", 10, "F", "student", "key3"),
        ("user2", "pass2", "key2", "Bob", 12, "M", "student", "key4"),
        ("user3", "pass3", "key3", "Charlie", 35, "M", "parent", None),
        ("user4", "pass4", "key4", "Daisy", 40, "F", "parent", None),
        ("user5", "pass5", "key5", "Eve", 11, "F", "student", "key3")
    ]
    
    for user in users:
        # id_table에 삽입
        cursor.execute("INSERT INTO id_table (id, password, keyNum) VALUES (?, ?, ?)", (user[0], user[1], user[2]))
        
        # userinfo_table에 삽입
        cursor.execute("INSERT INTO userinfo_table (keyNum, name, age, gender, type, relative) VALUES (?, ?, ?, ?, ?, ?)", 
                       (user[2], user[3], user[4], user[5], user[6], user[7]))
        
        # 각 유저의 keyNum에 따른 빈 테이블 생성
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{user[2]}_table" (
                            date TEXT,
                            contents TEXT,
                            timeline TEXT,
                            summary TEXT,
                            evaluation TEXT,
                            analysis TEXT,
                            tl TEXT
                         )''')

    conn.commit()
    conn.close()
    print("예시 데이터가 성공적으로 추가되었습니다.")

if __name__ == "__main__":
    # 기본 테이블 생성
    create_tables()
    
    # 예시 데이터 추가
    insert_example_data()
