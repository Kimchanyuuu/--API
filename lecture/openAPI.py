# OpenAPI 사용하기
# - platform.openapi.com
# API KEY 발급
# 카드등록

# 라이브러리 관리
# 1.venv(가상환경)
# 터미널 ->
# 2.Anaconda

# OpenAI 회사에서 GPT 관련 API 제공
# -https://openai.com/blog/openai-api



from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "클라우드 시스템에 대해 알려줘"}
  ]
)

print(completion.choices[0].message)


# OpenAI의 API를 사용해서 챗봇 문제점
#  1.개발이 어려움(나이도 상) -> 더 쉽게 개발 할 수 있는 무언가(프레임워크)가 필요!
#  2.챗봇 개발 완성 -> Bard 모델 변경 -> Bard API 처음부터 개발! -> 프레임워크(LLM)

# -> LangChain프레임워크(코드 동일: 모델 바꾸면) - pip install langchain
# 