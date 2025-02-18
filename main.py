from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class QueryModel(BaseModel):
    query: str

@app.post("/chat/")
def chat(query: QueryModel):
    try:
        print(f"Received query: {query.query}")  # طباعة الاستعلام للتحقق
        response = agent.invoke({"input": query.query, "chat_history": []})  
        print(f"Response: {response}")  # طباعة الاستجابة للتحقق
        return {"response": response}
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # طباعة الخطأ في الكونسول
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
