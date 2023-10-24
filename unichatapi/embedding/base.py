from typing import List, Tuple, Union
from loguru import logger

class Embedding:
    SUPORTED_EMBS = ['openai']

    def __init__(self) -> None:
        self.llm_type = None

    def encode(self, input:List[str], is_query=False, 
            timeout:Union[Tuple[float], float]=(15, 30), **kwargs) -> str:
        raise NotImplementedError("ask need implement in subclass !")
    
    
    @classmethod
    def from_emb_type(cls, llm_type:str, **kwargs):
        if llm_type not in cls.SUPORTED_EMBS:
            raise ValueError(f"llm_type {llm_type} not supported !")
        
        if llm_type == 'openai':
            from .openai import OpenAI
            OpenAI.check_config(**kwargs)
            return OpenAI(**kwargs)
        else:
            raise ValueError(f"llm_type {llm_type} not supported !")
        
    
    @classmethod
    def show_emb_config_info(cls, emb_type:str):
        if emb_type not in cls.SUPORTED_EMBS:
            raise ValueError(f"llm_type {emb_type} not supported !")
        
        if emb_type == 'openai':
            from .openai import OpenAI
            info = OpenAI.config_info()
            logger.info(info)
        else:
            raise ValueError(f"llm_type {emb_type} not supported !")
        

    


        