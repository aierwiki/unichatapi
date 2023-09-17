from typing import List, Tuple, Union, Generator
from loguru import logger
import zhipuai
from .base import LLM

class ChatGLM(LLM):
    def __init__(self, api_key:str, model_name='chatglm_std', **kwargs) -> None:
        super().__init__()
        self.llm_type = 'chatglm'
        self.api_key = api_key
        self.model_name = model_name
        zhipuai.api_key = self.api_key

    @classmethod
    def config_info(cls)->str:
        info = """
        chatglm config info:
        api_key: None (required)
        model_name: chatglm_std (default)
        """
        return info
    
    @classmethod
    def check_config(cls, **kwargs)->bool:
        if kwargs.get("api_key", None) is None:
            return False
        return True
        
    
    def ask_stream(self, query:str, history:List[Tuple[str]]=[], incremental:bool=False,
            temperature:float=0.5, top_p:float=0.7, 
            presence_penalty:float=0.0, frequency_penalty:float=0.0, 
            timeout:Union[Tuple[float], float]=(15, 30), **kwargs) -> Union[str, Generator]:
        logger.info(f"chatglm api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        prompt = []
        for q, a in history:
            prompt.append({"role": "user", "content": q})
            prompt.append({"role": "assistant", "content": a})
        prompt.append({"role": "user", "content": query})
        logger.info(f"query messages: {prompt}")
        
        res_gen = zhipuai.model_api.sse_invoke(
            model="chatglm_std",
            prompt=prompt,
            temperature=temperature,
            top_p=top_p,
            incremental=incremental,
            request_timeout=timeout
        )

        for event in res_gen.events():
            if event.event == "add":
                content = event.data
                yield content
            elif event.event == "error" or event.event == "interrupted":
                raise Exception("interrupted")
            elif event.event == "finish":
                break
            else:
                break
            

    def ask(self, query:str, history:List[Tuple[str]]=[],
            temperature:float=0.5, top_p:float=0.7, 
            presence_penalty:float=0.0, frequency_penalty:float=0.0, 
            timeout:Union[Tuple[float], float]=(15, 30), **kwargs) -> str:
        logger.info(f"chatglm api parameters: temperature={temperature}, top_p={top_p}, presence_penalty={presence_penalty}, frequency_penalty={frequency_penalty}")
        prompt = []
        for q, a in history:
            prompt.append({"role": "user", "content": q})
            prompt.append({"role": "assistant", "content": a})
        prompt.append({"role": "user", "content": query})
        logger.info(f"query messages: {prompt}")

        res = zhipuai.model_api.invoke(
                model="chatglm_std",
                prompt=prompt,
                temperature=temperature,
                top_p=top_p,
                incremental=False,
                request_timeout=timeout
            )
        code = res.get("code", 0)
        msg = res.get("msg", "")
        if code != 200:
            raise Exception(f"chatglm api error: {msg}, code: {code}")
        res = res.get("data", "")
        status = res.get("task_status", "")
        if status != 'SUCCESS':
            raise Exception(f"chatglm api error: {res}")
        choices = res.get("choices", [])
        all_response = ""
        for choice in choices:
            if choice.get("role", "") == "assistant":
                response = choice.get("content", "")
                all_response += response
        return all_response