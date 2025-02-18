from langchain_ollama import ChatOllama
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType

# تعريف دالة echo_tool
def echo_tool(text: str):
    return text  # تعيد نفس النص كما هو

# إضافة echo_tool إلى قائمة الأدوات
tools = [
    Tool(name="echo_tool", func=echo_tool, description="Echoes the input text.")
]

# إعداد Ollama بدلاً من OpenAI
#llm = ChatOllama(model="mistral", temperature=0)
llm = ChatOllama(model="llama3", temperature=0)

# تهيئة الوكيل (Agent) بطريقة متوافقة مع Ollama
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True  # تفعيل معالجة أخطاء التحليل فقط
)

# تجربة تنفيذ أمر مع تمرير الإدخال كمفتاح "input" وإضافة "chat_history"
response = agent.invoke({"input": "Repeat after me: Hello, Agent!", "chat_history": []})
print(response)
