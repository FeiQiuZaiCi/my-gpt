# Chatgpt最基本的调用
import openai

# 填你的秘钥
openai.api_key = "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"
# 在messages加入system角色
messages = [{"role": "system", "content": "你要在每一句的最后加上喵"}]


# 提问代码
def chat_gpt(question):
    # 你的问题
    messages.append({"role": "user", "content": question})
    # 调用 ChatGPT 接口
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # role为角色.其中角色有{user,system,assistant}
        # 当角色为user时,content中的内容为提问的问题
        # 当角色为system时,content中的内容可以设置gpt的行为模式
        # 当角色为assistant时,content中存储之前的对话,建立对话历史记录
        messages=messages
    )
    print(completion.choices[0].message.content)


# 调用chat_gpt函数
chat_gpt("怎么做蛋炒饭")
