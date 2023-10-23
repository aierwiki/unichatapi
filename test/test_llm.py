import os
import sys
from unichatapi.llm import LLM
from unichatapi.llm import ChatGLM
from loguru import logger


def test_chatglm():
    api_key = os.getenv("API_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export API_KEY=xxx` or `code: zhipuai.api_key=xxx`")
    llm = LLM.from_llm_type('chatglm', api_key=api_key)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=True)
    for r in res:
        logger.info(r)
    
    logger.info("-------------")

    res = llm.ask_stream('你好', incremental=False)
    for r in res:
        logger.info(r)


def test_qwen():
    api_key = os.getenv("QWEN_API_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export QWEN_API_KEY=xxx` or `code: zhipuai.api_key=xxx`")
    llm = LLM.from_llm_type('qwen', api_key=api_key)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=True)
    for r in res:
        logger.info(r)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=False)
    for r in res:
        logger.info(r)


def test_erniebot():
    api_key = os.getenv("ERNIEBOT_API_KEY")
    if api_key is None:
        raise Exception("api_key not provided, you could provide it with `shell: export ERNIEBOT_API_KEY=xxx` or `code: zhipuai.api_key=xxx`")
    llm = LLM.from_llm_type('erniebot', api_key=api_key)
    res = llm.ask('你好')
    logger.info(res)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=True)
    for r in res:
        logger.info(r)
    logger.info("-------------")
    res = llm.ask_stream('你好', incremental=False)
    for r in res:
        logger.info(r)
    

def main():
    # test_chatglm()
    # test_qwen()
    test_erniebot()



if __name__ == "__main__":
    main()
