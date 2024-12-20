from core import yjbot
import datetime
'''
core폴더에 있는 모델 임포트. 

데이터는 해당 예시 데이터형식으로 넣어줘야함. (딕셔너리형태, key 이름 그대로.)


'''
data = {
    'key': '0002',
    'name': 'Jane',
    'age': 17,
    'gender': 'female',
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
data2 = {
    'key': '0001',
    'name': 'John',
    'age': 18,
    'gender': 'male',
    'datetime': datetime.datetime.now(),
    'contents': [
        "오늘은 정말 재미있는 꿈을 꿨어요.",
        "하늘에 커다란 풍선들이 떠다니고 있었어요.",
        "그리고 그 풍선을 타고 친구들이랑 모험을 떠났어요.",
        "숲속을 지나서 무지개 다리를 건넜어요.",
        "어디선가 고양이들이 나타나 우리와 함께 놀았어요.",
        "그리고 신기한 나무를 만났어요. 나무가 말을 하더라고요.",
        "나무가 내 이름을 부르는데 정말 놀랐어요!",
        "마지막엔 바다로 갔는데 물고기들이 춤을 추고 있었어요.",
        "그 꿈에서 깼을 때, 너무 아쉬웠어요.",
        "언젠가 진짜로 그런 모험을 떠나고 싶어요."
    ],
    'timeline': [
        "1\n00:00:01,000 --> 00:00:03,500\n오늘은 정말 재미있는 꿈을 꿨어요.",
        "2\n00:00:04,000 --> 00:00:06,500\n하늘에 커다란 풍선들이 떠다니고 있었어요.",
        "3\n00:00:07,000 --> 00:00:10,000\n그리고 그 풍선을 타고 친구들이랑 모험을 떠났어요.",
        "4\n00:00:10,500 --> 00:00:13,500\n숲속을 지나서 무지개 다리를 건넜어요.",
        "5\n00:00:14,000 --> 00:00:16,000\n어디선가 고양이들이 나타나 우리와 함께 놀았어요.",
        "6\n00:00:16,500 --> 00:00:18,500\n그리고 신기한 나무를 만났어요. 나무가 말을 하더라고요.",
        "7\n00:00:19,000 --> 00:00:21,500\n나무가 내 이름을 부르는데 정말 놀랐어요!",
        "8\n00:00:22,000 --> 00:00:24,500\n마지막엔 바다로 갔는데 물고기들이 춤을 추고 있었어요.",
        "9\n00:00:25,000 --> 00:00:27,500\n그 꿈에서 깼을 때, 너무 아쉬웠어요.",
        "10\n00:00:28,000 --> 00:00:30,500\n언젠가 진짜로 그런 모험을 떠나고 싶어요."
    ]
}



# yjbot으로 LLMWrapper 인스턴스 생성
case1 = yjbot(info=data)

print('---metainfo---')
case1.showMetaInfo()
case1.showSummary()
case1.showEvaluation()
case1.showAnalysis()
case1.showTimeline()



case2 = yjbot(info = data2)

print('---metainfo---')
case2.showMetaInfo()
case2.showSummary()
case2.showEvaluation()
case2.showAnalysis()
case2.showTimeline()

