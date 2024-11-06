from database import connect_db
import os

# 로그인 함수
def login(user_id, password):
    conn = connect_db()
    cursor = conn.cursor()
    
    # id_table에서 사용자 인증
    cursor.execute("SELECT * FROM id_table WHERE id = ? AND password = ?", (user_id, password))
    user = cursor.fetchone()
    if user:
        keyNum = user[2]
        
        # userinfo_table에서 추가 사용자 정보 가져오기
        cursor.execute("SELECT * FROM userinfo_table WHERE keyNum = ?", (keyNum,))
        userinfo = cursor.fetchone()
        
        # 로그인한 사용자가 부모일 경우 자녀의 keyNum을 조회
        if userinfo and userinfo[4] == 'parent':  # type == 'parent' 확인
            cursor.execute("SELECT keyNum FROM userinfo_table WHERE relative = ?", (keyNum,))
            child_keyNums = [row[0] for row in cursor.fetchall()]  # 자녀의 keyNum 목록
            
            # 부모 정보와 자녀 keyNum 목록 반환
            conn.close()
            return userinfo, child_keyNums
        
        conn.close()
        return userinfo, None  # 부모가 아니면 자녀 keyNum 없음
    conn.close()
    return None, None

if __name__ == "__main__":
    # 테스트: 부모 계정으로 로그인
    user_info, child_keyNums = login("user3", "pass3")
    if user_info:
        print("로그인 성공!")
        print("사용자 정보:", user_info)
        print("자녀 keyNum 목록:", child_keyNums)
    else:
        print("로그인 실패: 잘못된 ID 또는 비밀번호")
