from app import auth, analysis
from app.core import yjbot,Prompts, model
import datetime
'''
process_student_entry : 
    1. 로그인 성공, 학생 계정일 때, 녹음을 진행하고(아직 구현 안 됌, 일단은 예시 데이터 사용) 
    2. 학생의 keyNum, name, age, gender, datetime, contents, timeline (STT 결과)를 받음. 
    3. 여기에서 contents & timeline을 사용해서 summary, evaluation, analysis, timeline(타임라인 요약)을 생성. 
    4. 3번에서 생성한 분석결과들을 해당 유저 테이블에 저장 (f{keyNum}_table)
    5. 연결 종료


main
    1. process_student_entry를 실행시켜서 학생의 정보를 저장
    2. 부모 계정으로 로그인
    3. db확인해보면 type이 student인 경우, relatives에 부모 keyNum이 적혀져 있음 (부모는 Null)
    4. 따라서 부모계정으로 로그인하면 relative 칼럼에 부모의 keynum을 가지고 있는 모든 자식들의 정보를 가져옴(keyNum값을 가져옴) 
    5. 가져온 자식들 for loop을 돌면서 (자식이 2명이상일 경우) db에 저장되어 있는 정보 조회 


* 일단 openai key가 필요함. 
* app을 패키지로 묶어놨는데 이게 참조가 어떤지 아직 잘 몰라서 확인 필요 
* 화면은 구현이 안되어 있음


'''
def process_student_entry(user_id, password):
    # 학생 계정으로 로그인
    user_info, _ = auth.login(user_id, password)
    if user_info and user_info[4] == 'student':  # 학생 계정 확인
        keyNum = user_info[0]  # 학생의 고유 keyNum
        print(f"학생 {user_info[1]}님이 로그인했습니다.")

        # 예시: 녹음 데이터 및 타임라인 (실제로는 녹음 후 STT 결과를 여기서 사용)
        data = {
            'key': keyNum,
            'name': user_info[1],
            'age': user_info[2],
            'gender': user_info[3],
            'datetime': datetime.datetime.now(),
            'contents': [
                "오늘은 정말 힘든 하루였어요.",
                "학교에서 계속 실수를 해서 선생님께 혼났어요.",
                "친구들과의 사이도 뭔가 어색해져서 마음이 무거웠어요.",
                "점심시간에도 혼자 앉아서 밥을 먹었어요.",
                "집에 돌아오는 길에 비가 내려 더 우울해졌어요.",
                "우산을 챙기지 않아서 옷이 다 젖었어요.",
                "집에 와서 숙제를 하려는데 집중이 잘 안 돼요.",
                "부모님도 오늘따라 저한테 잔소리가 많으셨어요.",
                "하루가 빨리 끝나서 내일은 좀 나아졌으면 좋겠어요.",
                "그래도, 언젠가 이런 날들이 지나가길 바라고 있어요."
            ],
            'timeline': [
                "1\n00:00:01,000 --> 00:00:03,500\n오늘은 정말 힘든 하루였어요.",
                "2\n00:00:04,000 --> 00:00:06,500\n학교에서 계속 실수를 해서 선생님께 혼났어요.",
                "3\n00:00:07,000 --> 00:00:10,000\n친구들과의 사이도 뭔가 어색해져서 마음이 무거웠어요.",
                "4\n00:00:10,500 --> 00:00:13,500\n점심시간에도 혼자 앉아서 밥을 먹었어요.",
                "5\n00:00:14,000 --> 00:00:16,000\n집에 돌아오는 길에 비가 내려 더 우울해졌어요.",
                "6\n00:00:16,500 --> 00:00:18,500\n우산을 챙기지 않아서 옷이 다 젖었어요.",
                "7\n00:00:19,000 --> 00:00:21,500\n집에 와서 숙제를 하려는데 집중이 잘 안 돼요.",
                "8\n00:00:22,000 --> 00:00:24,500\n부모님도 오늘따라 저한테 잔소리가 많으셨어요.",
                "9\n00:00:25,000 --> 00:00:27,500\n하루가 빨리 끝나서 내일은 좀 나아졌으면 좋겠어요.",
                "10\n00:00:28,000 --> 00:00:30,500\n그래도, 언젠가 이런 날들이 지나가길 바라고 있어요."
            ]
        }

        # LLMWrapper 인스턴스 생성
        case = yjbot(info=data)
        
        # 분석 수행
        summary = case.showSummary()
        evaluation = case.showEvaluation()
        analysis = case.showAnalysis()
        timeline = case.showTimeline()

        # 데이터베이스에 저장
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO "{keyNum}_table" (date, contents, timeline, summary, evaluation, analysis, tl)
                           VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                       (data['datetime'].strftime('%Y-%m-%d %H:%M:%S'), 
                        '\n'.join(data['contents']), 
                        '\n'.join(data['timeline']), 
                        summary, evaluation, analysis, timeline))
        
        conn.commit()
        conn.close()
        print(f"학생 {user_info[1]}의 일기가 성공적으로 데이터베이스에 저장되었습니다.")
        
    else:
        print("학생 계정이 아니거나 잘못된 로그인 정보입니다.")

def main():
    # 학생 계정으로 로그인 및 일기 저장
    process_student_entry("user1", "pass1")  # 예: user1 학생 로그인

    # 부모 계정으로 로그인 및 자녀 일기 조회
    user_info, child_keyNums = auth.login("user3", "pass3")
    if user_info and user_info[4] == 'parent':  # 부모 계정 확인
        print(f"{user_info[1]}님의 자녀 목록: {child_keyNums}")
        
        # 각 자녀의 일기 목록 조회
        all_entries = analysis.get_children_entries_for_parent(user_info[0])
        for child_keyNum, entries in all_entries.items():
            print(f"\n자녀 {child_keyNum}의 일기 목록:")
            for entry in entries:
                print(f"Date: {entry[0]}, Summary: {entry[1]}, Evaluation: {entry[2]}")
        
        # 특정 자녀의 특정 날짜 일기 상세 조회
        selected_date = "2024-11-05"  # 예시 날짜
        details = analysis.get_detailed_entry(child_keyNums[0], selected_date)  # 첫 자녀의 일기 조회
        print(f"\n{selected_date} 일기의 상세 정보:", details)
    else:
        print("부모 계정이 아니거나 잘못된 로그인 정보입니다.")

if __name__ == "__main__":
    main()
