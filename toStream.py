# Chatgpt最基本的调用
import openai

# 填你的秘钥
openai.api_key = "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"
# 在messages加入system角色
messages = [{"role": "system", "content": "你是一个面向老人的管家"}]


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
        messages=messages,  # 信息
        temperature=0.3,  # 温度
        stream=True  # 启用流传输
    )
    collected_messages = []
    for chunk in completion:
        chunk_message = chunk['choices'][0]['delta'].get('content', '')  # 提取每次返回的信息
        collected_messages.append(chunk_message)  # 添加每次返回的信息，即最终结果
        print(chunk_message, end="")  # 打印每次返回的信息
    messages.append({"role": "assistant", "content": "".join(collected_messages)})  # 添加这次的聊天记录
    print()


# 调用chat_gpt函数
while True:
    question = input("question: ")
    chat_gpt(question)
