from typing import List, Tuple, Union, Generator
from loguru import logger
import requests
import json
from .base import LLM


class ErnieBot4(LLM):
    def __init__(self, api_key, secret_key) -> None:
        super().__init__()
        self.llm_type = 'erniebot4'
        # curl 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【API Key】&client_secret=【Secret Key】'
        self.api_key = api_key  # api_key is actually access_token get from above curl command
        self.secreat_key = secret_key
        self.api = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + self.get_access_token()
        
    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.api_key, "client_secret": self.secreat_key}
        return str(requests.post(url, params=params).json().get("access_token"))

    def ask_stream(self, query: str, history: List[Tuple[str]] = [], incremental: bool = False,
                   temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0,
                   frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> Generator:
        logger.info(f"erniebot api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        history = [{'user': q, 'bot': a} for q, a in history]
        logger.info(f"erniebot history: {history}, query={query}")
        messages = []
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        messages.append({"role": "user", "content": query})
        data = {"messages": messages, "stream": True}
        logger.info(f"erniebot final prompt: {data}")
        response = requests.post(self.api, json=data, stream=True, timeout=timeout)
        all_content = ""
        data = b""
        for chunk in response:
            for line in chunk.splitlines(True):
                data += line
                if data.endswith((b"\r\r", b"\n\n", b"\r\n\r\n")):
                    line_str = data.decode()
                    json_str = line_str[6:]
                    json_data = json.loads(json_str)
                    text = json_data["result"]
                    if incremental:
                        yield text
                    else:
                        all_content += text
                        yield all_content
                    data = b""
        if data:
            line_str = data.decode()
            json_str = line_str[6:]
            json_data = json.loads(json_str)
            text = json_data["result"]
            if incremental:
                yield text
            else:
                all_content += text
                yield all_content
        
    def ask(self, query: str, history: List[Tuple[str]] = [],
            temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0,
            frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> str:
        # 获取是否需要打印日志的标记
        log_flag = kwargs.get("log", True)
        if log_flag:
            logger.info(f"erniebot api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        penalty_score = min(2.0, presence_penalty + 1.0)
        history = [{'user': q, 'bot': a} for q, a in history]
        if log_flag:
            logger.info(f"erniebot history: {history}, query={query}")
        messages = []
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        messages.append({"role": "user", "content": query})
        data = {"messages": messages, "stream": False, "temperature": temperature, "top_p": top_p, "penalty_score": penalty_score}
        if log_flag:
            logger.info(f"erniebot final prompt: {data}")
        response = requests.post(self.api, json=data, timeout=timeout)
        json_data = response.json()
        text = json_data["result"]
        return text
    
    @classmethod
    def config_info(cls) -> str:
        info = """
        erniebot config info:
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
            

    
