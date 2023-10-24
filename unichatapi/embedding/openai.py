from typing import List, Tuple, Union
from loguru import logger
import openai
from .base import Embedding

class OpenAI(Embedding):
    def __init__(self, api_key:str, model_name='text-embedding-ada-002', api_base=None, **kwargs) -> None:
        super().__init__()
        self.llm_type = 'openai'
        self.api_key = api_key
        self.api_base = api_base
        self.model_name = model_name
        openai.api_key = self.api_key
        if api_base is not None:
            openai.api_base = api_base


    @classmethod
    def config_info(cls)->str:
        info = """
        openai config info:
        api_key: None (required)
        model_name: text-embedding-ada-002 (default)
        api_base: None (default)
        """
        return info
    
    @classmethod
    def check_config(cls, **kwargs)->bool:
        if kwargs.get("api_key", None) is None:
            return False
        return True       

    def encode(self, input:Union[str,List[str]], is_query=False, 
            timeout:Union[Tuple[float], float]=(15, 30), **kwargs) -> str:
        response = openai.Embedding.create(
                    model="text-embedding-ada-002",
                    input=input,
                    encoding_format="float",
                    timeout=timeout,
                    is_query=is_query
                    )
        if isinstance(input, str):
            embeddings = response.data[0].embedding
        else:
            embeddings = [data.embedding for data in response.data]
        return embeddings
        