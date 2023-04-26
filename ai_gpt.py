#https://di-acc2.com/programming/python/24841/
import openai
import os

filename = "code.py"
with open(filename, 'r') as f:
    code_string = f.read()

openai.organization = os.environ.get("AI_ORGANI")
openai.api_key = os.environ.get("AI_APIKEY")

# リクエストを送信する関数を定義する
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=200,
        n = 1,
    )
    message = completions.choices[0].text
    return message.strip()

def Ask_ChatGPT(message):
    
    # 応答設定
    completion = openai.ChatCompletion.create(
                 model    = "gpt-3.5-turbo",     # モデルを選択
                 messages = [{
                            "role":"user",
                            "content":message,   # メッセージ 
                            }],
    
                 max_tokens  = 1024,             # 生成する文章の最大単語数
                 n           = 1,                # いくつの返答を生成するか
                 stop        = None,             # 指定した単語が出現した場合、文章生成を打ち切る
                 temperature = 0.5,              # 出力する単語のランダム性（0から2の範囲） 0であれば毎回返答内容固定
    )
    
    # 応答
    response = completion.choices[0].message.content
    
    # 応答内容出力
    return response

# # リクエストを送信する
# prompt = "大谷翔平って誰ですか？"
# response = generate_text(prompt)

# リクエストを送信する
prompt = "以下のコードにコメントアウトをつけて" + "\n" + "\n" + code_string
response = Ask_ChatGPT(prompt)

#結果を保存
save_filename = "save_code.py"
with open(save_filename, mode="w", encoding="utf-8") as f:
    f.write(response)

print(response)