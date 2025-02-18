from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_ollama import ChatOllama
from question_utils import self_ask  # استيراد دالة التحليل
from search_utils import web_search  # استيراد دالة البحث

# إعداد الأدوات
tools = [
    Tool(name="self_ask", func=self_ask, description="Analyzes text and provides insights."),
    Tool(name="web_search", func=web_search, description="Searches Google and returns the top result.")
]

# إعداد نموذج اللغة
llm = ChatOllama(model="mistral", temperature=0)

# إعداد الوكيل (Agent)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# دالة لاستدعاء الوكيل مع إدخال
def invoke_agent(input_text: str, chat_history=None):
    if chat_history is None:
        chat_history = []
    return agent.invoke({"input": input_text, "chat_history": chat_history})
