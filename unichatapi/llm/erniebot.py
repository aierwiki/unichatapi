from typing import List, Tuple, Union, Generator
import qianfan
from loguru import logger
from .base import LLM


class ErnieBot(LLM):
    def __init__(self, api_key, secret_key, model_name="ERNIE-Bot-turbo") -> None:
        super().__init__()
        self.llm_type = 'erniebot'
        self.api_key = api_key
        self.secret_key = secret_key
        self.model_name = model_name
        self.chat_comp = qianfan.ChatCompletion(ak=self.api_key, sk=self.secret_key)

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
        if isinstance(timeout, tuple):
            timeout = timeout[0]
        penalty_score = max(1.0, min(presence_penalty + 1.0, 2.0))
        resp = self.chat_comp.ado(model=self.model_name, messages=messages, stream=True, 
                                  temperature=temperature, top_p=top_p, penalty_score=penalty_score,
                                  request_timeout=timeout)
        total_result = ""
        for r in resp:
            if r['code'] != 200:
                logger.error('Code: %d' % (r['code']))
                raise Exception('API ERROR')
            result = r['result']
            total_result += result
            if incremental:
                yield result
            else:
                yield total_result

        
    def ask(self, query: str, history: List[Tuple[str]] = [],
            temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0,
            frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> str:
        logger.info(f"erniebot api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        history = [{'user': q, 'bot': a} for q, a in history]
        logger.info(f"erniebot history: {history}, query={query}")
        messages = []
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        messages.append({"role": "user", "content": query})
        data = {"messages": messages, "stream": False}
        logger.info(f"erniebot final prompt: {data}")
        if isinstance(timeout, tuple):
            timeout = timeout[0]
        penalty_score = max(1.0, min(presence_penalty + 1.0, 2.0))
        resp = self.chat_comp.do(model=self.model_name, messages=messages, stream=False,
                                  temperature=temperature, top_p=top_p, penalty_score=penalty_score,
                                  request_timeout=timeout)
        if resp['code'] != 200:
            logger.error('Code: %d' % (resp['code']))
            raise Exception('API ERROR')
        text = resp['body']['result']
        return text
    
    @classmethod
    def config_info(cls) -> str:
        info = """
        erniebot config info:
        api_key: None (required)
        secret_key: None (required)
        model_name: ernie-bot-turbo
        """
        return info
    
    @classmethod
    def check_config(cls, **kwargs)->bool:
        if kwargs.get("api_key", None) is None:
            return False
        if kwargs.get("secret_key", None) is None:
            return False
        return True
            

    

