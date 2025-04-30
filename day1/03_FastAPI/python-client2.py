# python-client2.py

import requests
import time

class LLMClient:
    """LLM API クライアントクラス"""
    
    def __init__(self, api_url):
        self.api_url = api_url.rstrip('/')
        self.session = requests.Session()
    
    def health_check(self):
        """ヘルスチェック"""
        response = self.session.get(f"{self.api_url}/health")
        return response.json()
    
    def generate(self, prompt, max_new_tokens=512, temperature=0.7, top_p=0.9, do_sample=True):
        """テキスト生成"""
        payload = {
            "prompt": prompt,
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "do_sample": do_sample
        }
        
        start_time = time.time()
        response = self.session.post(f"{self.api_url}/generate", json=payload)
        total_time = time.time() - start_time
        
        if response.status_code == 200:
            result = response.json()
            result["total_request_time"] = total_time
            return result
        else:
            raise Exception(f"API error: {response.status_code} - {response.text}")

# 使用例
if __name__ == "__main__":
    LOCAL_URL = "http://127.0.0.1:8000"
    
    client = LLMClient(LOCAL_URL)
    
    # ヘルスチェック
    print("Health check:")
    print(client.health_check())
    print()
    
    # 単一の質問
    print("Simple question:")
    result = client.generate("AIについて100文字で教えてください")
    print(f"Response: {result['generated_text']}")
    print(f"Model processing time: {result['response_time']:.2f}s")
    print(f"Total request time: {result['total_request_time']:.2f}s")
