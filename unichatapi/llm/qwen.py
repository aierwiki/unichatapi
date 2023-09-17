from typing import List, Tuple, Union, Generator
from loguru import logger
from dashscope import Generation as QWenGeneration
from http import HTTPStatus
from .base import LLM

class Qwen(LLM):
    def __init__(self, api_key:str, model_name='qwen-7b-chat-v1') -> None:
        super().__init__()
        self.api_key = api_key
        self.model_name = model_name
        self.llm_type = 'qwen'
        
    def ask_stream(self, query: str, history: List[Tuple[str]] = [], incremental: bool = False, 
                   temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0, 
                   frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> Generator:
        logger.info(f"qwen api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        history = [{'user': q, 'bot': a} for q, a in history]
        logger.info(f"qwen-7b history: {history}, query={query}")
        responses = QWenGeneration.call(
            model=self.model_name,
            prompt=query,
            history=history,
            stream=True,
            api_key=self.api_key,
            top_p=top_p,
            timeout=timeout
        )
        previous = ""
        for response in responses:
            if response.status_code == HTTPStatus.OK:
                text = response.output.text
                delta = text[len(previous):]
                previous += delta
                if incremental:
                    yield delta
                else:
                    yield text
            else:
                logger.error('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))
                raise Exception('API ERROR')
        
    def ask(self, query: str, history: List[Tuple[str]] = [],
            temperature: float = 0.5, top_p: float = 0.7, presence_penalty: float = 0,
            frequency_penalty: float = 0, timeout: Tuple[float] | float = (15, 30), **kwargs) -> str:
        logger.info(f"qwen api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        history = [{'user': q, 'bot': a} for q, a in history]
        logger.info(f"qwen-7b history: {history}, query={query}")
        response = QWenGeneration.call(
            model=self.model_name,
            prompt=query,
            history=history,
            stream=False,
            api_key=self.api_key,
            top_p=top_p,
            timeout=timeout
        )
        if response.status_code == HTTPStatus.OK:
            return response.output.text
        else:
            logger.error('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))
            raise Exception('API ERROR')
        
    @classmethod
    def config_info(cls) -> str:
        info = """
        qwen config info:
        api_key: None (required)
        model_name: qwen-7b-chat-v1 (default)
        """
        return info
    
    @classmethod
    def check_config(cls, **kwargs) -> bool:
        if kwargs.get("api_key", None) is None:
            return False
        return True
        
    