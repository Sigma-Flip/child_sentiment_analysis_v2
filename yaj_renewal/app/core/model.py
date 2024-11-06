from utils import Prompts  
from openai import OpenAI
prompts = Prompts()

class Model:
    def __init__(self):
        self.model_name = 'gpt-4o-mini'
        self.client = self.setClient()
        self.info = {}

    @staticmethod
    def setClient():
        api_key = 'YOUROUR_API_KEY_HERE'
        client = OpenAI(api_key=api_key)
        print("Client set up successfully.")
        return client

    def updateInfo(self, info):
        self.info = info

    def create(self, work, contents):
        if work not in ['Summary', 'Evaluation', 'Analysis', 'Timeline']:
            raise KeyError("Invalid work type. Must be one of ['Summary', 'Evaluation', 'Analysis', 'Timeline']")
        prompt = prompts.getPrompt(work)

        if work == 'Timeline':
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"{prompt}\n\n일기 내용:\n{''.join(self.info['timeline'])}",
                    }
                ],
                model=self.model_name
            )
            return chat_completion.choices[0].message.content
        else:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"{prompt}\n\n일기 내용:\n{''.join(self.info['contents'])}",
                    }
                ],
                model=self.model_name
            )
            return chat_completion.choices[0].message.content

model = Model()
