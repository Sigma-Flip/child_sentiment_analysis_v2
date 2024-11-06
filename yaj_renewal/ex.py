'''로그인 함수 잘 작동하는지 테스트 코드
아직 회원가입은 구현이 안되어 있고, 기존 db에 저장되어 있는 id/pw만 식별가능 '''
# database.py에 정의된 connect_db 함수와 login 함수를 사용
from app.database import connect_db
from app.auth import login

# ID와 비밀번호를 입력하여 로그인 시도
user_id = "test_user"
password = "password123"

# 로그인 함수 호출
user_info = login(user_id, password)

# 로그인 결과 출력
if user_info:
    print("로그인 성공!")
    print(f"사용자 정보:")
    print(f"  KeyNum: {user_info[0]}")
    print(f"  Name: {user_info[1]}")
    print(f"  Age: {user_info[2]}")
    print(f"  Gender: {user_info[3]}")
    print(f"  Type: {user_info[4]}")
else:
    print("로그인 실패: 잘못된 ID 또는 비밀번호")
