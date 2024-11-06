import json
import os
import datetime
from .utils import prompts
from .model import model



data = {
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

class LLMWrapper:
    def __init__(self, info: dict):
        self.info = info
        self._summary = ""
        self._evaluation = ""
        self._analysis = ""
        self._timeline = ""
        model.updateInfo(self.info)

    def showMetaInfo(self):
        print("[Meta Information]")
        print(f"Name: {self.info['name']}, Age: {self.info['age']}, Gender: {self.info['gender']}")
        print(f"Date: {self.info['datetime'].strftime('%Y-%m-%d')}, Time: {self.info['datetime'].strftime('%H:%M:%S')}")

    def showResult(self, result_type):
        print(f"\n[{result_type}]")

    def summarize(self):
        self._summary = model.create(work='Summary', contents=self.info['contents'])
        return self._summary

    def showSummary(self):
        self.showResult("Summary")
        if not self._summary:
            self.summarize()
        print(self._summary)

    def evaluate(self):
        self._evaluation = model.create(work="Evaluation", contents=self.info['contents'])
        return self._evaluation

    def showEvaluation(self):
        self.showResult("Evaluation")
        if not self._evaluation:
            self.evaluate()
        print(self._evaluation)

    def analyze(self):
        self._analysis = model.create(work='Analysis', contents=self.info['contents'])
        return self._analysis

    def showAnalysis(self):
        self.showResult("Analysis")
        if not self._analysis:
            self.analyze()
        print(self._analysis)

    def createTimeline(self):
        self._timeline = model.create(work='Timeline', contents=self.info['contents'])
        return self._timeline

    def showTimeline(self):
        self.showResult("Timeline")
        if not self._timeline:
            self.createTimeline()
        print(self._timeline)

    def showAll(self):
        print("[Full Report]")
        self.showMetaInfo()
        self.showSummary()
        self.showEvaluation()
        self.showAnalysis()
        self.showTimeline()
        print("[End of Report]")



if __name__ == "__main__":
    parent = LLMWrapper(info=data)
    parent.showAll()

