# app_2.py

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import time
import requests

# LLM API クライアントのコード（仮のモデルを使用）
class LLMClient:
    """LLM API クライアントクラス"""
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.session = requests.Session()
    
    def generate(self, prompt, max_new_tokens=512, temperature=0.7, top_p=0.9, do_sample=True):
        """テキスト生成"""
        # ダミー応答（実際のLLMサーバが無いため）
        start = time.time()
        response = {
            "generated_text": f"（仮応答）'{prompt}' に関する出力です。",
            "response_time": round(time.time() - start, 2)
        }
        return response

# FastAPI アプリケーションを定義
app = FastAPI()

class TextGenerationRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.9
    do_sample: bool = True

# ヘルスチェック用
@app.get("/health")
async def health():
    return {"status": "ok"}

# API エンドポイントの定義
@app.post("/generate")
async def generate_text(request: TextGenerationRequest):
    result = LLMClient('http://localhost:8000').generate(
        request.prompt, 
        max_new_tokens=request.max_new_tokens,
        temperature=request.temperature,
        top_p=request.top_p,
        do_sample=request.do_sample
    )
    return result
    