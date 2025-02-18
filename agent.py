from model_utils import invoke_agent  # استيراد دالة استدعاء الوكيل

# تجربة تنفيذ أمر
response = invoke_agent("Repeat after me: Hello, Agent!")
print(response)
