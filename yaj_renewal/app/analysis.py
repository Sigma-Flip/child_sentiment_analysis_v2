from .database import connect_db

# 부모가 자녀의 일기 목록을 조회하는 함수
def get_children_entries_for_parent(parent_keyNum):
    conn = connect_db()
    cursor = conn.cursor()
    
    # 부모의 자녀 keyNum 목록 조회
    cursor.execute("SELECT keyNum FROM userinfo_table WHERE relative = ?", (parent_keyNum,))
    child_keyNums = [row[0] for row in cursor.fetchall()]
    
    # 각 자녀의 일기 목록 조회
    all_entries = {}
    for child_keyNum in child_keyNums:
        cursor.execute(f'SELECT date, summary, evaluation, analysis, tl FROM "{child_keyNum}_table"')
        entries = cursor.fetchall()
        all_entries[child_keyNum] = entries  # 자녀 keyNum을 키로 하여 일기 데이터 저장

    conn.close()
    return all_entries

# 자녀의 특정 날짜 일기 상세 조회 함수
def get_detailed_entry(child_keyNum, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'SELECT summary, evaluation, analysis, tl FROM "{child_keyNum}_table" WHERE date = ?', (date,))
    details = cursor.fetchone()
    conn.close()
    return details

if __name__ == "__main__":
    # 부모 계정 "user3"의 자녀 일기 목록 조회
    all_entries = get_children_entries_for_parent("key3")
    print("자녀의 일기 목록:", all_entries)
    
    # 자녀 "key1"의 특정 날짜 일기 상세 조회 (예: 2024-11-05)
    details = get_detailed_entry("key1", "2024-11-05")
    print("특정 일기 상세 정보:", details)
