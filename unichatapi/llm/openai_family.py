from typing import List, Tuple, Union, Generator
from openai import OpenAI
from loguru import logger
from .base import LLM

"""
参考：
https://platform.openai.com/docs/guides/text-generation
"""

class OpenAIFamily(LLM):
    def __init__(self, api_key, llm_type, base_url=None, model_name="gpt-3.5-turbo") -> None:
        super().__init__()
        self.api_key = api_key
        self.llm_type = llm_type
        self.model_name = model_name
        self.client = OpenAI(base_url=base_url, api_key=api_key)

    def ask_stream(self, query: str, history: List[Tuple[str]] = [], incremental: bool = False,
                   temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0,
                   frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> Generator:
        text = ""
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
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            timeout=timeout
        )
        text = ""
        for choice in response.choices:
            data = choice.model_dump()
            text += data["message"]["content"]
        return text
    
    @classmethod
    def config_info(cls) -> str:
        info = """
        openai config info:
        api_key: None (required)
        llm_type: None (required)
        base_url: None
        model_name: "gpt-3.5-turbo"
        """
        return info
    
    @classmethod
    def check_config(cls, **kwargs)->bool:
        if kwargs.get("api_key", None) is None:
            return False
        if kwargs.get("llm_type", None) is None:
            return False
        return True
            

    

