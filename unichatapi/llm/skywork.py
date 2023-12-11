from typing import List, Tuple, Union, Generator
from loguru import logger
import requests
import json
import time
import hashlib
from .base import LLM


class SkyWork(LLM):
    def __init__(self, api_key:str, secret_key:str, api_url:str=None, model:str=None) -> None:
        super().__init__()
        self.llm_type = 'skywork'
        self.api_key = api_key
        self.secret_key = secret_key
        if api_url is None:
            self.api = "https://sky-api.singularity-ai.com/saas/api/v3/generate"
        else:
            self.api = api_url
        if model is None:
            self.model = "sky-chat-3.5"
        else:
            self.model = model
    
    def ask_stream(self, query: str, history: List[Tuple[str]] = [], incremental: bool = False,
                   temperature: float = 0.66, top_p: float = 1.0, presence_penalty: float = 1.0,
                   frequency_penalty: float = 1.0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> Generator:
        logger.info(f"skywork api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        logger.info(f"skywork history: {history}, query={query}")
        timestamp = str(int(time.time()))
        sign_content = self.api_key + self.secret_key + timestamp
        sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()

        headers={
            "app_key": self.api_key,
            "timestamp": timestamp,
            "sign": sign_result,
            "Content-Type": "application/json",
            "stream": "false" # or change to "false" 不处理流式返回内容
        }
        param = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": 1,
            "repetition_penalty": frequency_penalty,
            "length_penalty": presence_penalty,
        }

        messages = []
        messages.append({"role":"system", "content":"你是 sky-chat"})
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "bot", "content": a})
        messages.append({"role": "user", "content": query})
        
        data = {"messages": messages, "model": self.model, "param": param}
        response = requests.post(self.api, headers=headers, json=data, stream=True, timeout=timeout)

        for line in response.iter_lines():
            if line:
                resp_data = json.loads(line.decode('utf-8'))
                if resp_data.get('code') == 200:
                    yield resp_data.get('resp_data', {}).get('reply')
        yield ''
        
    def ask(self, query: str, history: List[Tuple[str]] = [],
            temperature: float = 0.66, top_p: float = 1.0, presence_penalty: float = 1.0,
            frequency_penalty: float = 1.0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> str:
        # 获取是否需要打印日志的标记
        log_flag = kwargs.get("log", True)
        if log_flag:
            logger.info(f"skywork api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")

        timestamp = str(int(time.time()))
        sign_content = self.api_key + self.secret_key + timestamp
        sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()

        headers={
            "app_key": self.api_key,
            "timestamp": timestamp,
            "sign": sign_result,
            "Content-Type": "application/json",
            "stream": "false" # or change to "false" 不处理流式返回内容
        }
        param = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": 1,
            "repetition_penalty": frequency_penalty,
            "length_penalty": presence_penalty,
        }

        if log_flag:
            logger.info(f"skywork history: {history}, query={query}")
        messages = []
        messages.append({"role":"system", "content":"你是 sky-chat"})
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "bot", "content": a})
        messages.append({"role": "user", "content": query})
        
        data = {"messages": messages, "model": self.model, "param": param}
        if log_flag:
            logger.info(f"skywork final prompt: {data}")
        response = requests.post(self.api, headers=headers, json=data, timeout=timeout, stream=False)
        json_data = response.json()
        text = json_data["resp_data"]["reply"]
        return text
    
    @classmethod
    def config_info(cls) -> str:
        info = """
        skywork config info:
        api_key: None (required)
        secret_key: None (required)
        """
        return info
    
    @classmethod
    def check_config(cls, **kwargs)->bool:
        if kwargs.get("api_key", None) is None:
            return False
        if kwargs.get("secret_key", None) is None:
            return False
        return True
