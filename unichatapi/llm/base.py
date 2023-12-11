from typing import List, Tuple, Union, Generator
from loguru import logger

class LLM:
    SUPORTED_LLMS = ['chatglm', 'qwen', 'erniebot', 'erniebot4']

    def __init__(self) -> None:
        self.llm_type = None
    
    def ask_stream(self, query:str, history:List[Tuple[str]]=[], incremental:bool=False,
            temperature:float=0.5, top_p:float=0.7, 
            presence_penalty:float=0.0, frequency_penalty:float=0.0, 
            timeout:Union[Tuple[float], float]=(15, 30), **kwargs) -> Generator:
        raise NotImplementedError("ask_stream need implement in subclass !")

    def ask(self, query:str, history:List[Tuple[str]]=[],
            temperature:float=0.5, top_p:float=0.7, 
            presence_penalty:float=0.0, frequency_penalty:float=0.0, 
            timeout:Union[Tuple[float], float]=(15, 30), **kwargs) -> str:
        raise NotImplementedError("ask need implement in subclass !")
    
    
    @classmethod
    def from_llm_type(cls, llm_type:str, **kwargs):
        if llm_type not in cls.SUPORTED_LLMS:
            raise ValueError(f"llm_type {llm_type} not supported !")
        
        if llm_type == 'chatglm':
            from .chatglm import ChatGLM
            ok = ChatGLM.check_config(**kwargs)
            if not ok:
                logger.error(ChatGLM.config_info())
                raise ValueError(f"llm_type {llm_type} config error !")
            return ChatGLM(**kwargs)
        elif llm_type == 'qwen':
            from .qwen import Qwen
            ok = Qwen.check_config(**kwargs)
            if not ok:
                logger.error(Qwen.config_info())
                raise ValueError(f"llm_type {llm_type} config error !")
            return Qwen(**kwargs)
        elif llm_type == 'erniebot':
            from .erniebot import ErnieBot
            ok = ErnieBot.check_config(**kwargs)
            if not ok:
                logger.error(ErnieBot.config_info())
                raise ValueError(f"llm_type {llm_type} config error !")
            return ErnieBot(**kwargs)
        elif llm_type == 'erniebot4':
            from .erniebot4 import ErnieBot4
            ok = ErnieBot4.check_config(**kwargs)
            if not ok:
                logger.error(ErnieBot4.config_info())
                raise ValueError(f"llm_type {llm_type} config error !")
            return ErnieBot4(**kwargs)
        else:
            raise ValueError(f"llm_type {llm_type} not supported !")
        
    
    @classmethod
    def show_llm_config_info(cls, llm_type:str):
        if llm_type not in cls.SUPORTED_LLMS:
            raise ValueError(f"llm_type {llm_type} not supported !")
        
        if llm_type == 'chatglm':
            from .chatglm import ChatGLM
            info = ChatGLM.config_info()
            logger.info(info)
        elif llm_type == 'qwen':
            from .qwen import Qwen
            info = Qwen.config_info()
            logger.info(info)
        elif llm_type == 'erniebot':
            from .erniebot import ErnieBot
            info = ErnieBot.config_info()
            logger.info(info)
        elif llm_type == 'erniebot4':
            from .erniebot4 import ErnieBot4
            info = ErnieBot4.config_info()
        else:
            raise ValueError(f"llm_type {llm_type} not supported !")
        

    


        