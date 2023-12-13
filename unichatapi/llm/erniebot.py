from typing import List, Tuple, Union, Generator
import erniebot
from loguru import logger
from .base import LLM

"""
参考：
https://github.com/PaddlePaddle/ERNIE-Bot-SDK
https://github.com/PaddlePaddle/ERNIE-Bot-SDK/blob/develop/docs/api_reference/chat_completion.md
https://github.com/PaddlePaddle/ERNIE-Bot-SDK/blob/develop/docs/authentication.md
"""

class ErnieBot(LLM):
    def __init__(self, api_type, access_token, model_name="ernie-bot") -> None:
        super().__init__()
        self.llm_type = 'erniebot'
        self.api_type = api_type
        self.access_token = access_token
        self.model_name = model_name

    def ask_stream(self, query: str, history: List[Tuple[str]] = [], incremental: bool = False,
                   temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0,
                   frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> Generator:
        log_flag = kwargs.get("log", True)
        if log_flag:
            logger.info(f"erniebot api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        if log_flag:
            logger.info(f"erniebot history: {history}, query={query}")
        messages = []
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        messages.append({"role": "user", "content": query})
        if log_flag:
            logger.info(f"erniebot final prompt: {messages}")
        if isinstance(timeout, tuple):
            timeout = timeout[0]
        penalty_score = max(1.0, min(presence_penalty + 1.0, 2.0))
        disable_search = kwargs.get("disable_search", False)
        response = erniebot.ChatCompletion.create(
            _config_=dict(
                api_type=self.api_type,
                access_token=self.access_token,
            ),
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            penalty_score=penalty_score,
            disable_search=disable_search,
            request_timeout=timeout
        )
        text = response.get_result()
        return text
        
    def ask(self, query: str, history: List[Tuple[str]] = [],
            temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0,
            frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> str:
        log_flag = kwargs.get("log", True)
        if log_flag:
            logger.info(f"erniebot api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        if log_flag:
            logger.info(f"erniebot history: {history}, query={query}")
        messages = []
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        messages.append({"role": "user", "content": query})
        if log_flag:
            logger.info(f"erniebot final prompt: {messages}")
        if isinstance(timeout, tuple):
            timeout = timeout[0]
        penalty_score = max(1.0, min(presence_penalty + 1.0, 2.0))
        disable_search = kwargs.get("disable_search", False)
        response = erniebot.ChatCompletion.create(
            _config_=dict(
                api_type=self.api_type,
                access_token=self.access_token,
            ),
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            penalty_score=penalty_score,
            disable_search=disable_search,
            request_timeout=timeout
        )
        text = response.get_result()
        return text
    
    @classmethod
    def config_info(cls) -> str:
        info = """
        erniebot config info:
        api_type: None (required)
        access_token: None (required)
        model_name: ernie-bot
        """
        return info
    
    @classmethod
    def check_config(cls, **kwargs)->bool:
        if kwargs.get("api_type", None) is None:
            return False
        if kwargs.get("access_token", None) is None:
            return False
        return True
            

    

