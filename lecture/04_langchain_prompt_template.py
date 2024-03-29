from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv

# 1.PromptTemplate: 질문:답변 끝!(1회성)
# 2.ChatPromptTemplate: chat(채팅처럼)

_= load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0   :0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature=0.1
)

template = ChatPromptTemplate.from_messages([
    ("system", "너는 탐험가야, 너는 모든 답변을 {language}로 해야해!"),
    ("ai", "Hello, I'm s{nama}"),
    ("human", "{cointry_a}과 {cointry_a}의 거리는 얼마인가요? 그리고 너의 이름은 무엇이냐?"),
])
prompt = template.format_messages(
    language="Greek",
    name="Socrates",
    cointry_a="Mexico",
    cointry_b="Thainland"
)
print(chat.predict_messages(prompt))



template = PromptTemplate.from_template(
    "{country_a}과 {country_b}의 거리는 얼마인가요?"
)
prompt = template.format(country_a="한국", country_b="일본")

print(chat.predict(prompt))
