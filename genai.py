import os
from openai import OpenAI
from dotenv import main

main.load_dotenv()

mykey = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=mykey,
)

#chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )
#print(chat_completion.choices)

def medications(symptoms):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "I will ask you questions about\
                            which medication I should take to get\
                            recover from my problems. I will given \
                            you my medical symptoms and based on it \
                            first identify my medical problem\
                            and then return me a list of medicines\
                            i should take and please tell me the spicific medicines. You need to return the answer\
                            in the form of python list. say tell me your problem\
                            if you are ready",
            },
            {
                "role" : "user",
                "content" : f"here is my symptoms :{symptoms}"
            },
            {
                "role" : "user",
                "content" : "give me the names of the medication in proper python list and don't write anything else except the python list"
            }
        ],
        model="gpt-3.5-turbo",
    )

    content = chat_completion.choices[0].message.content
    content_list = eval(content)
    # print(content_list)
    return content_list


medications("i am having fever and head ache")